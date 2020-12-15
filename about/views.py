from django.shortcuts import render
import logging
import logging.config
#from .models import About
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
            from_email = 'osullivanccuserjade@gmail.com'
            form_email_address=form.cleaned_data['email']
            to_email = [form_email_address,from_email]
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            message_body = message + ' from ' +  str(from_email)
            try:
                messages_sent = send_mail(subject, message_body, from_email,to_email ,fail_silently=False)
                logger.warn(str(name) + ' sent ' + str(messages_sent) + ' emails to ' + str(to_email) + ' from  '  + str(from_email) )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            context = {
                    'form':form,
                    }    
            messages.success(request, 'Your Email has been sent!')
            return render(request, 'about/about.html', context)    
            #return redirect('success')
        else:
            logger.warn('Invalid form  ')   

    context = {
        'form':form,
    }

    return render(request, 'about/about.html', context)
