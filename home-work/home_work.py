#! /usr/bin/env python3

import requests
from pyquery import PyQuery as pq
import json

# 获取某页的乡野
def get_one_page(url):
    res = requests.get(url)
    return res.content.decode('utf8')

# 对某页内容进行解析生成对应的dict
def parse_one_page(html):
    doc = pq(html)
    dd = doc('.t')
    for item in dd.items():
        print(f'标题：{item.text()}')
        print(f"链接：{item('a').attr('href')}")
        yield {
            '标题': item.text(),
            '链接': item('a').attr('href')
        }

# 写入文件
def write_one_page(parse):
    with open('wuzhangpeng.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(parse, ensure_ascii=False)+'\n')

def main(word):
    url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={}&oq=%25E5%25B7%25AB%25E7%25AB%25A0%25E9%25B9%258F&rsv_pq=893dc9c500015fd0&rsv_t=dbebkn0JpQB8qBGxIhp5lH66j68gUrCo%2FgfN1yG7BlP37r%2FTZzWgw2nN8P8&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=1&rsv_sug1=1&rsv_sug7=000&rsv_sug2=0&inputT=4&rsv_sug4=917&rsv_sug=1'.format(
        str(word))
    html = get_one_page(url)
    for parse in parse_one_page(html):
        write_one_page(parse)

if __name__ == '__main__':
    main('巫章鹏')
