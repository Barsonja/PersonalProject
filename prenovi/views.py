from django.shortcuts import render
from django.views import generic
from .models import Post, Contractor, WorkInstance
from send_email.forms import ContactForm


# Create your views here.


def index(request):
    recent_posts = Post.objects.order_by('-date')[:3]
    form = ContactForm()
    return render(request, 'prenovi/index.html')

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post


class ContractorListView(generic.ListView):
    model = Contractor
    paginate_by = 10


class ContractorDetailView(generic.DetailView):
    model = Contractor


class WorkInstanceListView(generic.ListView):
    model = WorkInstance
    paginate_by = 10

class WorkInstanceDetailView(generic.DetailView):
    model = WorkInstance