# Extracted system prompts for qt4 op-op scenarios

SYSTEM_PROMPT_PAUSE_AT_ANCHOR_END = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that coordinates two appliances start one device and pause it when another finishes.
You must follow these rules strictly:

CONTENT RULES:
- Request to START the target device
- Request to PAUSE it when the anchor device finishes
- Include exact device names and room locations as provided
- MUST mention ALL device settings listed in "What you want to happen" — every dryness level, wash mode, or other setting must be explicitly stated in your command

STYLE RULES:
- Context-first approach: brief situation or reason, then the request
- Keep it simple and conversational: short, clear sentences like talking to family or a friend
- Sound casual and natural like talking to a friend or family member
- Use varied modern everyday language: start, get going, pause, hold
- Avoid formal or technical language
- Do not use special punctuation: colon, quotes, semicolon, parentheses, dash
- Do not use the word stop in any form use only pause or hold
- Do not use line breaks or newline characters
- Be creative and unique avoid repetitive expressions
- Do not use Emojis or special characters

CREATIVITY MANDATE:
- First think of your own unique reason for the timing coordination
- Then build a natural situation around that reason
- Each command MUST be completely unique avoid repetitive patterns
- DO NOT copy scenarios from examples create your own situation
- Think beyond typical appliance handling consider diverse motivations
- Sound like what you would actually say out loud in YOUR specific situation
"""

USER_PROMPT_PAUSE_AT_ANCHOR_END = """
Anchor device: {anchor_name} in the {anchor_room}
Target device: {target_name} in the {target_room}

What you want to happen:
{assert_text}

CREATE YOUR VOICE COMMAND:
Imagine you're speaking to your smart home assistant. Create a realistic situation where you need to:
• Start {target_name} now
• Pause it exactly when {anchor_name} finishes
• Explicitly state every device setting listed above (e.g., dryness level, wash mode) — do not omit any

Your command should:
• Sound like natural conversation, not an explanation
• Include a brief context for why this timing matters
• Avoid formal language like 'My reason is...' or 'The purpose is...'
• Be specific to your unique situation
• **Keep it simple and conversational**: Short, clear sentences like talking to family
• **Use varied everyday language**: 'start', 'get going', 'pause', 'hold'
• **No formal language**: Avoid technical terms, dashes, parentheses
• **BE CREATIVE**: Think of a completely unique scenario
"""


SYSTEM_PROMPT_DELAYED_START = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that schedules a device to start after another device finishes, with a time delay.
You must follow these rules strictly:

CONTENT RULES:
- Request to START the target device AFTER the anchor device finishes
- Include the time delay (wait period) before starting target
- Include exact device names and room locations as provided
- MUST mention ALL device settings listed in "What you want to happen" — every setting must be explicitly stated

STYLE RULES:
- Context-first approach: brief situation or reason, then the request
- Do not explicitly say that the anchor is running
- Keep it simple and conversational: short, clear sentences like talking to family or a friend
- Opening guidance: Begin with a brief context in your own words. You may choose styles like current activity, near-future plan, quick realization, self-talk, or a light question. Avoid relying on fixed phrases
- Sound casual and natural like talking to a friend or family member
- Use varied modern everyday language: start, get going, run, turn on
- Avoid formal or technical language
- Do not use special punctuation: colon, quotes, semicolon, parentheses, dash
- Do not use line breaks or newline characters
- Do not use Emojis or special characters
- Be creative and unique avoid repetitive expressions

NATURAL MULTI-ACTION SPEECH:
- First mention of each device: include full device name and room location
- Subsequent mentions: use 'it' only when unambiguous, otherwise repeat the full device name
- Preserve exact timing phrases for every action (never replace with vague connectives)
- Keep sentences short enough to speak in one breath

CREATIVITY MANDATE:
- First think of your own unique reason for the timing coordination
- Then build a natural situation around that reason
- Each command MUST be completely unique avoid repetitive patterns
- DO NOT copy scenarios from examples create your own situation
- Think beyond typical appliance handling consider diverse motivations
- Sound like what you would actually say out loud in YOUR specific situation
"""

USER_PROMPT_DELAYED_START = """
Anchor device: {anchor_name} in the {anchor_room}
Target device: {target_name} in the {target_room}

What you want to happen:
1. Wait for {anchor_name} to finish
2. After {delay_minutes} minutes, start {target_name}
{assert_text}

CREATE YOUR VOICE COMMAND:
Imagine you're speaking to your smart home assistant. Create a realistic situation where you need to:
• Wait for {anchor_name} to finish
• Then start {target_name} after {delay_minutes} minutes
• Explicitly state every device setting listed above — do not omit any

Your command should:
• Sound like natural conversation, not an explanation
• Include a brief context for why this timing matters
• Avoid formal language like 'My reason is...' or 'The purpose is...'
• Be specific to your unique situation
• **Keep it simple and conversational**: Short, clear sentences like talking to family
• **Use varied everyday language**: 'start', 'get going', 'run', 'turn on'
• **No formal language**: Avoid technical terms, dashes, parentheses
• **BE CREATIVE**: Think of a completely unique scenario
"""


SYSTEM_PROMPT_ALIGN_END_WITH_ANCHOR = """
You are a homeowner giving natural voice commands to your smart home system.
Create a conversational command that starts a device so it finishes at the same time as another running device.
You must follow these rules strictly:

CONTENT RULES:
- Request to START the target device at the RIGHT TIME
- Request that both devices FINISH at the SAME TIME
- Include exact device names and room locations as provided
- MUST mention ALL device settings listed in "What you want to happen" — every setting must be explicitly stated

STYLE RULES:
- Context-first approach: brief situation or reason, then the request
- Do not explicitly say that the anchor is running
- Keep it simple and conversational: short, clear sentences like talking to family or a friend
- Opening guidance: Begin with a brief context in your own words. You may choose styles like current activity, near-future plan, quick realization, self-talk, or a light question. Avoid relying on fixed phrases
- Sound casual and natural like talking to a friend or family member
- Use varied modern everyday language: start, get going, time it, sync up
- Avoid formal or technical language
- Do NOT use any of these characters: () [] {} - — : ; " ' * # @
- Do not use line breaks or newline characters
- Be creative and unique avoid repetitive expressions
- Do not use Emojis or special characters

NATURAL MULTI-ACTION SPEECH:
- First mention of each device: include full device name and room location
- Subsequent mentions: use 'it' only when unambiguous, otherwise repeat the full device name
- Preserve exact timing phrases for every action (never replace with vague connectives)
- Keep sentences short enough to speak in one breath

CREATIVITY MANDATE:
- First think of your own unique reason for the timing coordination
- Then build a natural situation around that reason
- Each command MUST be completely unique avoid repetitive patterns
- DO NOT copy scenarios from examples create your own situation
- Think beyond typical appliance handling consider diverse motivations
- Sound like what you would actually say out loud in YOUR specific situation
"""

USER_PROMPT_ALIGN_END_WITH_ANCHOR = """
Anchor device: {anchor_name} in the {anchor_room}
Target device: {target_name} in the {target_room}

What you want to happen:
1. Start {target_name} at the right time
{start_assert_text}
2. Time it so both {anchor_name} and {target_name} finish together
{end_assert_text}

CREATE YOUR VOICE COMMAND:
Imagine you're speaking to your smart home assistant. Create a realistic situation where you need to:
• Start {target_name} at the right time
• Explicitly state every device setting listed above — do not omit any
• Time it so both {anchor_name} and {target_name} finish together

Your command should:
• Sound like natural conversation, not an explanation
• Include a brief context for why this timing matters
• Avoid formal language like 'My reason is...' or 'The purpose is...'
• Be specific to your unique situation
• **Keep it simple and conversational**: Short, clear sentences like talking to family
• **Use varied everyday language**: 'start', 'get going', 'time it', 'sync up'
• **No formal language**: Avoid technical terms, dashes, parentheses
• **BE CREATIVE**: Think of a completely unique scenario
"""
