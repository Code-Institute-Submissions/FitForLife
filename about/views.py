from django.shortcuts import render
import logging
import logging.config
from .models import About
from django.contrib import messages


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Get an instance of a logger
logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger



def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def about(request):
    """ A view to show all abouts, including sorting and search queries """


    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            try:
                messages_sent = send_mail(subject, message, from_email, ['osullivanccuserjade@gmail.com'],fail_silently=False)
                logger.warn(str(name) + ' sent  ' + str(messages_sent) + ' emails')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            context = {
                    'form':form,
                    }    
            messages.success(request, 'Email Sent!')
            return render(request, 'about/about.html', context)    
            #return redirect('success')
        else:
            logger.warn('Invalid form  ')   

    context = {
        'form':form,
    }

    return render(request, 'about/about.html', context)
