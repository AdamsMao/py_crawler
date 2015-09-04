#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib

urls = ['http://tieba.baidu.com/p/3969991000','http://tieba.baidu.com/p/4000737356']

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'src="(.+?\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	x = 0
	#for imgurl in imglist:
	#	urllib.urlretrieve(imgurl, '%s.jpg' % x)
	#	x += 1
	return imglist
	
def getLinks(html):
	reg = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
	linkre = re.compile(reg)
	linkslist = re.findall(linkre, html,re.S | re.I)
	#link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
	return linkslist

def crawl(urls):
	for i in urls:
		print i
		html = getHtml(i)
		links = getLinks(html)
		#print getImg(html)
		for l in links:
			self.urls.append(l)
	print self.urls
crawl(urls)
