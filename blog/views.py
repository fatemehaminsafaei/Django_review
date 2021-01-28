from django.views.generic import View, ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Detail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context