from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Different plot types %s." % question_id)

def results(request, question_id):
    response = "You're looking at the plot called %s."
    return HttpResponse(response % question_id)

def plot(request, question_id):
    return HttpResponse("You're viewing the plot! %s." % question_id)










