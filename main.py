import datetime, os, sys
from discord.ext import commands
from discord.utils import get, find
# Secure
from Secure import *


parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)
client = commands.Bot(command_prefix=["!"])



@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print(client.get_all_channels())
    print("================")

#test
@client.command(name="ping",
                brief = "test 명령입니다")
async def _ping(ctx):
    await ctx.send('pong')



client.run(token)