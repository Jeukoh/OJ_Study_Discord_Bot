import sqlite3
from selenium import webdriver
import time
from Secure import *
import re
import json


class DB():
    def __init__(self, folder):
        self.path = folder + 'data.db'
        self.conn = sqlite3.connect(self.path)
        # BOJ_data_table = 'BOJ_data(number INTEGER not null PRIMARY KEY,name TEXT not null,rank integer not null, algorithm text)'
        # self.conn.execute(f'CREATE TABLE if not exists {BOJ_data_table}')
        # self.conn.commit()


    # number, name, rank, algorithm
    # def save(self, data, tablename='BOJ_data'):
    #     cur = self.conn.cursor()
    #     #print(f'{tablename}_save: data = \n{data}')
    #     cur.executemany(f'INSERT or Replace INTO {tablename} Values(?,?,?,?)', data)
    #     self.conn.commit()
    #     cur.close()


    def load(self,tablename,flag=False,**kwargs):
        output = ['number', 'name', 'rank']
        cond = []
        cond2 = []
        for key,value in kwargs.items():
            #print(key,value)
            if key == 'rank_low':
                cond.append(f'rank >= {value}')
                continue
            if key == 'rank_high':
                cond.append(f'rank <= {value}')
                continue

        buffer = ' and '.join(x for x in cond)
        if flag:
            buffer += ' ORDER BY RANDOM()'
        if kwargs.get('limit'):
            buffer += f' limit {kwargs["limit"]}'
        output = ', '.join(x for x in output)
        sql = f"select {output} from {tablename} where {buffer}"
        print(f'{tablename}_load sql {sql}')
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        #print(f'{tablename}_load_ rows {rows}')
        return rows



''':var

BOJ에서 웹 스크래핑을 금지하여 실행을 금합니다 ㅜ

'''

