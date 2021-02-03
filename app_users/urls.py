from django.urls import path
from app_users.views import index,registeruser,loginuser

urlpatterns = [
    path('',index,name='index'),
    path('signup/',registeruser,name='signup'),
    path('login/',loginuser,name='login')
]
