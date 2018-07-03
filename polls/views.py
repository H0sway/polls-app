from django.shortcuts import render

# Create your views here.
# Import modules
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, you're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
