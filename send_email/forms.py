from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Your Email', required=True)
    subject = forms.CharField(label='Subject', required=True)
    message = forms.CharField(widget=forms.Textarea, label='Message', required=True)
