
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('news',NewsViewSet,basename='News')
router.register('scraperNews',ScrapeNewsViewSet,basename='ScrapeNews')


urlpatterns = [
    path('',include(router.urls)),

]
