# python 3.7.1

"""Available Commands:
.support"""


import asyncio

from yaarabot.utils import admin_cmd


@yaarabot.on(admin_cmd(pattern="(.*)"))
@yaarabot.on(sudo_cmd(pattern="(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    input_str = event.pattern_match.group(1)
    if input_str == "support":
        await eor(event, input_str)
        animation_chars = [
            "Hello,",
            "Hello, do you need support?",
            "Then join the support group.",
            "[Join Now](t.me/YaaraBotHelpChat)",
            "[SUPPORT GROUP](t.me/YaaraBotHelpChat)",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await eor(event, animation_chars[i % 5])
