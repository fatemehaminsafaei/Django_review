from django.shortcuts import render
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

class Writer(View):
    def get(self, request, writer):
        posts_list = Post.objects.filter(writer=writer)

        context = {'posts_list': posts_list}
        return render(request, 'blog/writer.html', context)