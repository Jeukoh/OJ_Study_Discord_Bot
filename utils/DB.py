import sqlite3
from selenium import webdriver
import time
from Secure import *
import re


class DB():
    def __init__(self, folder):
        self.path = folder + 'data.db'
        self.conn = sqlite3.connect(self.path)
        BOJ_data_table = 'BOJ_data(number INTEGER not null PRIMARY KEY,name TEXT not null,rank integer not null, algorithm text)'
        self.conn.execute(f'CREATE TABLE if not exists {BOJ_data_table}')
        self.conn.commit()


    # number, name, rank, algorithm
    def save(self, data, tablename='BOJ_data'):
        cur = self.conn.cursor()
        #print(f'{tablename}_save: data = \n{data}')
        cur.executemany(f'INSERT or Replace INTO {tablename} Values(?,?,?,?)', data)
        self.conn.commit()
        cur.close()


    def load(self,tablename='BOJ_data',output=['number', 'name', 'rank', 'algorithm'],**kwargs):
        cond = []
        for key,value in kwargs.items():
            #print(key,value)
            if key == 'rank_low':
                cond.append(f'rank >= {value}')
                continue
            if key == 'rank_high':
                cond.append(f'rank < {value}')
                continue
            if key == 'algorithm':
                cond.append(f'{key} like \"{value}\"')

        buffer = ' and '.join(x for x in cond)
        output = ', '.join(x for x in output)
        sql = f"select {output} from {tablename} where {buffer}"
        print(f'{tablename}_load sql {sql}')
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        print(f'{tablename}_load_ rows {rows}')
        return rows



''':var

BOJ에서 웹 스크래핑을 금지하여 실행을 금합니다 ㅜ

'''

# 셀레니움 실행 -> 로그인 -> nums problem db에 저장
# def AllBOJcralwer(start,num):
#     options = webdriver.ChromeOptions()
#     options.headless = True
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('disable-gpu')
#     options.add_argument('window-size=900x1080')
#     options.add_argument(
#         "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
#     options.add_argument("lang=ko_KR")
#     # 실제브라우져와 동일하게 작동하는 세션루틴실행
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     # 지정경로에 세션정보를 디스크에 저장하고 실행시마다 재사용함
#     options.add_argument(r'--user-data-dir='+Sessiondir)
#     driver = webdriver.Chrome('../Data/chromedriver.exe', chrome_options=options)
#
#
#     baseUrl = 'https://www.acmicpc.net/problem/'
#     driver.get(baseUrl)
#
#     # login
#
#     if not driver.find_element_by_xpath('/html/head/meta[13]').get_attribute('content'):
#         print('logining')
#         time.sleep(1)
#         driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/ul/li[3]/a').click()
#         time.sleep(1)
#         driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/input').send_keys(LoginName)
#         time.sleep(1)
#         driver.find_element_by_xpath('// *[ @ id = "login_form"] / div[3] / input').send_keys(Loginpassword)
#         time.sleep(1)
#         driver.find_element_by_xpath('// *[ @ id = "login_form"] / div[4] / div[1] / label / input').click()
#         time.sleep(1)
#         driver.find_element_by_xpath('// *[ @ id = "submit_button"]').click()
#
#     print('login!')
#     db = DB('../Data/')
#
#     ret = []
#     h = re.compile('[가-힣]+')
#     for number in range(start,start+num):
#         url = baseUrl+str(number)
#         driver.get(url)
#         try:
#             name = driver.find_element_by_xpath('//*[@id="problem_title"]').text
#             if not h.search(name):
#                 continue
#             rank = int(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[3]/div/blockquote/span').get_attribute('class').split('-')[-1])
#             if not rank:
#                 continue
#             algorithms = driver.find_elements_by_class_name('spoiler-link')
#             algorithm = ','.join(map(lambda x : x.get_attribute('textContent'), algorithms))
#             ret.append((number,name,rank,algorithm))
#         except:
#             continue
#         if not number%100:
#             db.save(ret)
#             ret = []
#
#     db.save(ret)
#     #print(ret)
#     print("DBsave!")

if __name__ == '__main__':
    pass
    #A = DB('../Data/')
