from django.urls import path
from .api import *

urlpatterns = [
    path("list", MessageListApi), 
    path("create", MessageCreateApi),
    path('update/<int:id>', MessageUpdateApi),
    path('delete/<int:id>', MessageDeleteApi),
]
