# -*- coding: utf-8 -*-

from lxml import html
from lxml.etree import tostring
import requests
import codecs, os, re


for i in range(1,19): #change range and below trailing url
	url = 'http://www.voachinese.com/archive/bilingual-news/' + str(i) + '/1737/2404.html'
	page = requests.get(url)
	tree = html.fromstring(page.content)
	firstlink = tree.xpath('//div[@class="articleContent zoomMe"]/a[@class="linksmall linkmore"]')
	otherlink = tree.xpath('//div[@class="archive_rowmm"]/h4[@class="black"]/a[@class=""]')

	firsturl = 'http://www.voachinese.com' + firstlink[0].get("href")
	firstpage = requests.get(firsturl)
	firsttree = html.fromstring(firstpage.content)
	title = firsttree.xpath('//div[@class="middle_content"]/h1/text()')
	title = title[0].lstrip()
	title = re.findall('\d+',title)
	if (len(title[1])==1):
                if(len(title[2])==1):
                        title = title[0]+'0'+title[1]+'0'+title[2]
                else:
                        title = title[0]+'0'+title[1]+title[2]
        else:
                if(len(title[2])==1):
                        title = title[0]+title[1]+'0'+title[2]
                else:
                        title = title[0]+title[1]+title[2]
                   
	print(title)
	content = firsttree.xpath('//div[@class="zoomMe"]')
	content = content[0].text_content().lstrip()
	
	newpath = "/Users/YiSangHyun/Desktop/VOA/"+title
	if os.path.exists(newpath):
                os.makedirs(newpath+'_1')
        else:
                os.makedirs(newpath)
        filepath = newpath+"/f.txt"
        f = codecs.open(filepath,'w', encoding = 'utf8')
        f.write(content)
        f = codecs.open(filepath,'r', encoding = 'utf8')
        english = ''
        chinese = ''
        for line in f:
                if(re.search(u'[\u4e00-\u9fff]+',line)):
                        chinese += line
                elif(re.search(u'[\u0041-\u005a\u0061-\u007a]+',line)):
                        english += line
                else:
                        next
        fc = codecs.open(newpath+"/c.txt",'w', encoding = 'utf8')
        fc.write(chinese)
        fe = codecs.open(newpath+"/e.txt",'w', encoding = 'utf8')
        fe.write(english)
        os.remove(filepath)
        
	for j in range(len(otherlink)):
		otherurl = 'http://www.voachinese.com' + otherlink[j].get("href")
		otherpage = requests.get(otherurl)
		othertree = html.fromstring(otherpage.content)
		title = othertree.xpath('//div[@class="middle_content"]/h1/text()')
		title = title[0].lstrip()
		title = re.findall('\d+',title)
		if (len(title[1])==1):
                        if(len(title[2])==1):
                                title = title[0]+'0'+title[1]+'0'+title[2]
                        else:
                                title = title[0]+'0'+title[1]+title[2]
                else:
                        if(len(title[2])==1):
                                title = title[0]+title[1]+'0'+title[2]
                        else:
                                title = title[0]+title[1]+title[2]
		print(title)
		content = othertree.xpath('//div[@class="zoomMe"]')
		content = content[0].text_content().lstrip()
		newpath = "/Users/YiSangHyun/Desktop/VOA/" + title
                if os.path.exists(newpath):
                        os.makedirs(newpath+'_1')
                else:
                        os.makedirs(newpath)
                filepath = newpath+"/f.txt"
                f = codecs.open(filepath,'w', encoding = 'utf8')
                f.write(content)
                f = codecs.open(filepath,'r', encoding = 'utf8')
                english = ''
                chinese = ''
                for line in f:
                        if(re.search(u'[\u4e00-\u9fff]+',line)):
                                chinese += line
                        elif(re.search(u'[\u0041-\u005a\u0061-\u007a]+',line)):
                                english += line
                        else:
                                next
                fc = codecs.open(newpath+"/c.txt",'w', encoding = 'utf8')
                fc.write(chinese)
                fe = codecs.open(newpath+"/e.txt",'w', encoding = 'utf8')
                fe.write(english)
                os.remove(filepath)


	
##page = requests.get('http://www.voachinese.com/content/bilingual-news-20120612/1207932.html')
##tree = html.fromstring(page.content)
##title = tree.xpath('//div[@class="articleContent"]/div[@class="dateblock"]/p[@class="article_date"]/text()')
##content = tree.xpath('//div[@class="zoomMe"]') 
##title = title[0].lstrip()[:10]
##content = content[0].text_content().lstrip()
##print(content)
##newpath = "/Users/YiSangHyun/Desktop/VOA/"+title
##os.makedirs(newpath)
##filepath = newpath+"/f.txt"
##f = codecs.open(filepath,'w', encoding = 'utf8')
##f.write(content)
##f = codecs.open(filepath,'r', encoding = 'utf8')
##english = ''
##chinese = ''
##
##for line in f:
##        if(re.search(u'[\u4e00-\u9fff]+',line)):
##                chinese += line
##        elif(re.search(u'[\u0041-\u005a\u0061-\u007a]+',line)):
##                english += line
##        else:
##                next
##
##                        
##fc = codecs.open(newpath+"/c.txt",'w', encoding = 'utf8')
##fc.write(chinese)
##fe = codecs.open(newpath+"/e.txt",'w', encoding = 'utf8')
##fe.write(english)
##os.remove(filepath)


#firstlink = tree.xpath('//div[@class="articleContent zoomMe"]/a[@class="linksmall linkmore"]')
#otherlink = tree.xpath('//div[@class="archive_rowmm"]/h4[@class="black"]/a[@class=""]')
#print('http://www.voachinese.com' + firstlink[0].get("href"))
#print(len(otherlink))


