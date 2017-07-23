
# coding: utf-8

# In[3]:

import requests
from bs4 import BeautifulSoup
import time


# In[4]:

tStart = time.time()

url = "https://tw.search.bid.yahoo.com/search/auction/product?p=%E8%BE%A6%E5%85%AC%E6%A4%85&qt=product&kw=%E8%BE%A6%E5%85%AC%E6%A4%85&cid=0&clv=0&acu=0&pg=1"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html5lib")
for product in soup.select(".att-item"):
    name = product.select(".srp-pdtitle a")[0].text
    href = product.select(".srp-pdtitle")[0].find("a").attrs["href"]
    price = product.select(".srp-pdprice em")[0].text
    print(name+"\n"+href+"\n"+price)
    print("\n")
    
tEnd = time.time()
print("執行時間 :"+str(tEnd - tStart))


# In[ ]:



