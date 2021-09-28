# NewsScrape
In this project i can create a simple Api for news 
where admin can add news by using api or adminpanel its also heve 
a features for ScrapeNews
where it scrape the news from thies website ['https://feeds.finance.yahoo.com/rss/2.0/headline?s=INTC,&amp;region=US&amp;lang=en-US','https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL,&amp;region=US&amp;lang=en-US','https://feeds.finance.yahoo.com/rss/2.0/headline?s=TWTR,&amp;region=US&amp;lang=en-US'] 
and render it 
i have also add celery for update the news every 60 secound

steps to run this project
This is for Windows
1. Insall all requirements using  pip install -r req.txt command
2. Install redis in you system windows 
    link:https://github.com/tporadowski/redis/releases
3. After setup the enviroment run the project on your local host
4. open 2 terminal with same path run this command celery -A NewsScrape.celery worker --pool=solo -l info
5. open 3 terminal with same path run this command celery -A NewsScrape.celery beat -l info
6. now you can see that celery hit the task every 60 seconds and update the News
  
for admin:
username =admin
password =admin
