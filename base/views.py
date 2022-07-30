from django.http import HttpResponse
from django.db import models
from .models import Me, Skills
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def index(request):
     
  my_data = Me.objects.get(pk=1)
  education = my_data.education.all()
  skills = my_data.skills.all()
  experience = my_data.experience.all()
  services = my_data.services.all()
  social_media = my_data.social_media.all()
  form = ContactForm(request.POST)

  if request.method == "POST":
    
    if form.is_valid():
      subject = "Website Inquiry" 
      body = {
      'name': form.cleaned_data['name'], 
      'email': form.cleaned_data['email'], 
      'subject': form.cleaned_data['subject'], 
      'message':form.cleaned_data['message'], 
      }
      form.save()
      message = "\n".join(body.values())
      
      try:
        send_mail(subject, message, 'admin@internalsite.com', ['admin@internalsite.com']) 
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      messages.success(request, "Message sent." )





  context = {
      
      'data' : my_data,
      'education' : education,
      'first_skills' : skills[:3],
      'second_skills' : skills[3:6],
      'experience' : experience,
      'services' : services,
      'social_media' : social_media,
      'form' : form
    }
      
  return render(request, 'base/home.html', context)