from django.urls import path
from .views import PostsList, Detail


urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<slug:slug>/', Detail.as_view(), name='post'),
]

