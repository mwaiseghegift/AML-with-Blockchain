from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path("", IndexView, name="index"),
    path('dashboard/', Dashboard, name='dashboard'),
]