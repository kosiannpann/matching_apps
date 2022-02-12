from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.Template.View):
  template_name = "index.html"
