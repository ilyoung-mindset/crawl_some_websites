# -*- coding: utf-8 -*-

from lxml import html
from lxml.etree import tostring
import requests
import codecs, os, re


for i in range(1,64): #change index
    url = 'https://www.ted.com/talks?page='+ str(i) +'&sort=popular'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    videos = tree.xpath('//div[@class="talk-link"]/div[@class="media media--sm-v"]/div[@class="media__image media__image--thumb talk-link__image"]/a')
    print('------------------------------------')
    print(i)
    print('------------------------------------')
    for video in videos:
        videourl = 'https://www.ted.com' + video.get("href")
        print(videourl)
        ko_transcripturl = videourl + '/transcript?language=ko'
        en_transcripturl = videourl + '/transcript?language=en'
        cn_transcripturl = videourl + '/transcript?language=zh-cn'
        ko_page = requests.get(ko_transcripturl)
        en_page = requests.get(en_transcripturl)
        cn_page = requests.get(cn_transcripturl)
        ko_tree = html.fromstring(ko_page.content)
        en_tree = html.fromstring(en_page.content)
        cn_tree = html.fromstring(cn_page.content)
        ko_transcript = ko_tree.xpath('//span[@class="talk-transcript__fragment"]/text()')
        en_transcript = en_tree.xpath('//span[@class="talk-transcript__fragment"]/text()')
        cn_transcript = cn_tree.xpath('//span[@class="talk-transcript__fragment"]/text()')
        ko_content = ''
        en_content = ''
        cn_content = ''
        for line in ko_transcript:
            ko_content += line.lstrip() + '\n'
        for line in en_transcript:
            en_content += line.lstrip() + '\n'
        for line in cn_transcript:
            cn_content += line.lstrip() + '\n'                                
        if (len(ko_content)<5)|(len(en_content)<5)|(len(cn_content)<5):
            next
        else:
            ko_filepath = "/Users/YiSangHyun/Desktop/TED/" + video.get("href")[7:] + "_ko.txt"
            en_filepath = "/Users/YiSangHyun/Desktop/TED/" + video.get("href")[7:] + "_en.txt"
            cn_filepath = "/Users/YiSangHyun/Desktop/TED/" + video.get("href")[7:] + "_cn.txt" 
            fk = codecs.open(ko_filepath,'w',encoding='utf8')
            fk.write(ko_content)
            fe = codecs.open(en_filepath,'w',encoding='utf8')
            fe.write(en_content)
            fc = codecs.open(cn_filepath,'w',encoding='utf8')
            fc.write(cn_content)

    
