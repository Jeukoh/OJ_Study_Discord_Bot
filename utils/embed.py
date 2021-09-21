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


def embed_print_BOJ_DB(ret,algoarg,author):
    korname = ['Bronze','Silver','Gold','Platinum','Diamond','Ruby']
    romenum = [' I', ' II', ' III', ' IV', ' V']
    f = lambda x : korname[(x-1)//5]+romenum[(4-(x-1)%5)]
    baseurl = 'https://www.acmicpc.net/problem/'
    title = f'{author.nick or author.name} 님의 요청 문제({algoarg})입니다. '
    embed = Embed(title=title)
    number_text = '\n'.join(f'[{x[0]}]({baseurl+str(x[0])})' for x in ret)
    name_text = '\n'.join(f'[{x[1]}]({baseurl+str(x[0])})' for x in ret)
    rank_text = '\n'.join(f'{f(x[2])}' for x in ret)
    embed.add_field(name="Numbers", value=number_text, inline=True)
    embed.add_field(name="Name", value=name_text, inline=True)
    embed.add_field(name="Rank", value=rank_text, inline=True)
    return embed

def embed_print_BOJ(ret,author):
    title = f'{author.nick or author.name} 님의 추천 문제입니다.'
    embed = Embed(title=title)
    rank_text = '\n'.join(f'{x["rank"]}' for x in ret)
    number_text = '\n'.join(f'[{x["number"]}]({x["url"]})' for x in ret)
    name_text = '\n'.join(f'[{x["name"]}]({x["url"]})' for x in ret)
    embed.add_field(name="Rank", value=rank_text, inline=True)
    embed.add_field(name="Numbers", value=number_text, inline=True)
    embed.add_field(name="Name", value=name_text, inline=True)
    return embed

def embed_temp():
    embed = Embed(title="Baekjoon 문제 검색기 사용법",\
                          description="!BOJ 명령어로 실행 가능합니다.\n 가능한 인수로는 (난이도, 알고리즘, 문제수 )가 있습니다.\n 인수 입력 방법은 Key:Value 입니다.",
                          color=0x3f2727)
    embed.add_field(name="Key 1 :  (난이도, rank, tier)", value="""
    Value : bronze(브론즈), silver(실버), gold(골드), platinum(플래티넘), diamond(다이아), ruby(루비)
    원하는 난이도만 검색합니다.
    한글입력 영어입력 모두 가능합니다. 구간을 표현하고 싶으시면 ~ 문자를 사용하시면 됩니다.
    한영 모두 첫글자만 사용하실 수도 있습니다.
    ex:  난이도:S5~G3, tier:실5~골3, rank:1~6 (== 브론즈1~실버5)
    미입력 시 기본 값은 모든 브론즈5~루비1입니다. 즉 모든 난이도를 다 검색합니다.""", inline=False)
    embed.add_field(name="Key 2 :  (알고리즘, 알고, algorithm, algo, tag)", value=f"""
        Value : dp, 다이나믹프로그래밍, 스택, dfs, 깊이우선탐색 등등
        원하시는 알고리즘 문제를 검색합니다. 한글입력 영어입력 모두 가능합니다. 
        데이터베이스에 없는 알고리즘을 요청하거나 오타가 났을 시 확인 과정이 있습니다.
        ex:  algo:dp, 알고:게임이론, 알고리즘:스택
        미입력 시 DB내 알고리즘 중 하나를 무작위 추출하여 줍니다.""", inline=False)
    embed.add_field(name="Key 3 :  (문제수, 수, limit, num, number)", value=f"""
        Value : <integer>
        원하시는 문제를 숫자를 입력합니다.
        ex:  num:5, 수:10, 문제수:7
        미입력 시 기본 값은 5입니다. 최대 값은 15입니다.""", inline=False)
    embed.add_field(name="-", value=r"""
    질문 및 추가 원하시는 알고리즘 문의는 직접 문의 및 [블로그](https://velog.io/@jeukoh26) 로 연락 주시면 감사합니다.
""",inline=False)

    return embed