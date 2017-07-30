"""webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.PostListView.as_view(), name='posts'),
    url(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail-view'),
    url(r'^contractors/$', views.ContractorListView.as_view(), name='contractors'),
    url(r'contractor/(?P<pk>\d+)$', views.ContractorDetailView.as_view(), name='contractor-detail-view'),
    url(r'^workinstances/$', views.WorkInstanceListView.as_view(), name='workinstances'),
    url(r'workinstance/(?P<pk>[-\w]+)', views.WorkInstanceDetailView.as_view(), name='workinstance-detail-view'),

]