#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import urllib2
import json

from collections import deque
 
f = open('data.json','wb')

queue = deque()
visited = set()
 
#url = 'http://news.dbanotes.net/'  # 入口页面, 可以换成别的
url = 'http://news.baidu.com/'  # 入口页面, 可以换成别的
char_type = 'utf-8'
 
queue.append(url)
cnt = 0
 
while queue:
	url = queue.popleft()  # 队首元素出队
  	visited |= {url}  # 标记为已访问
 
  	print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  	cnt += 1
	
	try:
  		urlop = urllib2.urlopen(url,timeout=6)
	except KeyboardInterrupt:
		break
 	except:
		print '超时 ---> '
		continue

  	# 避免程序异常中止, 用try..catch处理异常
  	try:
    		data = urlop.read()
		# Find out Web charset type
		char_match = re.search(r'.*?charset=(.*?)[\'\"].*?',data)
		if char_match:
			char_type = char_match.group(1) 
		data = data.decode(char_type).encode('utf-8')
		link_re = re.compile(r'<a.*?href=[\"\']([http://|https://].*?)[\"\'].*?>(.*?)</a>')
		link_list = link_re.findall(data)
		for i in link_list:
			f.write(i[0])
			f.write('\n')
			f.write(i[1])
			f.write('\n\n')
  	except:
		print 'Unexpected exception.'
    		#continue
 
  	# 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  	linkre = re.compile(r'<a.*?href=[\"\']([http://|https://].*?)[\"\'].*?>.*?</a>')
  	for x in linkre.findall(data):
	    	if 'http' in x and x not in visited:
      			queue.append(x)
      			print('加入队列 --->  ' + x)

f.close()
