from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.contact_us, name='contact-us'),
    url(r'send-email/success/$', views.success, name='success'),
    url(r'send-email/$', views.send_email, name='send-email'),
]