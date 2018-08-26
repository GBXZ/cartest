from django.contrib import admin
from django.urls import path,include
from chat import views


urlpatterns = [
	path("weixin/",views.weixin)  
]
