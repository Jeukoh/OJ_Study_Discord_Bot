import requests
from bs4 import BeautifulSoup
import re
import json


def BOJCrawler_solvedac(args:dict):
    url = 'https://solved.ac/search?query='
    query = []
    for  i in args.items():
        query.append('%3A'.join(x for x in i))
    query = '+'.join(x for x in query)
    query += '&sort=random'
    url += query
    html = requests.get(url).text
    bsObject = BeautifulSoup(html, "html.parser").select('div.StickyTable__Row-sc-10gspwa-2')
    ret = []
    h = re.compile('[가-힣]+')
    #print(bsObject)
    if bsObject:
        flag = url
        #print(bsObject)
        for item in bsObject[1:]:
            #print(item)
            rank = item.select_one('img.TierBadge__TierBadgeStyle-sc-zmdaar-0')['alt']
            num =  item.select_one('a.ProblemInline__ProblemStyle-sc-1w7zwvy-0').select_one('span').text
            name = item.select_one('a.hover_underline').select_one('span').text
            link = item.select_one('a.ProblemInline__ProblemStyle-sc-1w7zwvy-0')['href']
            #print(rank,num,name,link)
            if h.search(name):
                ret.append([rank,num,name,link])
    else:
        flag = False
        ret = url
    return ret, flag



def BOJcralwer(url):
    # return [number,name,rank_url]
    html = requests.get(url).text
    bsObject = BeautifulSoup(html, "html.parser")
    name = bsObject.select_one('#problem_title').text
    number = url.lstrip('https://www.acmicpc.net/problem/')
    url2 = 'https://solved.ac/search?query='+number
    html = requests.get(url2).text
    bsObject = BeautifulSoup(html, "html.parser")
    rank = bsObject.select_one('img.TierBadge__TierBadgeStyle-sc-zmdaar-0')['alt']

    return {'url':url,'number':number,'name':name,'rank':rank}




if __name__ == '__main__':
    #print(BOJCrawler_solvedac({'tier':'g2'}))

    print(BOJcralwer('https://www.acmicpc.net/problem/19539'))