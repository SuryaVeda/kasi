from django.urls import path
from . import views

app_name = 'kasi'
urlpatterns = [
path('', views.homePage, name='home'),
path('comment', views.comment, name = 'comment')
]
