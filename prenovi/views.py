from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


def index(request):
    recent_posts = Post.objects.order_by('-date')[:3]
    return render(request, 'index.html', {'recent_posts': recent_posts})

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post
