from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='Your Email', required=True)
    subject = forms.CharField(label='Subject', required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your inquiry'}), label='Message',
                              help_text='Enter your message', required=True)
