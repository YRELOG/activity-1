from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/Home.html'

class AboutPageView(TemplateView):
     template_name = 'app/about.html'

class ContactPageView(TemplateView):
     template_name = 'app/contact.html'


