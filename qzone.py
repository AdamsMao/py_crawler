#!/usr/bin/python
# -*- coding: utf-8 -*'

import spynner  
      
if __name__ == "__main__":  
	browser = spynner.Browser()  
        # 设置代理  
        #browser.set_proxy('http://host:port')  
        browser.show()  
        try:  
		browser.load(url='http://qzone.qq.com/', load_timeout=5, tries=1)  
        except:  
            	print 'Timeout.'  
        #browser.wait(5) 
        #browser.wk_click('a[class="switch_btn_focus"]', wait_load=True)  
	#browser.wait(3)
	# Input username & ID	
<<<<<<< HEAD
        #browser.wk_fill('input[id="u"]', '464048025@qq.com')  
	#browser.wait(3)
        #browser.wk_fill('input[id="p"]', 'Password')  
	#browser.wait(3)
=======
        browser.wk_fill('input[name="account"]', '464048025@qq.com')  
	browser.wait(3)
        browser.wk_fill('input[name="password"]', 'PASSWORD')  
	browser.wait(3)
>>>>>>> a9f8eaebbb4c7e30a885d34532647f70ea517e45
	# Click login
	#browser.wk_click('input[id="login_button"]', wait_load=True)
	# Wait to input verify code manually
	wait_value = raw_input('wait to input verify code manually!')
	browser.wait(5)
        # 获取页面的HTML  
        html = browser.html  
        if html:  
		html = html.encode('utf-8')  
		f = open('search_results.html', 'wb')
		f.write(html)  
		f.close()
	browser.close() 

 
