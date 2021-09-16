from discord import Embed

def embed_print_BOJs(query,data,flag):
    title = f'(난이도:{query["tier"]}, 분류:{query["tag"]})'
    embed = Embed(title="추천 문제" + title, url=flag or data, color=0x00ff00)
    if flag:
        rank_text = '\n'.join(f'{x[0]}' for x in data[:10])
        number_text = '\n'.join(f'[{x[1]}]({x[3]})' for x in data[:10])
        name_text = '\n'.join(f'[{x[2]}]({x[3]})' for x in data[:10])

        embed.add_field(name="Rank", value=rank_text, inline=True)
        embed.add_field(name="Numbers", value=number_text, inline=True)
        embed.add_field(name="Name", value=name_text, inline=True)
    else:
        embed.add_field(name="요청이 잦습니다", value="링크에서 확인하세요 ㅜ")
    return embed

def embed_print_BOJ(ret,author):
    title = f'{author.nick} 님의 추천 문제입니다.'
    embed = Embed(title=title)
    rank_text = '\n'.join(f'{x["rank"]}' for x in ret)
    number_text = '\n'.join(f'[{x["number"]}]({x["url"]})' for x in ret)
    name_text = '\n'.join(f'[{x["name"]}]({x["url"]})' for x in ret)
    embed.add_field(name="Rank", value=rank_text, inline=True)
    embed.add_field(name="Numbers", value=number_text, inline=True)
    embed.add_field(name="Name", value=name_text, inline=True)
    return embed