import requests
import json

def getPlaces(query, latitude, longitude):
	url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
           'key=AIzaSyDC0jCu8MN8DPkIikVwubrerrP7ft4xYOA'
           '&keyword={k}'
           '&location={l},{m}'
           '&radius=1000').format(k=query,l=latitude,m=longitude)

	r = requests.get(url)
	send = []
	data = json.loads(r.text)
	
	for x in data["results"]:
		url = ('https://maps.googleapis.com/maps/api/place/details/json?'
				   'placeid={place}'
				   '&key=AIzaSyDC0jCu8MN8DPkIikVwubrerrP7ft4xYOA').format(place=x["place_id"])

		r = requests.get(url)
		data2 = json.loads(r.text)
		x = data2["result"]
		data3 = {"name": x.get("name",""),
			   	 "address": x.get("formatted_address",""),
			   	 "phone": x.get("formatted_phone_number", ""),
			   	 "website": x.get("website",""),
			   	 "ratings": x.get("rating",""),
			   	 "price_level": x.get("price_level",""),
			   	 "latitude": data2["result"]["geometry"]["location"]["lat"],
			   	 "longitude": data2["result"]["geometry"]["location"]["lng"]
			}
		send.append(data3)

	print send

# getPlaces("Coffee",12.9858731,77.6204105)