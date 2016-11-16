# -*- coding: utf-8 -*-

# prepare for Python version 3x features and functions
from __future__ import division, print_function

# -*- coding: utf-8 -*-

#PSE clear screen
import os
os.system('cls')

#PSE: edit...use below to check current working directory
print(os.getcwd())

os.chdir("C://Users//Peter//Documents//Personal//Grad School//nw - scs//Predict 452//individual assignment 1//craigslist_mcy")
print(os.getcwd())


# each spider class gives code for crawing and scraping
import scrapy  # object-oriented framework for crawling and scraping


os.system('scrapy list & pause')
os.system('scrapy crawl craigmcy2 -o craigslist_peter.csv')
os.system('scrapy crawl craigmcy2 -o craigslist_petert.csv \t')

os.system('scrapy crawl craigmcy2 -o craigslist_peter.xml  ')
os.system('scrapy crawl craigmcy2 -o craigslist_peter.json  ')
