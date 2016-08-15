# -*- coding: utf-8 -*-

from lxml import html
from lxml.etree import tostring
import requests
import codecs, os, re

url = 'http://cn.nytimes.com'
page = requests.get(url)
tree = html.fromstring(page.content)
leadHeadline  = tree.xpath('//div[@id="leadNews"]/h2[@class="leadHeadline"]/a')
regularSummaryHeadline = tree.xpath('//h3[@class="regularSummaryHeadline"]/a')
wellHeadline_top = tree.xpath('//li[@class="wellHeadline top"]/h3/a')
wellHeadline = tree.xpath('//li[@class="wellHeadline"]/a')
referListHeadline = tree.xpath('//h3[@class="referListHeadline"]/a')
commentSummaryHeadline = tree.xpath('//h3[@class="commentSummaryHeadline"]/a')
cf = tree.xpath('//td[@class="cf"]/div/a')

urllst = leadHeadline + regularSummaryHeadline + wellHeadline_top + wellHeadline + referListHeadline + commentSummaryHeadline + cf

e_text = ''
c_text = ''
n = 0
print(len(urllst))

for urls in urllst:
    url = 'http://cn.nytimes.com'
    urls = urls.get("href")
    if urls[:4] == "http" : #if nytStyle
        print("nytStyle")
        url = urls
        print(url)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        try:
            c_url = 'http://cn.nytstyle.com' + tree.xpath('//ul[@class="cf tabList"]/li[@class="zh-hans on"]/a')[0].get("href")
            print("a")
        except IndexError, e:
            print("b")
            continue
        else:
            try:
                e_url = 'http://cn.nytstyle.com' + tree.xpath('//ul[@class="cf tabList"]/li[@class="en-us "]/a')[0].get("href")
                print("c")
            except IndexError, e:
                print("d")
                continue
            else:
                print("e")
                c_page = requests.get(c_url)
                c_tree = html.fromstring(c_page.content)
                OnlyEnglishCheck = c_tree.xpath('//h3[@class="articleHeadline"]/text()')[0]
                l = len(OnlyEnglishCheck)
                if ('(' == OnlyEnglishCheck[l-4])&(')' == OnlyEnglishCheck[l-1]):
                    continue
                else:
                    c_title = c_tree.xpath('//h3[@class="articleHeadline"]/text()')[0].lstrip()
                    c_content = ''
                    for p in c_tree.xpath('//div[@class="content chinese"]/p[@class="paragraph"]'):
                        c_content += p.text_content().lstrip()
                    c_text += c_title + '\n' + c_content + '\n\n'
    
                    e_page = requests.get(e_url)
                    e_tree = html.fromstring(e_page.content)
                    e_title = e_tree.xpath('//h3[@class="articleHeadline"]/text()')[0].lstrip()
                    e_content = ''
                    for p in e_tree.xpath('//div[@class="content english"]/p[@class="paragraph"]'):
                        e_content += p.text_content().lstrip()
                    e_text += e_title + '\n' + e_content + '\n\n'
                    
                    n += 1
                    print(n)
    else:
        print("nyt")
        url = url + urls
        print(url)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        try:
            c_url = 'http://cn.nytimes.com' + tree.xpath('//ul[@class="cf tabList"]/li[@class="zh-hans on"]/a')[0].get("href")
            print("a")
        except IndexError, e:
            print("b")
            continue
        else:
            try:
                e_url = 'http://cn.nytimes.com' + tree.xpath('//ul[@class="cf tabList"]/li[@class="en-us "]/a')[0].get("href")
                print("c")
            except IndexError, e:
                print("d")
                continue
            else:
                print("e")
                c_page = requests.get(c_url)
                c_tree = html.fromstring(c_page.content)
                OnlyEnglishCheck = c_tree.xpath('//h3[@class="articleHeadline"]/text()')[0]
                l = len(OnlyEnglishCheck)
                if ('(' == OnlyEnglishCheck[l-4])&(')' == OnlyEnglishCheck[l-1]):
                    continue
                else:
                    c_title = c_tree.xpath('//h3[@class="articleHeadline"]/text()')[0].lstrip()
                    c_content = ''
                    for p in c_tree.xpath('//div[@class="content chinese"]/p[@class="paragraph"]'):
                        c_content += p.text_content().lstrip()
                    c_text += c_title + '\n' + c_content + '\n\n'

                    e_page = requests.get(e_url)
                    e_tree = html.fromstring(e_page.content)
                    e_title = e_tree.xpath('//h3[@class="articleHeadline"]/text()')[0].lstrip()
                    e_content = ''
                    for p in e_tree.xpath('//div[@class="content english"]/p[@class="paragraph"]'):
                        e_content += p.text_content().lstrip()
                    e_text += e_title + '\n' + e_content + '\n\n'

                    n += 1
                    print(n)

fe = codecs.open("/Users/YiSangHyun/Desktop/nyt_e.txt",'w',encoding='utf8')
fe.write(e_text)
fc = codecs.open("/Users/YiSangHyun/Desktop/nyt_c.txt",'w',encoding='utf8')
fc.write(c_text)

