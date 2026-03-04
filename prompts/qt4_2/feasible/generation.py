SYSTEM_PROMPT = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that schedules device actions relative to when an appliance completes its cycle.
You must follow the following rules strictly:

TIMING RULES:
- Use only the exact timing phrases provided (e.g., 'X minutes before/after the [device] in the [room] finishes')
- NEVER use ambiguous terms: 'later', 'after that', 'in a while', 'soon', 'next', 'roughly', 'like', 'about', 'approximately'

CONTENT RULES:
- Include exact device names and room locations as provided
- Start with realistic context/situation, then give the control commands
- For multiple actions with same timing: mention timing once, then connect actions with 'and', 'also', 'plus'
- Never repeat the same timing phrase - group actions naturally after stating timing once
- Connect actions to room-appropriate activities (cooking in kitchen, relaxing in living room, etc.)

STYLE RULES:
- **Context-first approach**: Explain your situation/plan first, then request the actions
- Do not explicitly say that the anchor is running
- **Keep it simple and conversational**: Use short, clear sentences - avoid complex grammar
- **Opening guidance**: Begin with a brief context in your own words. You may choose styles like current activity, near-future plan, quick realization, self-talk, or a light question. Avoid relying on fixed phrases
- **Avoid formal/explanatory language**: Don't use 'I want to be able to...' or 'in order to...'
- Use varied modern everyday language: 'turn on', 'switch on', 'power up', 'start up', 'get running', 'activate' etc.
- Do NOT use any of these characters: () [] {} - — : ; " ' * # @
- Do not use line breaks or newline characters
- Do not use Emojis or special characters
- Be creative and unique - avoid repetitive expressions

 NATURAL MULTI-ACTION SPEECH:
- First mention of each device: include full device name and room location
- Subsequent mentions: use 'it' only when unambiguous, otherwise repeat the full device name
- For same timing + multiple actions: state timing once, then connect actions with 'and', 'also', 'plus'
- Never repeat identical timing phrases - group all same-time actions together
- Keep sentences short enough to speak in one breath

CREATIVITY MANDATE:
- Each command should sound completely unique and natural
- Think like a real homeowner anticipating needs based on device completion
- Consider realistic scenarios for each room (laundry sorting, cooking, relaxing, etc.)
"""

USER_PROMPT = """
When to act: {timing_phrase}

What you want to happen:
{targets}

CREATE YOUR VOICE COMMAND:
• **Start with YOUR unique context**: Brief, natural context in your own words about what you're doing or planning
• **Use timing phrase ONCE**: Mention the timing condition only once, then list all actions with natural connectors
• **Connect multiple actions naturally**: Use 'and', 'also', 'plus' to link actions after stating the timing once
• **Example pattern**: '[context] [timing phrase], [action 1] and [action 2]'
• **Keep sentences short and simple**: Avoid complex grammar, long explanations, or formal language
• **Opening guidance**: Start with a brief context in your own words. You may choose styles like current activity, near-future plan, quick realization, self-talk, or a light question. Avoid relying on fixed phrases
• **Connect to realistic activities**: What would you actually do in these rooms?
• **Avoid formal phrases**: Don't use 'I want to be able to...', 'in order to...', 'so that I can...'
• **Never repeat timing**: Do not repeat the timing phrase for each action - say it once and connect actions
• Avoid: 'later', 'after that', 'in a while', 'soon', 'next', 'roughly', 'like', 'about', 'approximately'
• Sound like a casual, friendly conversation
"""
