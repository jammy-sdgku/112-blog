from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#home page
class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
#about page
class AboutPageView(TemplateView):
    template_name = "pages/about.html"