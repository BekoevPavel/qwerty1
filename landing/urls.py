from django.conf.urls import url, include
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^', views.landing, name='landing'),
    url(r'^ff/', views.ff, name='ff'),
]