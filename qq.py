# -*- coding: utf-8 -*'

import spynner  
import time
      
if __name__ == "__main__":  
	browser = spynner.Browser()  
        # 设置代理  
        #browser.set_proxy('http://host:port')  
        browser.show()  
        try:  
		browser.load(url='http://qzone.qq.com', load_timeout=120, tries=1)  
        except spynner.SpynnerTimeout:  
            	print 'Timeout.'  
        else:
		browser.wait(5)  
           	browser.wk_fill('input[id="u"]', '464048025')  
           	browser.wk_fill('input[id="p"]', 'Dex156')  
		browser.wait(3)
            	browser.wk_click('input[id="login_button"]', wait_load=True)  
            	# 获取页面的HTML  
            	html = browser.html  
            	if html:  
                	html = html.encode('utf-8')  
                	open('html.html', 'w').write(html)  
	browser.close() 

 
