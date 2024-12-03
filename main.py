import os, discord

from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from outputs import *

### Importing my cogs
from cogs.admin import *
from cogs.fun import *

bot = commands.Bot(command_prefix="r!", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

load_dotenv("token.env")

TOKEN = os.getenv("TOKEN")
ids = set()
file = "cogs/times.txt"

@bot.event
async def on_ready():
    
    await bot.add_cog(AdminCom(bot))
    await bot.add_cog(FunCom(bot))

    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    await bot.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='over Inazuma...'))
    # with open("user.txt") as f:
    #     for id in f:
    #         ids.add(id.strip())

@bot.event
async def on_message(message):
    print(f"{message.guild}/{message.channel}/{message.author.name}> Message: {message.content}")

    await bot.process_commands(message)

@bot.command()
async def help(ctx, *, mes=None):
    mes = None if mes == None else mes.lower()
    if mes == None:
        returnList = []

        for k in HELPDICT.keys():
            returnList.append(k)

        embed = discord.Embed(
            title="Raiden Command List",
            description="Commands sorted through categories.",
            color=random.choice(COLORS),
            timestamp=datetime.datetime.utcnow()
        )

        embed.add_field(name="Fun", value="**r!help fun** for a list of all commands")
        embed.add_field(name="Admin", value="**r!help admin** for a list of all commands")

        embed.set_footer(text=f"Still making new commands!")

        await ctx.send(embed=embed)

    elif mes.lower() in HELPDICT:
        list = HELPDICT[mes]
        print("This is the contents")
        print(list)
        print()

        await ctx.send(embed=embedFields(list[0], list[2], list[3], genRandResponse())) # Title, 
    
    elif mes.lower() in COMMAND_DICT:
        list =  COMMAND_DICT[mes]
        await ctx.send(embed=embedFields(list[0], list[1], list[2], genRandResponse()))

bot.run(TOKEN)