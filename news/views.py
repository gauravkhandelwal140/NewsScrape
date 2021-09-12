from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics

from .models import *
import datetime
from .serializers import *

import requests
from bs4 import BeautifulSoup
from rest_framework import viewsets

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    filterset_fields = ['symbol']

    # def list(self,request):
    #     queryset=News.objects.all()
    #     serialize=NewsSerializer(queryset,many=True)
    #     return Response( serialize.data)
    #
    # def create(self,request):
    #     serialize = NewsSerializer(request.data)
    #     if serialize.is_valid():
    #         title=serialize.validated_data['title']
    #         description=serialize.validated_data['description']
    #         symbol=serialize.validated_data['symbol']
    #         link=serialize.validated_data['link']
    #         news=News(title=title,description=description,symbol=symbol,link=link)
    #         news.save()
    #         return Response({'message':'News Save SUCCESS' })
    #     else:
    #         return Response(serialize.errors)


class ScrapeNewsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NewsScrapeSerializer
    queryset = ScrapeNews.objects.all()
    filterset_fields = ['symbol']

    def filter_queryset(self, queryset):
        queryset = super(ScrapeNewsViewSet, self).filter_queryset(queryset)
        return queryset.order_by('pubDate')

