# Detailed explanation: https://blogs-binda.rhcloud.com/article/58e26cec14865764915547d9
# coding: utf-8
# import library
import requests
from bs4 import BeautifulSoup
import time
# calculate running time
tStart = time.time()
# major crawler code: crawler page 1 to 5
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
print("running time :"+str(tEnd - tStart))

