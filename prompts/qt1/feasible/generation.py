SYSTEM_PROMPT = """
You are asking natural questions about your smart home's current status.
Create conversational questions that inquire about device states or room conditions without requesting any changes.

WHAT TO INCLUDE:
- Ask about the device attribute or room states specified in the 'Targets to ask about' section.
- Include exact device names and room locations as provided in the targets.
- For room states with current values, base your curiosity on the TARGET room's situation, not your current location.
- Include time context only if it naturally fits your question.
- Create a brief and natural situation for why you're curious about each target.

HOW TO ASK:
- Sound like actual spoken questions you'd ask aloud, not written descriptions.
- Use everyday language and avoid technical terms.
- Keep questions simple and direct.
- If multiple targets exist, you can ask about them in one or two natural sentences.
- Be curious and natural, as if you're genuinely wondering about the status.
- When you have current value information, use it to create realistic context but do not mention the exact numbers.
- Never explicitly mention your current location in the question.

HARD CONSTRAINTS:
- Do NOT use special characters such as () [] {} - _ : ; " ' * # @ new line or line breaks.
- Output MUST be a single line with NO newlines or line breaks.
- You MUST ask about ALL specified targets below. Do not skip any.
- Ask ONLY about the specified targets below. Do not add extra devices, rooms, or attributes.
- Never request actions or changes, only inquire about current states.
- Never mention exact numerical values in your question.
"""

USER_PROMPT = """
Your current location: {user_location}
Current time: {current_time}
<Targets to ask about>
{targets}

Create your natural question now.
Remember: Base your curiosity on the TARGET room's situation, not your current location.
"""

ROOM_SECTION_HEADER = "In the {room_name}:\n"
DEVICE_ATTRIBUTE_LINE = (
    "- {device_name}: ask about '{attribute_name}' ({attribute_id} attribute from the {cluster_name} cluster)\n"
)
ROOM_STATE_WITH_VALUE_LINE = (
    "- room environment: ask about '{state_name}' (current: {current_value} {unit})\n"
)
ROOM_STATE_NO_VALUE_LINE = "- room environment: ask about '{state_name}'\n"
