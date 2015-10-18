from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import requests
import json
from gocode import getPlaces, getCity
from models import city


def index(request):
	if request.method == 'POST':
		query = request.POST["query"]
		latitude = request.POST["latitude"]
		longitude = request.POST["longitude"]
		cty = getCity(latitude, longitude)
		ctyid = city.objects.get(city=cty).city_id
		# print ctyid
		dataset = getPlaces(query, latitude, longitude)
		jsonified = json.dumps(dataset)
		return render(request, 'result.html', {"rel" : jsonified,
											   "rel2": dataset,
											   "lat" : latitude,
											   "lng" : longitude})
		
	return render(request, 'index.html', {})
   # return HttpResponse('Hello from Python!')
