import django
from django.urls import path, include
from .views import SportNewsListView,SportNewDetailView
from . import api

app_name = "sportnew"
urlpatterns = [
    path('',SportNewsListView.as_view(), name='news_list'),
    path('<int:pk>/',SportNewDetailView.as_view(), name='news_detail'),

    #api 
    # path('api/news',api.SportNew_list_api, name='SportNew_list_api'),
    # path('api/news/<int:id>/',api.SportNew_detail_api, name='SportNew_detail_api'),

    #apis from generics view class
    path('api/news',api.SportNewListApi.as_view(), name='SportNew_list_api'),
    
    path('api/news/<int:id>/',api.SportNewDetailAPi.as_view(), name='SportNew_detail_api'),




]