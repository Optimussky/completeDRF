from django.urls import path
from .api import MessageListApi, MessageCreateApi

urlpatterns = [
    path('list',MessageListApi),
    path('create',MessageCreateApi)
]
