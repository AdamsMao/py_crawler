#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import urllib2
import json

from collections import deque

F = open('data.json','wb')
 
def items(html):
	try:
		items_re = re.compile(r'<a.*?href=[\"\']([http://|https://].*?)[\"\'].*?>(.*?)</a>')
		items_list = items_re.findall(html)
		pipeline(items_list)
	except:
		print 'Unexpected items exception.'

def pipeline(items):
	try:
		for i in items:
			F.write(i[0])
			F.write('\n')
			F.write(i[1])
			F.write('\n\n')
  	except:
		print 'Unexpected pipeline exception.'

class Spider:
	''' Spider class '''

	def __init__(self):
		#url = 'http://news.dbanotes.net/'  # 入口页面, 可以换成别的
		self.url = 'http://news.baidu.com/'  # 入口页面, 可以换成别的
		self.cnt = 0
		self.queue = deque()
		self.queue.append(self.url)
		self.visited = set()
		self.char_type = 'utf-8'

	def crawl(self):
		urlobj = None
		html = None
		while self.queue:
			url = self.queue.popleft()  # 队首元素出队
  			self.visited |= {url}  # 标记为已访问
 
  			print('已经抓取: ' + str(self.cnt) + '   正在抓取 <---  ' + url)
  			self.cnt += 1
	
			# Open a link, maybe meet a bad link, should rounded by try...catch
			try:
  				urlobj = urllib2.urlopen(url,timeout=6) # timeout 6 seconds
			except KeyboardInterrupt:  # Manual interrupt the spider
				break
 			except:
				print '超时 ---> '
				continue # Fetch next Url

  			# 避免程序异常中止, 用try..catch处理异常
  			try:
    				html = urlobj.read()
				# Find out Web charset type
				char_match = re.search(r'.*?charset=[\'\"]?(.*?)[\'\"].*?',html)
				if char_match:
					self.char_type = char_match.group(1) 
					html = html.decode(self.char_type).encode('utf-8')
					# 处理或者保存页面的内容
					items(html)	
  			except Exception as e:
				print 'Unexpected read() exception.'
 			finally:
				# 处理页面的hyperlinks
				self.filter_links(html)

	def filter_links(self,html):
		
		try:
			# 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  			linkre = re.compile(r'<a.*?href=[\"\']([http://|https://].*?)[\"\'].*?>.*?</a>')
			links = linkre.findall(html)
  			for x in links:
	    			if 'http' in x and x not in self.visited:
      					self.queue.append(x)
      					print('加入队列 --->  ' + x)
		except:
			print 'Unexpected filter_links() exception'

if __name__ == "__main__":
	spider = Spider()
	spider.crawl()
	F.close()

