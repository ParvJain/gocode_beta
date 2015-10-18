import requests
import json

def getPlaces(query, latitude, longitude):
	url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
           'key=AIzaSyAPHbSgdQneYb2vouuoS6eaxWTNu50JviQ'
           '&keyword={k}'
           '&location={l},{m}'
           '&radius=1000').format(k=query,l=latitude,m=longitude)

	r = requests.get(url)
	send = []
	data = json.loads(r.text)
	
	for x in data["results"]:
		url = ('https://maps.googleapis.com/maps/api/place/details/json?'
				   'placeid={place}'
				   '&key=AIzaSyAPHbSgdQneYb2vouuoS6eaxWTNu50JviQ').format(place=x["place_id"])

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

	return send

def getCity(latitude, longitude):
	url = ('https://maps.googleapis.com/maps/api/geocode/json?'
		   'address={lat},{lng}'
		   '&key=AIzaSyAPHbSgdQneYb2vouuoS6eaxWTNu50JviQ').format(lat=latitude,
		   														  lng=longitude)
	r = requests.get(url)
	data = json.loads(r.text)
	for x in data["results"]:
		if "locality" in x["types"]:
			return x["address_components"][0]["long_name"]

def getHotels(city_id):
	url = ('http://developer.goibibo.com/api/voyager/get_hotels_by_cityid/?'
		   'app_id=dde2de00'
		   '&app_key=ac404774f7d4a5b54e205adcd00dc7ef'
		   '&city_id=6771549831164675055')

	r = requests.get(url)
	data = json.loads(r.text)
	# print data["data"]["4325474491990470056"]["hotel_geo_node"]["name"]
	for x in data["data"]:
		name      = data["data"][x]["hotel_geo_node"]["name"]
		latitude  = data["data"][x]["hotel_geo_node"]["location"]["lat"]
		longitude = data["data"][x]["hotel_geo_node"]["location"]["lng"]

getHotels(6771549831164675055)
# getCity(12.9747865,77.560566)
# getPlaces("coffee",12.982470653198506,77.62573589101567)