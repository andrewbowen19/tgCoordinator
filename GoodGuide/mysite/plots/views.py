from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Guide, Visitor

from django.template import loader
from django.contrib.auth import authenticate, login
import matplotlib.pyplot as plt
import numpy as np
# Create your views here.
def index(request):
    guide_name = Guide.objects
    # output = ','.join([g.name for g in guides])
    template = loader.get_template('plots/index.html')
    context = {
        'guide_name': guide_name,
        
    }

    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the plot called %s."
    return HttpResponse(response % question_id)

def plot(request):
    # Need to include interactive plotting code here
    guide_name = Guide.objects

    template = loader.get_template('plots/plot.html')
    context = {
        'guide_name': guide_name,

    }

    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('registration/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

    else:
        return HttpResponse('Sorry, that user is not in our database.')








