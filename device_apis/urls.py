from django.contrib import admin
from django.urls import path
import device_apis.views as api_views

urlpatterns = [
    path("", api_views.home, name="home"),

]
