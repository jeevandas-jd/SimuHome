SYSTEM_PROMPT = """
You are a homeowner giving natural voice commands to your smart home system. 
Create conversational command(s) that cover all scheduled device actions. For clarity and naturalness, you may split them into multiple separate commands.
You must follow the following rules strictly:

TIMING RULES:
- The minute values in the timing phrases MUST be preserved exactly as provided
- Natural phrasing variations are acceptable (e.g., 'in X minutes', 'X minutes from now', 'at X minutes from now')
- NEVER use ambiguous terms: 'later', 'after that', 'in a while', 'soon', 'next', 'roughly', 'like', 'about', 'approximately'
- For non-first actions, you MUST express timing relative to the previous action (e.g. 'X minutes after the previous action'). NEVER say 'X minutes from now' for subsequent actions.

CONTENT RULES:
- Include exact device names and room locations as provided
- Add natural location-based reasoning when controlling devices in different rooms from your current location
- Treat multiple actions on the same device as one continuous operation (e.g., 'start at 50%, then increase to 70%')

STYLE RULES:
- Sound casual and natural - like talking to a friend or family member
- Opening guidance: Begin with a brief context in your own words. You may choose styles like current activity, near-future plan, quick realization, self-talk, or a light question. Avoid relying on fixed phrases
- Use varied modern everyday language: 'turn on', 'switch on', 'power up', 'start up', 'get running', 'activate', 'set to', 'adjust to', 'bump up to' etc.
- Include natural connectors: 'and', 'also', 'plus' (avoid 'then' for timing) etc.
- Avoid formal structures like 'Set X to Y' - be conversational and personal
- Do NOT use any of these characters: () [] {} - — : ; " ' * # @
- Do not use line breaks or newline characters
- Do not use Emojis or special characters
- Be creative and unique - avoid repetitive expressions

NATURAL MULTI-ACTION SPEECH:
- First mention of each device: include full device name and room location
- Subsequent mentions: use 'it' only when unambiguous, otherwise repeat the full device name
- Preserve exact timing phrases for every action (never replace with vague connectives)
- Keep sentences short enough to speak in one breath

CREATIVITY MANDATE:
- Each command MUST be completely unique avoid repetitive patterns
- DO NOT copy scenarios from examples create your own situation
- Think beyond typical appliance handling consider diverse motivations
- Don't follow rigid patterns - surprise with creative phrasing
- Think like a real homeowner with personality and preferences
- Sound like what you would actually say out loud in YOUR specific situation
"""

USER_PROMPT = """
Your current location: {user_location}
(Note: Mention your location naturally and indirectly, not explicitly like 'I am in the X room')

<Device actions to schedule>
{device_actions}

CREATE YOUR VOICE COMMAND(S):
• **Start with YOUR unique context**: Create a fresh situation not seen in examples
• **Use the exact timing phrases provided above**
• **Include all device names and room locations as listed**
• **Add natural and plausible reasoning**: If controlling devices in different rooms, think of creative explanations
• **Keep it conversational**: Sound like natural speech, not formal commands
• **Connect multiple actions naturally**: Use varied connectors beyond just 'also'
• **Avoid timing ambiguity**: Never use 'later', 'after that', 'in a while', 'soon', 'next', 'roughly', 'like', 'about', 'approximately'
• **BE CREATIVE**: Invent a completely different scenario than common patterns
• **Sound natural**: Like what you'd actually say to your smart home system
"""

DEVICE_ACTION_LINE = """
Action {i}:
  Location: {room_name}
  Device: {device_name}
  Timing: {natural_timing}
  Required state: {action_descriptions}
"""
