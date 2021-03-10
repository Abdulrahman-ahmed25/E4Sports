import django
from django.urls import path, include
from .views import SportNewsListView,SportNewDetailView

app_name = "sportnew"
urlpatterns = [
    path('',SportNewsListView.as_view(), name='news_list'),
    path('<int:pk>/',SportNewDetailView.as_view(), name='news_detail'),

]