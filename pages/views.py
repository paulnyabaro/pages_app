from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'base.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'