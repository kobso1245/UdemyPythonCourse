from django.conf.urls import include
from django.urls import path
from help_app import views

urlpatterns = [
    path('', views.help),
]
