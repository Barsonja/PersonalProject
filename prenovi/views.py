from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


def index(request):
    return render(request, 'index.html')

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post
