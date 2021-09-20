import datetime, os, sys
from discord.ext import commands
from discord.utils import get, find
# Secure
from Secure import *
from utils.crawler import *
from utils.embed import *
import re

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
    brief = "난이도(G1~G3) 태그(수학, 다이나믹 프로그래밍, 깊이 우선 탐색, 너비 우선 탐색, 그래프)"
                )
async def reprBOJ(ctx,*args):
    input_args = {'tier':args[0],'tag':args[1]}
    data, flag = BOJCrawler_solvedac(input_args)
    await ctx.send(embed=embed_print_BOJs(input_args,data,flag))
    await ctx.message.delete()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #print(message)
    # 추천문제 채널 문제 정리기
    if message.channel.id == 883333465720889353:
        a = re.findall("https://www.acmicpc.net/problem/[0-9]+",message.content)
        if a:
            ret = []
            for url in a:
                ret.append(BOJcralwer(url))
            await message.delete()
            await message.channel.send(embed=embed_print_BOJ(ret,message.author))


    await client.process_commands(message)

client.run(token)