SYSTEM_PROMPT = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that schedules a device action.
You must follow these rules strictly:

CONTENT RULES:
- Mention BOTH a clock time AND a relative time (X minutes from now)
- Include exact device names and room locations
- Include the specific action to perform on the device

STYLE RULES:
- Sound casual and natural
- Create natural, varied ways to express timing calculations
- Express the clock time FIRST, then the relative time as natural confirmation: "at [time], that's X minutes from now" — NOT the reverse
- STRICTLY FORBIDDEN: Do NOT use any of these characters: () [] {} _ — ; " ' * # @ & % $ !
- Be creative and unique
- Keep it conversational
- NEVER use ambiguous timing words: 'about', 'roughly', 'approximately', 'later', 'soon', 'in a while'
"""

USER_PROMPT = """
Your current location: {user_location}

Device to control: {target_name} in the {target_room}
Action to perform: {action_description}

What you want:
Perform this action at {conflict_time} — that is {expected_minutes} minutes from now

CREATE YOUR VOICE COMMAND:
• State the clock time first, then confirm with the relative time (e.g., "at 3:15, that's 13 minutes from now")
• Be specific about the exact action to perform
• Be specific and precise about the timing
• Add context for why you need this action
"""
