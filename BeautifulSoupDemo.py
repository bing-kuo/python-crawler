
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import time

tStart = time.time()
for i in range(5):
    print("page: "+str((i+1)))
    url = "https://tw.search.bid.yahoo.com/search/auction/product"
    url_params = {"p":"辦公椅", "qt":"product", "kw":"辦公椅", "cid":0, "clv":0, "acu":0, "pg":(i+1)}
    res = requests.get(url, params = url_params)
    soup = BeautifulSoup(res.text, "html5lib")
    
    for product in soup.select(".att-item"):
        name = product.select(".srp-pdtitle a")[0].text
        href = product.select(".srp-pdtitle")[0].find("a").attrs['href']
        price = product.select(".srp-pdprice em")[0].text
        print(name+"\n"+href+"\n"+price)
        print("\n")

tEnd = time.time()
print("Run Time :"+str(tEnd - tStart))

