import requests
from bs4 import BeautifulSoup

import pandas as pd
import time
import sys
import time # to time the requests
from multiprocessing import Process, Queue, Pool,Manager
import threading
import sys

proxies = { # define the proxies which you want to use
  'http': 'http://195.22.121.13:443',
  'https': 'http://195.22.121.13:443',
}
startTime = time.time()
qcount = 0 # the count in queue used to track the elements in queue
products=[] # List to store name of the product
prices=[] # List to store price of the product
ratings=[] # List to store ratings of the product
no_pages = 9 # no of pages to scrape in the website (provide it via arguments)


def get_data(pageNo,product):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    #r = requests.get("https://www.amazon.com/s?k=laptops&page="+str(pageNo), headers=headers)#,proxies=proxies)
    r = requests.get(f'https://www.amazon.com/s?k={product}&page='+str(pageNo), headers=headers)#,proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'lxml')
    for d in soup.findAll('div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
        #print(d)
        name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        price = d.find('span', attrs={'class':'a-offscreen'})
        if price is not None:
            print(name)
            print(price.text)

for i in range(10):
    get_data(i,'tv')



