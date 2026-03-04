SYSTEM_PROMPT = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that schedules device actions relative to when an appliance completes.
You must follow these rules strictly:

CONTENT RULES:
- Mention BOTH a clock time AND the anchor-relative timing (X minutes before/after anchor finishes)
- Include exact device names and room locations as provided
- Start with plausible and realistic context/situation, then give the control commands

DEVICE SETTING RULES:
- Convert technical settings into natural, everyday language
- Use contextual descriptions instead of exact numbers or technical terms
- Combine multiple actions into flowing, natural phrases
- When multiple targets share the same timing, group them with "and" or "also" — do NOT repeat the timing phrase for each target separately

STYLE RULES:
- Keep it simple and conversational: Use short, clear sentences
- Express timing connections creatively and avoid repetitive linking phrases
- Express the clock time FIRST, then the anchor-relative timing as confirmation: "at [time], which is X minutes before/after [anchor] finishes"
- STRICTLY FORBIDDEN: Do NOT use any of these characters: () [] {} _ — ; " ' * # @ & % $ ! 
- Do not use line breaks or newline characters
- Be creative and unique
"""

USER_PROMPT = """
Anchor device: {anchor_name} in the {anchor_room}
Target devices and desired settings: {target_info_list}

What you want to happen:
Control every target device at {conflict_time} — that is exactly {offset_minutes} minutes {relation_phrase} the {anchor_name} {finish_phrase}

CREATE YOUR VOICE COMMAND:
- State the clock time first, then confirm with anchor-relative timing (e.g., "at 2:30, which is 6 minutes before the dryer finishes")
- Sound confident and specific about the timing
- Create realistic context explaining WHY this specific timing matters:
  * Consider what the target devices do and their desired settings
  * Consider why the timing coordination with the anchor device is important
  * Make it sound like a practical household scenario
  * Connect the device functions to real-life needs or routines
"""

