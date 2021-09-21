import datetime, os, sys
from discord.ext import commands
from discord.utils import get, find
# Secure
from Secure import *
from utils.crawler import *
from utils.embed import *
import re
from utils.aliases import *
import utils.DB as dt
import random

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)
client = commands.Bot(command_prefix=["!"])
DB = dt.DB('Data/')


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
    name="BOJ_Solvedac",
    brief = "난이도(G1~G3) 태그(math, dp, bfs, dfs ...)"
                )
async def reprBOJ_solvedac(ctx,*args):
    input_args = {'tier':args[0],'tag':args[1]}
    data, flag = BOJCrawler_solvedac(input_args)
    #print(data,flag)
    await ctx.send(embed=embed_print_BOJs(input_args,data,flag))
    await ctx.message.delete()


@client.command(name="BOJ",brief = "난이도:G5~P3 알고리즘:dp 문제수:")
async def reprBOJ(ctx):
    kwargs = {}
    for idx,v in enumerate(ctx.message.content.split()):
        if idx == 0:
            continue
        key, value = v.split(':')
        if key.lower() in ['난이도','rank','tier']:
            kwargs['rank'] = value
            continue
        if key.lower() in ['알고리즘','알고','algorithm','algo','tag']:
            kwargs['algo'] = value
            continue
        if key.lower() in ['문제수','수','limit','num','number']:
            kwargs['limit'] = value
            continue
    try:
        algoarg_row = kwargs['algo']
        algoarg = load_algo_aliases(algoarg_row, r'Data/algo_aliases.json')
    except:
        algo_list = load_algo_aliases('None',r'Data/algo_aliases.json')
        algoarg = random.choice(algo_list)
    try:
        rank = kwargs['rank'].split('~')
        if len(rank) == 2:
            low_rank_row = rank[0]
            high_rank_row = rank[1]
            low_rank = load_rank_aliases(low_rank_row, r'Data/rank_aliases.json')
            high_rank = load_rank_aliases(high_rank_row, r'Data/rank_aliases.json')
            if int(low_rank) > int(high_rank):
                low_rank, high_rank = high_rank, low_rank
        else:
            low_rank = high_rank = load_rank_aliases(rank[0], r'Data/rank_aliases.json')
        if not (low_rank and high_rank):
            raise Exception

    except:
        low_rank = 1
        high_rank = 30
    try:
        limit = int(kwargs['limit'])
        if limit > 15:
            limit = 15
    except:
        limit = 5

    print(algoarg,ctx,kwargs)
    if str(type(algoarg)) == "<class 'list'>":
        msg1 = await ctx.send(f'{ctx.author.nick or ctx.author.name}님께서 요청하신 알고리즘 {algoarg_row}이(가) 다음 중 무엇인지 다시 한번 입력해주십시오.' \
                              + f'(None 입력 시 종료됩니다.)\n'+'\t'.join(algoarg))

        def check(m):
            return m.channel == ctx.channel and m.author == ctx.author
        msg2 = await client.wait_for('message',check=check)
        save_new_algo_aliases(msg2.content, algoarg_row, r'Data/algo_aliases.json')
        algoarg = msg2.content
        await msg1.delete()
        await msg2.delete()

    if algoarg.lower() == 'none':
        await ctx.message.delete()
        return

    data = DB.load(algoarg, flag=True, rank_low=low_rank, rank_high=high_rank, limit=limit)
    data.sort(key = lambda x: x[2])
    await ctx.send(embed=embed_print_BOJ_DB(data,algoarg,ctx.message.author))

@client.command(name="temp")
async def temp(ctx):
    await ctx.send(embed=embed_temp())


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