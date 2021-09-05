import discord


def embed_print_BOJ(query,data,flag):

    title = f'(난이도:{query["tier"]}, 분류:{query["tag"]})'
    embed = discord.Embed(title="추천 문제"+title, url=flag, color=0x00ff00)

    rank_text = '\n'.join(f'{x[0]}' for x in data[:10])
    number_text = '\n'.join(f'[{x[1]}]({x[3]})' for x in data[:10])
    name_text = '\n'.join(f'[{x[2]}]({x[3]})' for x in data[:10])

    embed.add_field(name="Rank", value=rank_text, inline=True)
    embed.add_field(name="Numbers", value=number_text, inline=True)
    embed.add_field(name="Name", value=name_text, inline=True)

    return embed