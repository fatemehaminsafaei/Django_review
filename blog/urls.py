from django.urls import path
from .views import PostsList, Detail, Writer


urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<slug:slug>/', Detail.as_view(), name='post'),
    path('writer/<int:writer>', Writer.as_view(), name='writer_detail'),
]

