from django.urls import path
from app_users.views import index,registeruser,loginuser,user_logout

urlpatterns = [
    path('',index,name='index'),
    path('signup/',registeruser,name='signup'),
    path('login/',loginuser,name='login'),
    path('logout/',user_logout,name='logout')
]
