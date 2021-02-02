from django.urls import path
from app_users.views import index

urlpatterns = [
    path('',index,name='index')
]
