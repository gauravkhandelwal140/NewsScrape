from django.utils.timezone import utc
from rest_framework import serializers
from .models import *
import datetime
from .models import models

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'


class NewsScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ScrapeNews
        fields='__all__'
