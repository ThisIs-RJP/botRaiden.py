# BOT_TOKEN: str = "MTA3ODQ3Njc1MDg2ODIwMTUyMw.G9IhOl.B-UVzkHbqBR3dPLn0B6EaO1LaBn25XK9Xm5Tug"

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
#### Create the initial embed object ####
# embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x109319)

# # Add author, thumbnail, fields, and footer to the embed
# embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")

# embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

# embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False)
# embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
# embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

# embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")

    # embed = discord.Embed(
    #     title = f"{PONG}",
    #     color = random.choice(COLORS)
    # )
    # await ctx.send(embed=embed)