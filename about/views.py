from django.shortcuts import render

# Create your views here.

from .models import About


# Create your views here.


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['osullivanccuserjade@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "about.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def about(request):
    """ A view to show all abouts, including sorting and search queries """

    abouts = About.objects.all()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['osullivanccuserjade@gmail.com'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                
            return redirect('success')

    context = {
        'abouts': abouts,
        'form':form,
    }

    return render(request, 'about/about.html', context)
