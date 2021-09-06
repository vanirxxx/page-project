from django.shortcuts import render

# Create your views 
from django.http import HttpResponse
from django.views.generic import TemplateView
class homePageView(TemplateView):
    template_name = 'home.html'
class aboutPageView(TemplateView):
    template_name = 'about.html'
