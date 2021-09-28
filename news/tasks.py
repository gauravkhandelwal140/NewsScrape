from celery import shared_task
# from django.http import HttpResponse
# from django.shortcuts import render
# # Create your views here.
# from .models import *
# import datetime
from .serializers import *

import requests
from bs4 import BeautifulSoup
# from rest_framework import viewsets

@shared_task
def get_scripe_data():
    urls = ['https://feeds.finance.yahoo.com/rss/2.0/headline?s=INTC,&amp;region=US&amp;lang=en-US','https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL,&amp;region=US&amp;lang=en-US','https://feeds.finance.yahoo.com/rss/2.0/headline?s=TWTR,&amp;region=US&amp;lang=en-US']
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    for url in urls:
        html = requests.get(url, headers=header)
        soup = BeautifulSoup(html.content,"xml")
        item = soup.find_all('item')
        for news in item:
            try:
                guid = news.guid.text
            except:
                continue
            try:
                description = str(news.description.text)
            except:
                description =''
            try:
                link = str(news.link.text)
            except:
                link =''
            try:
                pubDate = news.pubDate.text.split(',')[1].strip()
                pubDate=datetime.datetime.strptime(pubDate, '%d %b %Y %H:%M:%S %z')

            except:
                pubDate = ''
            try:
                symbol = str(soup.find('channel').link.text.split('s')[1].replace('=', ''))
            except:
                symbol=''
            try:
                title = news.title.text

            except:
                title=''
            try:
                sn =ScrapeNews.objects.create(guid=guid,title=title,pubDate=pubDate ,description=description, link=link,symbol=symbol)

                sn.save()
            except:
                continue
    return 'yes'