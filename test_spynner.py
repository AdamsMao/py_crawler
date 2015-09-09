#!/usr/bin/python
# -*- coding: utf-8 -*'

import spynner  
      
if __name__ == "__main__":  
	browser = spynner.Browser()  
        # 设置代理  
        #browser.set_proxy('http://host:port')  
        browser.show()  
        try:  
		browser.load(url='http://www.zhihu.com', load_timeout=5, tries=1)  
        except:  
            	print 'Timeout.'  
         
        browser.wk_click('a[class="js-signin signin-switch with-icon"]', wait_load=True)  
	# Input username & ID	
        browser.wk_fill('input[name="account"]', '464048025@qq.com')  
	browser.wait(3)
        browser.wk_fill('input[name="password"]', 'Dex156')  
	browser.wait(3)
	# Click login
	#browser.wk_click('button[class="sign-button submit"]', wait_load=True)
        # 获取页面的HTML  
        html = browser.html  
        if html:  
		html = html.encode('utf-8')  
		f = open('search_results.html', 'wb')
		f.write(html)  
		f.close()
	browser.close() 

 
