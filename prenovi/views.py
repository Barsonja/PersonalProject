from django.shortcuts import render
from django.views import generic
from .models import Post
from send_email.forms import ContactForm


# Create your views here.


def index(request):
    recent_posts = Post.objects.order_by('-date')[:3]
    form = ContactForm()
    return render(request, 'prenovi/index.html', {'recent_posts': recent_posts, 'form': form})

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post
