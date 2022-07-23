from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from yaarabot import CMD_HELP
from yaarabot.utils import admin_cmd


@yaarabot.on(admin_cmd(pattern="ascii ?(.*)"))
@yaarabot.on(sudo_cmd(pattern="ascii ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eor(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eor(event, "```reply to media message```")
        return
    chat = "@asciiart_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await eor(event, "```Reply to actual users message.```")
        return
    await eor(event, "```Wait making ASCII...```")
    # For YaaraBot
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=164766745)
            )
            await borg.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @asciiart_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await eor(
                event,
                "```can you kindly disable your forward privacy settings for good?```",
            )
        else:
            await borg.send_file(event.chat_id, response.message.media)


# For YaaraBot
CMD_HELP.update(
    {
        "ascii": "`.ascii` reply to any image file:\
      \nUse - Makes an image ascii style, try out your own.\
      "
    }
)
