
# coding: utf-8

# In[72]:

# version: 1.0
# author: Bing
# selenium demo
##############################################################
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
##############################################################


# In[75]:

# 新增一個Firefox driver
browser = webdriver.Firefox(executable_path=r"C:\Python\geckodriver.exe")

# 轉址到url
url = 'https://item.taobao.com/item.htm?id=542794230198&toSite=main'
browser.get(url)

# 找到元素(此處用xpath)，並且點擊
browser.find_element_by_xpath("//ul[@id='J_TabBar']/li[2]/a").click()

# sleep 5 sec，讓瀏覽器載入資料
time.sleep(5)

# 用BeautifulSoup parse 資料
soup = BeautifulSoup(browser.page_source, "html.parser")

# 取得評論的文字和時間
reviews = soup.select(".J_KgRate_ReviewItem")
for review in reviews:
    content = review.select(".review-details .tb-rev-item .tb-tbcr-content")[0].text
    content = content.strip()
    date = review.select(".review-details .tb-rev-item .tb-r-act-bar .tb-r-info .tb-r-date")[0].text
    print(content)    
    print(date)

#結束，關閉瀏覽器
browser.quit()


# In[ ]:




# In[ ]:



