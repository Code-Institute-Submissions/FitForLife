# sendemail/forms.py
from django import forms
#from .models import About

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,label='Subject')
    name = forms.CharField(max_length=100,label='Your name')
    name.widget = forms.TextInput(attrs={'size': 10, 'title': 'name','class':'form-control'})
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea,label='Message')

 