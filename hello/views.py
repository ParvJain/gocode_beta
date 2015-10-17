from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import requests
import json


def index(request):
	if request.method == 'POST':
		latitude = request.POST["latitude"]
		longitude = request.POST["longitude"]
		query = request.POST["query"]

		return render(request, 'result.html', {})
		
	return render(request, 'db.html', {})
   # return HttpResponse('Hello from Python!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
