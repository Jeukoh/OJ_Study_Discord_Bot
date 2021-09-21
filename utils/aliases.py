import json

def load_algo_aliases(algoargs, file_path):
    algoargs = algoargs.lower().replace(' ','')
    with open(file_path, 'r') as outfile:
        json_data = json.load(outfile)

    ret = []
    for i,x in json_data.items():
        if algoargs in x:
            return i
        ret.append(i)

    return ret

def save_new_algo_aliases(key,value, file_path):
    with open(file_path, 'r') as outfile:
        json_data = json.load(outfile)
    try:
        json_data[key].append(value)
    except:
        json_data[key] = [value]

    with open(file_path,'w') as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False)


def load_rank_aliases(rankargs,file_path):
    rankargs = rankargs.lower().replace(' ', '')
    with open(file_path, 'r') as outfile:
        json_data = json.load(outfile)
        for i, x in json_data.items():
            if rankargs in x:
                return i
    return False

if __name__ == '__main__':

    # data = {}
    # data['다이나믹프로그래밍'] = ['다이나믹프로그래밍','dp','dynamic Programming','디피','dynamicProgramming']
    # data['구현'] = ['구현','implementation']
    # data['깊이우선탐색'] = ['깊이우선탐색','dfs', 'depthfirstsearch']
    # data['너비우선탐색'] = ['너비우선탐색', 'bfs', 'breadthfirstsearch', '넓이우선탐색']
    # data['그래프'] = ['그래프','graph']
    # data['백트래킹'] = ['백트래킹','백트레킹','backtracking']
    # data['자료구조'] = ['자료구조','datastructure']
    # data['비트마스크'] = ['비트마스크','bitmask']
    # data['트리'] = ['트리','tree']
    # data['이분탐색'] = ['이분탐색','binarysearch']
    # data['브루트포스'] = ['브루트포스','bruteforce']
    # data['게임이론'] = ['게임이론','gametheory']
    # data['스택']  = ['스택','stack']
    #
    # with open(file_path,'w') as outfile:
    #     json.dump(data, outfile, indent=4, ensure_ascii=False)

    pass
    #
    # with open(file_path, 'r') as outfile:
    #     json_data = json.load(outfile)
    # for i,x in json_data.items():
    #     print(i,x)

    # file_path = '../Data/rank_aliases.json'
    # # 1~5 브론즈 6~10 실버 11~15 골드 16~20 플레 21~25 다이아 26~30 루비
    # data = {i:[i] for i in range(1,31)}
    # korname = ['브론즈','실버','골드','플래티넘','다이아','루비']
    # engname = ['bronze','silver','gold','platinum','diamond','ruby']
    #
    # for idx in range(1,31):
    #     name_idx = (idx-1)//5
    #     rank_idx = 5-(idx-1)%5
    #
    #     data[idx].append(korname[name_idx]+str(rank_idx))
    #     data[idx].append(korname[name_idx][0] + str(rank_idx))
    #     data[idx].append(engname[name_idx]+str(rank_idx))
    #     data[idx].append(engname[name_idx][0] + str(rank_idx))
    #
    # with open(file_path,'w') as outfile:
    #     json.dump(data, outfile, indent=4, ensure_ascii=False)