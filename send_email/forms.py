from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='Your Email', widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}),
                             required=True)
    name = forms.CharField(label='Your name', required=True)
    subject = forms.CharField(label='Subject', required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your inquiry'}), label='Message',
                              help_text='Enter your message', required=True)
