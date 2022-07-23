# For YaaraBot
# By @AKASH_AM1 and @YaaraOP
# Kangers keep cr eors
from yaarabot import ALIVE_NAME
from yaarabot.utils import admin_cmd

n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

# @command(outgoing=True, pattern="^.ded$")


@yaarabot.on(admin_cmd(pattern=r"ded"))
@yaarabot.on(sudo_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await eor(
        ded,
        n + " ==             |\n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


M = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)
P = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)
K = r"_/﹋\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉ - -\n" r"_/﹋\_\n"
G = (
    "........___________________\n"
    "....../ `-___________--_____|] - - - - - -\n"
    " - - ░ ▒▓▓█D \n"
    "...../==o;;;;;;;;______.:/\n"
    ".....), -.(_(__) /\n"
    "....// (..) ), —\n"
    "...//___//\n"
)
D = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
H = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Hello, my friend :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)


@yaarabot.on(admin_cmd(pattern=r"monster"))
@yaarabot.on(sudo_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await eor(monster, M)


@yaarabot.on(admin_cmd(pattern=r"pig"))
@yaarabot.on(sudo_cmd(pattern=r"pig"))
async def bluedevipig(pig):
    await eor(pig, P)


@yaarabot.on(admin_cmd(pattern=r"kiler"))
@yaarabot.on(sudo_cmd(pattern=r"kiler"))
async def bluedevikiller(kiler):
    await eor(killer, K)


@yaarabot.on(admin_cmd(pattern=r"gun"))
@yaarabot.on(sudo_cmd(pattern=r"gun"))
async def bluedevigun(gun):
    await eor(gun, G)


@yaarabot.on(admin_cmd(pattern=r"dog"))
@yaarabot.on(sudo_cmd(pattern=r"dog"))
async def bluedevidog(dog):
    await eor(dog, D)


@yaarabot.on(admin_cmd(pattern=r"hmf"))
@yaarabot.on(sudo_cmd(pattern=r"hmf"))
async def bluedevihmf(hmf):
    await eor(hmf, H)
