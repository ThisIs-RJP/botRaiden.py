import discord
import random

""" 
    Basic Strings, for output, not for configs
"""

PONG: str = "PONG"
START_UP: list = ["Stay close and you will live.", "What's the situation?"]
POLL_MESSAGES: list = ["Another stupid opinion...", "NEVER LET THIS GUY COOK AGAIN! (?)"]
INVALID_INPUT: str = "That doesn't look like a valid input?"
RAIDEN_SUB_MSG: list = ["MEOW MEOW >:3", "BARK BARK"]
RAIDEN_HATE_MSG: list = ["DIE IN THE DEPTHS OF HELL", "ew"]
"""
    End of Basic Strings and lists    
"""

"""
    Configuration Strings and lists
"""

COLORS: list = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

"""
    end of Configuration Strings and lists
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
        color=random.choice(COLORS),
        description=d
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
