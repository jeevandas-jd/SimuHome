from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict

@dataclass
class HiMemory:
    """
    Hierarchical Memory Management for HiAgent.
    Includes boundary preservation sampling to keep critical observations.
    """
    subgoals: List[str] = field(default_factory=list)
    current_subgoal_index: int = 0
    short_term_memory: List[Dict[str, Any]] = field(default_factory=list)
    long_term_memory: List[str] = field(default_factory=list)
    critical_indices: List[int] = field(default_factory=list)  # Indices of critical observations
    max_short_term_size: int = 20  # Max size for sampling
    global_context: Dict[str, Any] = field(default_factory=dict)  # Persistent context across subgoals
    archived_trajectories: Dict[int, List[Dict[str, Any]]] = field(default_factory=dict)  # Archived detailed trajectories

    @property
    def current_subgoal(self) -> Optional[str]:
        if 0 <= self.current_subgoal_index < len(self.subgoals):
            return self.subgoals[self.current_subgoal_index]
        return None

    def set_subgoals(self, subgoals: List[str]) -> None:
        self.subgoals = subgoals
        self.current_subgoal_index = 0
        self.short_term_memory = []
        self.long_term_memory = []
        self.critical_indices = []
        self.archived_trajectories = {}

    def add_observation(self, action: str, action_input: str, observation: str) -> None:
        """Adds an action-observation pair to short-term memory."""
        self.short_term_memory.append({
            "action": action,
            "action_input": action_input,
            "observation": observation
        })
        
        # Auto-detect critical observations: first get_current_time
        if action == "get_current_time" and len(self.critical_indices) == 0:
            # Mark this as critical (index is len - 1 since we just appended)
            self.critical_indices.append(len(self.short_term_memory) - 1)

    def get_sampled_short_term_memory(self, max_size: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Returns boundary-preserved sampled short-term memory.
        
        Always includes:
        1. Critical observations (e.g., first get_current_time)
        2. Recent N observations
        3. If space allows, evenly distributed middle observations
        """
        if max_size is None:
            max_size = self.max_short_term_size
        
        memory_size = len(self.short_term_memory)
        
        # If we're under the limit, return everything
        if memory_size <= max_size:
            return self.short_term_memory
        
        # Boundary preservation logic
        result_indices = set()
        
        # 1. Add critical observations
        for idx in self.critical_indices:
            if idx < memory_size:
                result_indices.add(idx)
        
        # 2. Add recent observations (last 5 or 1/4 of max_size, whichever is larger)
        recent_count = max(5, max_size // 4)
        for idx in range(max(0, memory_size - recent_count), memory_size):
            result_indices.add(idx)
        
        # 3. Add first observation if not already included
        if 0 not in result_indices:
            result_indices.add(0)
        
        
        # 4. If we still have space, add evenly distributed middle observations
        remaining_slots = max_size - len(result_indices)
        if remaining_slots > 0:
            # Find available indices in the middle
            available = [i for i in range(1, memory_size - recent_count) if i not in result_indices]
            if available and len(available) > 0:
                # Sample evenly (but don't exceed remaining slots)
                num_to_sample = min(remaining_slots, len(available))
                step = max(1, len(available) // num_to_sample)
                for i in range(0, len(available), step):
                    if len(result_indices) >= max_size:
                        break
                    result_indices.add(available[i])
        
        # Return observations in order
        sorted_indices = sorted(list(result_indices))
        return [self.short_term_memory[i] for i in sorted_indices[:max_size]]

    def summarize_current_subgoal(self, summary: str) -> None:
        """Moves current subgoal info to long-term memory as a summary."""
        if self.current_subgoal:
            entry = f"Subgoal '{self.current_subgoal}' completed. Summary: {summary}"
            self.long_term_memory.append(entry)
            
            # Archive detailed trajectory before clearing
            self.archived_trajectories[self.current_subgoal_index] = list(self.short_term_memory)
        
        # Clear short-term memory for the next subgoal
        self.short_term_memory = []
        self.critical_indices = []  # Reset critical indices for new subgoal
        self.current_subgoal_index += 1

    def get_short_term_memory_str(self, use_sampling: bool = False, max_size: Optional[int] = None) -> str:
        """
        Returns formatted short-term memory string.
        
        Args:
            use_sampling: If True, use boundary-preserved sampling
            max_size: Maximum number of observations to include (if sampling)
        """
        memory = self.get_sampled_short_term_memory(max_size) if use_sampling else self.short_term_memory
        
        if not memory:
            return "No recent history."
        
        result = []
        for item in memory:
            result.append(f"Action: {item['action']}({item['action_input']})")
            result.append(f"Observation: {item['observation']}")
        return "\n".join(result)

    def get_long_term_memory_str(self) -> str:
        if not self.long_term_memory:
            return "No completed subgoals yet."
        return "\n".join(self.long_term_memory)

    def get_trajectory(self, subgoal_index: int) -> List[Dict[str, Any]]:
        """Retrieves the detailed trajectory for a specific subgoal index."""
        return self.archived_trajectories.get(subgoal_index, [])
