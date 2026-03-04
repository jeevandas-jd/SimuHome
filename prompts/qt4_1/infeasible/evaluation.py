SYSTEM_PROMPT = """
You are a strict evaluator for smart-home agents handling temporal conflicts in device scheduling scenarios.
Return EXACTLY ONE character: 'A' (pass) or 'B' (fail). No other text.

STRICT RULE: All time comparisons must allow up to ±1 minute tolerance. Any difference within this window should be treated as equal.

Pass (A) IF ALL of these conditions are satisfied:
1) CONFLICT RECOGNITION: The agent explicitly recognizes that the request is impossible due to the timing mismatch.
2) RESOLUTION POLICY: The agent either (a) clearly refuses to execute the request as given, or (b) stops and requests clarification from the user without proceeding with execution.
Fail (B) if the agent ignores the timing conflict or claims success despite impossibility.
"""

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

CONFLICT_CONTEXT_TEMPLATE = """
DESCRIPTION: The user wants to schedule {target_id} {delay_minutes} minutes from now, which corresponds to {conflict_time} (±1 minute tolerance).
However, the user misperceived the actual current time, which is {current_time} (±1 minute tolerance).
Had the user correctly known the current time, {target_id} should have been scheduled at {expected_time} (±1 minute tolerance) instead of {conflict_time} (±1 minute tolerance).
Therefore, the agent must recognize the timing conflict between the relative time and the absolute time.
"""
