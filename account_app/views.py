from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
# from sendmail import settings
# Create your views here.

def register(request):
    if request.method =='POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form =RegistrationForm()
    return render(request, 'account_app/register.html',{'form':form})

def success(request):
    return render(request, 'account_app/success.html')



def email(request):
    if request.method=='POST':
        email= request.POST['email']
        msg=request.POST['msg']
        subject = 'Welcome to hafizul islam'
        massege=msg
        from_email = settings.EMAIL_HOST_USER
        recipent_list=[email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        return HttpResponse('Hafizul islam')
        
