from yaarabot import CMD_HELP
from yaarabot.utils import admin_cmd


@yaarabot.on(admin_cmd(outgoing=True, pattern="group"))
@yaarabot.on(sudo_cmd(allow_sudo=True, pattern="group"))
async def join(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await eor(
            e,
            "This is my community.\n\n[Channel](http://t.me/giveaways_24hrs)\n\n[Chat Group](https://t.me/giveaways24hrsdiscuss)\n\n[UserBot Tutorial - YaaraBot](https://t.me/YaaraBotHelp)\n\n[YaaraBot Chat](https://t.me/YaaraBotHelpChat)\n\n[Github](https://github.com/YaaraOP)\n\n[YouTube](https://bit.ly/adityas7)",
        )


CMD_HELP.update({"group": ".group\nUse - None."})
