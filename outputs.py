### Output Configuration
import discord
from outputs import *
import datetime
import random

DESCRIPTION: str = "Greetings. I am the Raiden Shogun, the Electro Archon and the supreme ruler of the island nation of Inazuma"
COLORS: list = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

# COMMAND_DICT: dict = {
#     # TO ADD MORE COMMANDS HERE THE FORMAT
#     """
#     '' : ['', False, ''],
#     """
#     # ADMIN COMMANDS ###########################################################

#     # "clear" : ["Clear/Purge Command", "Usage: *r!clear <amount>*, default amount is 5", "Inputs = [integer], default=5\n Clears [integer] messages up to or the last 5 messages if integer is not specified"],
#     # "say" : ["Say Command", "Usage: *r!say <message>*", "Inputs = [anything as long as the length of the message > 0]\nSends your message through an embed, useful for announcements"],
#     # "specisay" : ["Specific Say Command", "Usage: *r!help <title name> <message>*", "Inputs = [anything as long as the length of the message > 0]\nSends your message through an embed, useful for announcements\nFormat: **r!specisay [This the title] This is the con"],
#     # "cdAdd" : ["Countdown Add Command", False, "Create an event to countdown to, follow with **r!cdFormat** for more details"],
#     # "cdFormat" : ["Countdown Format Command", False, "Returns the correct format to create timed events"],
#     # 'addrole' : ['Add Role Command', "Usage: *r!addrole <member> <role>*", 'Self explanatory'],
#     # 'removerole' : ['Remove Role Command', "Usage: *r!addrole <member> <role>*", 'Self Explanatory'],

#     # FUN COMMANDS ############################################################
#     # "poll" : ["Poll Command", "Usage: *r!poll <message>*", "Inputs = [anything]\n Returns an embed of your opinion to which members that see this can use emojis to determine if your opinionis valid or not"],
#     # "google" : ["Google Command", "Usage: *r!google <query>*", "Inputs = [anything]\nReturns a link to what you requested to look up E.G (r!google the raiden shogun) will return a link to google of the raiden shogun"],
#     "quote" : ["Help Command", "Usage: *r!quote @<USER>[]<query*", "Be sure to include the user! You can't quote a non existent person"]
# }

COMMAND_DICT: dict = {
    "quote" : ["Help Command", "Usage: *r!quote @<USER>[]<query*", "Be sure to include the user! You can't quote a non existent person"],
    "specisay" : ["Specific Say Command", "Usage: *r!help <title name> <message>*", "Inputs = [anything as long as the length of the message > 0]\nSends your message through an embed, useful for announcements\nFormat: **r!specisay [This the title] This is the con"],
}

HELPDICT: dict = {
    "fun"   : ["Fun Commands (cap sensitive)", False, "Here are our Fun commands", "quote\nkiss"],
    "admin" : ["Admin commands (cap sensitive, must have specific admin perms to call)", False, "Here are your admin commands", "clear\nsay\nspecisay\ncdAdd\ncdFormat\naddrole\nremoverole"]
}

KISS_LIST: list = ["https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-14.gif",
                   "https://media.tenor.com/YKd-wOisWB0AAAAC/anime-kiss.gif",
                   "https://media.tenor.com/6N4fuTkgpRIAAAAC/enage-kiss-anime-kiss.gif",
                   ]

COMMAND_STR: list = ["I wonder what you'll do with this information...", "r! is the prefix for this bot!", "Having fun?", "Currently adding new commands!"]

def genRandResponse():
    return f"{random.choice(COMMAND_STR)}"

def makeEmbed(title, link, d, mes):
    title = "Title" if title == False else title
    d = "Description" if d == False else d
    mes = "Message" if mes == False else mes
    link = None if link == False else link

    embed = discord.Embed(
        title=title,
        url=link,
        description=d,
        color=random.choice(COLORS),
        timestamp=datetime.datetime.utcnow()


    )
    embed.set_footer(text=f"{mes}")

    return embed

def embedFields(title, d, mes, footer):
    title = "Title" if title == False else title
    d = "Description" if d == False else d
    mes = "Message" if mes == False else mes

    embed = discord.Embed(
        title=title,
        description=d,
        timestamp=datetime.datetime.utcnow()
    )

    embed.add_field(name="Use **r!help**", value=f"{mes}")
    embed.set_footer(text=f"{footer}")

    return embed


def gifEmbed(title, gif, des, mes):
    title = title
    gif = gif
    des = des
    mes = mes

    embed = discord.Embed(
        title=title,
        description=des,
        color=random.choice(COLORS),
        timestamp=datetime.datetime.utcnow()

    )
    embed.set_footer(text=f"{mes}")
    embed.set_image(url=gif)

    return embed

def makeEmbedThumbNail(title, link, d, tmb, mes):
    title = "Title" if title == False else title
    link = None if link == False else link
    d = "Description" if d == False else d
    mes = "Message" if mes == False else mes

    embed = discord.Embed(
        title=title,
        url=link,
        color=random.choice(COLORS),
        description=d,
        timestamp=datetime.datetime.utcnow()

    )
    embed.set_thumbnail(url=tmb)
    embed.set_footer(text=f"{mes}")

    return embed
