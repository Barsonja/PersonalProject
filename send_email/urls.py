from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.email, name='email'),
    url(r'success/$', views.success, name='success'),
]