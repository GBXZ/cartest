
from django.contrib import admin
from django.urls import path,include
from cartest import views

urlpatterns = [
    path('index/', views.Index.as_view()),
    path('ajax_val/',views.ajax_val),
    path('refresh/',views.captcha_refresh),
]
