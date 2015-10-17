from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import requests
import json
from gocode import getPlaces


def index(request):
	if request.method == 'POST':
		query = request.POST["query"]
		latitude = request.POST["latitude"]
		longitude = request.POST["longitude"]

		dataset = getPlaces(query, latitude, longitude)
		jsonified = json.dumps(dataset)
		return render(request, 'result.html', {"rel" : jsonified,
											   "lat" : latitude,
											   "lng" : longitude})
		
	return render(request, 'db.html', {})
   # return HttpResponse('Hello from Python!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
