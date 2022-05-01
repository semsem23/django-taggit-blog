from django.urls import path
from .import views 

urlpatterns = [
    path('', views.post_list, name ='post_list'),
    path('create_tags/', views.create_tags, name ='create_tags'),
    path('<slug:slug>/', views.post_detail, name ='post_detail'),
    path('tags/<slug:slug>/', views.tagged, name ='tagged'),


]


