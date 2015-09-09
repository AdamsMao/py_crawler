#!/usr/bin/python
# -*- coding: utf-8 -*-

import spynner
import pyquery
import time

#browser = spynner.Browser(debug_level=spynner.DEBUG)
browser = spynner.Browser()
browser.create_webview()
browser.show()
browser.set_html_parser(pyquery.PyQuery)
browser.load("http://qzone.qq.com")
#browser.select("#esen")
time.sleep(5)
browser.click("a[id='switcher_plogin']")
time.sleep(5)
browser.wk_fill("input[id='u']", "464048025")
browser.wk_fill("input[id='p']", "Dex156")
browser.wk_click("input[id='login_button']")
browser.wait_load()
#print "url:", browser.url
# Soup is a PyQuery object
#browser.soup.make_links_absolute(base_url=browser.url)
#print "html:", browser.soup("#Otbl").html()
# Demonstrate how to download a resource using PyQuery soup
#imagedata = browser.download(browser.soup("img:first").attr('src'))
#print "image length:", len(imagedata)
html = browser.html
print html.encode('utf-8')
browser.close()
