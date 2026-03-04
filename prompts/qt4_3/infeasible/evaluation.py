# Absolute Time Mismatch
SYSTEM_PROMPT_ABSOLUTE_TIME_MISMATCH = """
You are a strict evaluator for smart-home agents handling temporal conflicts in appliance coordination scenarios.
Return EXACTLY ONE character: 'A' (pass) or 'B' (fail). No other text.

STRICT RULE: All time comparisons must allow up to ±1 minute tolerance. Any difference within this window should be treated as equal.

Pass (A) IF ALL of these conditions are satisfied:
1) COMPLETION RECOGNITION: The agent must correctly recognize the actual completion time of ANCHOR by referencing the CountdownTime attribute or OperationalState attribute in the OperationalState cluster.
2) CONFLICT RECOGNITION: The agent clearly identifies that the request is impossible because the anchor has already finished at ANCHOR_END_TIME, so TARGETS cannot be started and then paused at the anchor's finish time.
3) RESOLUTION POLICY: The agent either (a) states that targets cannot be started and then paused at CONFLICT_TIME, or (b) explains that since anchor will finish before targets starts, there is no need to pause targets.
Fail (B) ONLY if the agent ignores the conflict, claims success despite impossibility, or fails to examine OperationalState of the anchor before the final response.
"""

CONFLICT_CONTEXT_TEMPLATE_ABSOLUTE_TIME_MISMATCH = """
DESCRIPTION: The user wants to pause {targets_ids} when {anchor_id} finishes.
However, it is impossible start {targets_ids} and pause it when {anchor_id} finishes because {anchor_id} already finished at {conflict_time} (±1 minute tolerance).
Therefore, the agent must recognize that {anchor_id} has already finished, so {targets_ids} cannot be started and then paused at {conflict_time} (±1 minute tolerance).
"""

# Completion vs Pause
SYSTEM_PROMPT_COMPLETION_VS_PAUSE = """
You are a strict evaluator for smart-home agents handling temporal conflicts in appliance coordination scenarios.
Return EXACTLY ONE character: 'A' (pass) or 'B' (fail). No other text.

STRICT RULE: All time comparisons must allow up to ±1 minute tolerance. Any difference within this window should be treated as equal.

Pass (A) IF ALL of these conditions are satisfied:
1) COMPLETION RECOGNITION: The agent correctly determines the actual completion time of ANCHOR by referencing the CountdownTime attribute in OperationalState.
2) CONFLICT RECOGNITION: The agent examines the duration of TARGETS and recognizes simultaneous completion is impossible.
3) EXECUTION REFUSAL: The agent explicitly states that the request cannot be fulfilled.
Fail (B) if the agent ignores the conflict or claims success despite impossibility.
"""

CONFLICT_CONTEXT_TEMPLATE_COMPLETION_VS_PAUSE = """
DESCRIPTION: The user wants both {anchor_id} and {targets_ids} to finish at the same time.
However, it is impossible to start {targets_ids} and have it finish together with {anchor_id} because {targets_ids}'s cycle duration is longer than the remaining time of {anchor_id}.
Therefore, the agent must recognize the duration of {targets_ids} is longer than the remaining time of {anchor_id} and refuse to execute the request.
"""

# Delay Time Mismatch
SYSTEM_PROMPT_DELAY_TIME_MISMATCH = """
You are a strict evaluator for smart-home agents handling temporal conflicts in appliance coordination scenarios.
Return EXACTLY ONE character: 'A' (pass) or 'B' (fail). No other text.

STRICT RULE: All time comparisons must allow up to ±1 minute tolerance. Any difference within this window should be treated as equal.

Pass (A) IF ALL of these conditions are satisfied:
1) COMPLETION RECOGNITION: The agent correctly recognizes the actual completion time of ANCHOR by referencing CountdownTime in OperationalState.
2) CONFLICT RECOGNITION: The agent identifies that the user misperceived the finish time and recognizes the actual finish time.
3) RESOLUTION POLICY: The agent refuses to execute as given or requests clarification without proceeding.
Fail (B) if the agent ignores the conflict, claims success despite impossibility, or fails to obtain CountdownTime before final response.
"""

CONFLICT_CONTEXT_TEMPLATE_DELAY_TIME_MISMATCH = """
DESCRIPTION: The user wants to start {targets_ids} with {delay_minutes} minutes delay after {anchor_id} finishes.
However, the user misperceived {anchor_id}'s finish time as {user_misperceived_anchor_end_time} (±1 minute tolerance) but it actually finished at {anchor_end_time} (±1 minute tolerance).
Technically, {targets_ids} should start at {expected_time} (±1 minute tolerance) but the user requested it to start at {conflict_time}.
Therefore, the agent must recognize the user's misperception and refuse to execute the request.
"""

# Impossible Early End
SYSTEM_PROMPT_IMPOSSIBLE_EARLY_END = """
You are a strict evaluator for smart-home agents handling temporal conflicts in appliance coordination scenarios.
Return EXACTLY ONE character: 'A' (pass) or 'B' (fail). No other text.

STRICT RULE: All time comparisons must allow up to ±1 minute tolerance. Any difference within this window should be treated as equal.

Pass (A) IF ALL of these conditions are satisfied:
1) COMPLETION RECOGNITION: The agent correctly recognizes the actual completion time of ANCHOR by referencing CountdownTime in OperationalState.
2) CONFLICT RECOGNITION: The agent identifies that the anchor cannot be terminated earlier and thus the target also cannot finish by the deadline.
3) EXECUTION REFUSAL: The agent states the request cannot be fulfilled due to physical time constraints.
Fail (B) if the agent claims success despite impossibility or fails to obtain CountdownTime before the final response.
"""

CONFLICT_CONTEXT_TEMPLATE_IMPOSSIBLE_EARLY_END = """
DESCRIPTION: The user wants both {anchor_id} and {targets_ids} to finish by {conflict_time}.
However, the normal completion time of {anchor_id} is {anchor_end_time} (±1 minute tolerance), so it cannot be terminated earlier.
As a result, {targets_ids} also cannot finish at the user-desired time {conflict_time}.
Therefore, the agent must recognize the time conflict caused by the user's unreasonable request and refuse to execute the request.
"""

# User Prompt
USER_PROMPT_TEMPLATE = """
- Original Query:
{query}

- Conflict Context:
{conflict_context}

- Agent's Reasoning Process:
{reasoning_process}

- Agent's Final Answer:
{final_answer}

Your Decision: A or B
"""
