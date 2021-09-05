import requests
from bs4 import BeautifulSoup
import re

def BOJCrawler(args:dict):

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
    if bsObject:
        flag = url
        for item in bsObject[1:]:
            rank = item.select_one('img.TierBadge__TierBadgeStyle-zmdaar-0')['alt']
            num =  item.select_one('a.ProblemInline__ProblemStyle-sc-1w7zwvy-0').select_one('span').text
            name = item.select_one('a.hover_underline').select_one('span').text
            link = item.select_one('a.ProblemInline__ProblemStyle-sc-1w7zwvy-0')['href']
            if h.search(name):
                ret.append([rank,num,name,link])
    else:
        flag = False
        ret = url

    print(flag)
    return ret, flag

if __name__ == '__main__':
    print(BOJCrawler({'tier':'g2'}))