from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, "contact_us.html", {'form': form})


def send_email(request):
    # create a form instance and populate it with data from the request:
    form = ContactForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        try:
            send_mail(subject, message, email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid Header Found')
        return redirect('success')

def success(request):
    return render(request, "success.html")