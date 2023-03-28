import discord
import random

"""
    Configuration Strings and lists
"""

def genRandResponse():
    return f"{random.choice(COMMAND_STR)}"

COLORS: list = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

"""
    end of Configuration Strings and lists
"""

""" 
    Basic Strings, for output, not for configs
"""

def nsfw_nh_reply(s, t):
    return "You searched for: {} in the {} category".format(" ".join(s), t)

LINK: str = "https://i.kym-cdn.com/entries/icons/original/000/026/029/n.png"
LINK_NSFW_REPLY: str = "Heres a your requested nhentai link!"
COMMAND_STR: list = ["I wonder what you'll do with this information...", "r! is the prefix for this bot!", "Having fun?", "Currently adding new commands!"]
PONG: str = "PONG"
START_UP: list = ["Stay close and you will live.", "What's the situation?"]
POLL_MESSAGES: list = ["Another stupid opinion...", "NEVER LET THIS GUY COOK AGAIN! (?)"]
INVALID_INPUT: str = "That doesn't look like a valid input?"
RAIDEN_SUB_MSG: list = ["MEOW MEOW >:3", "BARK BARK"]
RAIDEN_HATE_MSG: list = ["DIE IN THE DEPTHS OF HELL", "ew"]
HELPDICT: dict = {
    "nsfw" : ["NSFW Commands (cap sensitive)", False, "Here are our NSFW commands", ""],
    "fun" : ["Fun Commands (cap sensitive)", False, "Here are our Fun commands", "poll\ngoogle\nsay\nhorni\nregister"],
    "admin" : ["Admin commands (cap sensitive, must have specific admin perms to call)", False, "Here are your admin commands", "clear\n"]
}

COMMAND_DICT: dict = {
    "register" : ["Register Command", False, "Inputs = Valid inputs: female, girl, woman, male, boy, man\nIf input == female, girl, woman, bot will occasionally meow or bark at user"],
    "google" : ["Google Command", False, "Inputs = [anything]\nReturns a link to what you requested to look up E.G (r!google the raiden shogun) will return a link to google of the raiden shogun"],
    "poll" : ["Poll Command", False, "Inputs = [anything]\n Returns an embed of your opinion to which members that see this can use emojis to determine if your opinionis valid or not"],
    "horni" : ["Horni Command", False, "Inputs= [None] or a mentioned user/user/name\n Bonks cus horny"],
    "clear" : ["Clear/Purge Command", False, "Inputs = [integer], default=5\n Clears [integer] messages up to or the last 5 messages if integer is not specified"],
    "say" : ["Say Command", False, "Inputs = [anything as long as the length of the message > 0]\nSends your message through an embed, useful for announcements"],
    "nhentai" : ["NHentai Command", False, "Inputs = [character/show/game], takes additional end arguments [all-time, today, week]\n Returns a link to the [character/show/game], if end argument is provided, it will return link under that category\ne.g r!nhentai raiden shogun all-time"]
}

"""
    End of Basic Strings and lists    
"""



"""
    Now for the classes and functions...
"""

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

    )
    embed.set_footer(text=f"{mes}")

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
        description=d
    )
    embed.set_thumbnail(url=tmb)
    embed.set_footer(text=f"{mes}")

    return embed
