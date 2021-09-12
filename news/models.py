from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    symbol =models.CharField(max_length=25,blank=True,null=True)
    link=models.URLField(blank=True,null=True)
    pubDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-->{self.symbol}'

class ScrapeNews(models.Model):
    guid=models.CharField(unique=True, max_length=250)
    title = models.CharField(max_length=255)
    description = models.TextField()
    symbol = models.CharField(max_length=25, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    pubDate = models.DateTimeField()

    def __str__(self):
        return f'{self.title}-->{self.symbol}'





