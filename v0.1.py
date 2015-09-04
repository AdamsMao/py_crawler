#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import urllib2
import json

from collections import deque
 
f = open('data.json','wb')

queue = deque()
visited = set()
 
url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
 
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
		link_re = re.compile(r'<a.*?>(.*?)</a>')
		link_list = link_re.findall(data)
		for i in link_list:
			#link_text = i.decode('utf-8')
			print i 
			#json_str = json.dumps(link_text) + '\n\n'
			f.write(i)
			f.write('\n\n')
  	except:
		print 'Unexpected exception.'
    		continue
 
  	# 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  	linkre = re.compile('href=\"(.+?)\"')
  	for x in linkre.findall(data):
	    	if 'http' in x and x not in visited:
      			queue.append(x)
      			print('加入队列 --->  ' + x)

f.close()
