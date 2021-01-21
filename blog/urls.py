from django.urls import path
from . import views
# from .views import PostList

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('',PostList.as_view, name ='blog'),
]