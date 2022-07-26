# (c)2022 YaaraBot
# You may not use this file without proper authorship and consent from @MissKaurSupport
#
"""
Available command(s)
.sticklol
Generates a. random laughing sticker.
"""
import random

from telethon import functions, types, utils

from yaarabot.utils import admin_cmd


def choser(cmd, pack, blacklist=None):
    if blacklist is None:
        blacklist = {}
    docs = None

    @yaarabot.on(admin_cmd(pattern=rf"{cmd}", outgoing=True))
    async def handler(event):
        await event.delete()

        nonlocal docs
        if docs is None:
            docs = [
                utils.get_input_document(x)
                for x in (
                    await borg(
                        functions.messages.GetStickerSetRequest(
                            types.InputStickerSetShortName(pack)
                        )
                    )
                ).documents
                if x.id not in blacklist
            ]

        await event.respond(file=random.choice(docs))


choser(
    "sticklol",
    "YaaraBot_LOLPack",
    {
        3088919966519394666,
        3088919966519394334,
        3088919966519394334,
        3088919966519394334,
    },
)
