from django.shortcuts import render

# Create your views here.

from .models import Question

def index(request):
    question = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions':question})


def detail(request, question_id):
    return render(request, 'detail.html', {'question_id' : question_id})

def result(request, question_id):
    return render(request, 'result.html', {'question_id' : question_id})
