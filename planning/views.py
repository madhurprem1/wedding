from django.shortcuts import render
from django.views.generic import TemplateView
# from django.views import View
# Create your views here.
class AboutView(TemplateView):
    template_name = "planning/about.html"

class ComingView(TemplateView):
    template_name = "planning/comingsoon.html"

class HomeView(TemplateView):
    template_name = "planning/home.html"