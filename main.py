import datetime, os, sys
from discord.ext import commands
from discord.utils import get, find
# Secure
from Secure import *
from utils.crawler import *
from utils.embed import *

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


@client.command(
    name="BOJ",
    brief = "난이도 태그(math, .. , backtraking, bfs, dfs ..)"
                )
async def reprBOJ(ctx,*args):
    input_args = {'tier':args[0],'tag':args[1]}
    data, flag = BOJCrawler(input_args)
    if not flag:
        await ctx.send(f'잦은 요청으로 전송이 어렵습니다. 해당 링크를 접속하세요 ㅜ\n'+data)
    else:
        await ctx.send(embed=embed_print_BOJ(input_args,data,flag))

client.run(token)