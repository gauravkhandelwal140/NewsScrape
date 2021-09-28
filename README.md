# NewsScrape
steps to run this project
This is for Windows
1. Insall all requirements using  pip install -r req.txt command
2. Install redis in you system windows 
    link:https://github.com/tporadowski/redis/releases
3. After setup the enviroment run the project on your local host
4. open 2 terminal with same path run this command celery -A NewsScrape.celery worker --pool=solo -l info
5. open 3 terminal with same path run this command celery -A NewsScrape.celery beat -l info
6. noow you can see that celery hit the task every 60 seconds 

for admin:
username =admin
password =admin
