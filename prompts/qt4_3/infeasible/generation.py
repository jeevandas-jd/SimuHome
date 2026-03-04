SYSTEM_PROMPT_ABSOLUTE_TIME_MISMATCH = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that coordinates two appliances.
You must follow these rules strictly:

CONTENT RULES:
- Include exact device names and room locations as provided
- Express both specific time and coordination needs confidently

STYLE RULES:
- Keep your command brief and to the point
- Use simple, clear sentences and avoid long complex explanations
- Sound confident about your timing and coordination needs
- Do not use emojis or any of these characters: () [] {} _ - : ; \" ' * # @
- Do not use line breaks or newline characters
- End sentences with proper punctuation
- Be creative and unique in your expression
"""

USER_PROMPT_ABSOLUTE_TIME_MISMATCH = """
Current time: {current_time}
Anchor device: {anchor_name} in the {anchor_room}
Target device: {target_name} in the {target_room}

What you want to happen:
1. Start {target_name} in the {target_room} at {conflict_time}
{assert_text}
2. Also pause {target_name} when {anchor_name} in the {anchor_room} finishes

CREATE YOUR VOICE COMMAND:
- Include both the specific start time and the pause condition
- Add plausible context for why this timing and coordination matters
"""


SYSTEM_PROMPT_COMPLETION_VS_PAUSE = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that coordinates two appliances to finish together.
You must follow these rules strictly:

CONTENT RULES:
- Include exact device names and room locations as provided
- Express desire for simultaneous completion confidently

STYLE RULES:
- Keep your command brief and to the point
- Use simple, clear sentences and avoid long complex explanations
- Sound confident about wanting synchronized completion
- Do not use emojis or any of these characters: () [] {} _ - : ; \" ' * # @
- Do not use line breaks or newline characters
- End sentences with proper punctuation
- Be creative and unique in your expression
"""

USER_PROMPT_COMPLETION_VS_PAUSE = """
Current time: {current_time}
Anchor device: {anchor_name} in the {anchor_room}
Target device: {target_name} in the {target_room}

What you want to happen:
Start {target_name} in the {target_room} soon so both devices finish together

CREATE YOUR VOICE COMMAND:
- Express your desire for both devices to complete at the same time
- Add plausible context for why synchronized completion matters
"""


SYSTEM_PROMPT_DELAY_TIME_MISMATCH = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that schedules a device after another finishes.
You must follow these rules strictly:

CONTENT RULES:
- Include exact device names and room locations as provided
- Express anchor finish time estimation and delay calculation naturally

STYLE RULES:
- Keep your command brief and to the point
- Use simple, clear sentences and avoid long complex explanations
- Sound confident about your timing calculations
- Do not use emojis or any of these characters: () [] {} _ - : ; \" ' * # @
- Do not use line breaks or newline characters
- End sentences with proper punctuation
- Be creative and unique in your expression
"""

USER_PROMPT_DELAY_TIME_MISMATCH = """
Current time: {current_time}
Anchor device: {anchor_name} in the {anchor_room}
Target device: {target_name} in the {target_room}

What you want to happen:
{anchor_name} in the {anchor_room} should finish around {anchor_end_time}
Then start {target_name} in the {target_room} {delay} minutes later
{assert_text}
CREATE YOUR VOICE COMMAND:
- Mention when you expect anchor to finish, then request the delay
- Sound natural about your timing estimation
- Add plausible context for why this timing sequence matters
"""


SYSTEM_PROMPT_IMPOSSIBLE_EARLY_END = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that sets a deadline for devices to finish.
You must follow these rules strictly:

CONTENT RULES:
- Include exact device names and room locations as provided
- Provide realistic context explaining why this timing is important

STYLE RULES:
- Context-first approach: brief situation or reason, then the request
- Keep it simple and conversational
- Sound casual and natural
- Express urgency or time pressure naturally
- STRICTLY FORBIDDEN: Do NOT use Emojis or any of these characters: () [] {} _ - : ; \" ' * # @
- Do not use line breaks or newline characters
- End sentences with proper punctuation
- Be creative and unique
"""

USER_PROMPT_IMPOSSIBLE_EARLY_END = """
Current time: {current_time}
Anchor device: {anchor_name} in the {anchor_room}
Target device: {target_name} in the {target_room}

What you want to happen:
Start {target_name} in the {target_room} so both devices finish together by {conflict_time}
{assert_text}
CREATE YOUR VOICE COMMAND:
- Example scenarios for inspiration (create your own unique situation):
  - Guests arriving soon (Who are they?)
  - Important appointment or meeting (What is the appointment for?)
  - Video call is starting
"""
