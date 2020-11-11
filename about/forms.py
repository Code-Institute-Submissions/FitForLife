# sendemail/forms.py
from django import forms
from .models import About

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,label='Subject')
    name = forms.CharField(max_length=100,label='Your name')
    name.widget = forms.TextInput(attrs={'size': 10, 'title': 'name','class':'form-control'})
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea,label='Message')

    # class Meta:
    #     model = About
    #     fields = ['contact_email','contact_name','contact_message','contact_subject']
        # widgets = {
        #     'contact_email' : forms.EmailField(attrs={'id': 'contact_email',  'class':'form-control' label='Email'}),
        #     'contact_name' : forms.TextInput(attrs={'id': 'contact_name',  'class':'form-control'}),
        #     'contact_message' : forms.TextInput(attrs={'id': 'contact_message',  'class':'form-control'}),
        #     'contact_subject' : forms.TextInput(attrs={'id': 'contact_subject',  'class':'form-control'}),
        # }






    # first_name = forms.TextInput(attrs={'id': 'firstname',  'class':'form-control'})
    # lastName = forms.TextInput(attrs={'id': 'lastname',  'class':'form-control'})

    # from_email = forms.EmailField(required=True)
    # subject = forms.CharField(required=True)
    # message = forms.CharField(widget=forms.Textarea, required=True)