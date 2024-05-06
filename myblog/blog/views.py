from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post

# Create your views here.

class Homeview(ListView):
    model = post
    template_name = 'blog/home.html'
    
class ArtileDetailview(DetailView):
    model = post
    template_name = 'blog/article_details.html'
