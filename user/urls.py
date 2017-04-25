from django.conf.urls import url,include
from django.contrib import admin
from user.views import *


urlpatterns = [
    
    url(r'^home/', 'views.profile', name="profile"),
    

]