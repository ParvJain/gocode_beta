import requests
import json
from operator import itemgetter

def getPlaces(query, latitude, longitude):
	url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
           'key=AIzaSyAPHbSgdQneYb2vouuoS6eaxWTNu50JviQ'
           '&keyword={k}'
           '&location={l},{m}'
           '&radius=1000').format(k=query,l=latitude,m=longitude)

	r = requests.get(url)
	send = []
	data = json.loads(r.text)
	return data["results"]


	# for x in data["results"]:
	# 	url = ('https://maps.googleapis.com/maps/api/place/details/json?'
	# 			   'placeid={place}'
	# 			   '&key=AIzaSyAPHbSgdQneYb2vouuoS6eaxWTNu50JviQ').format(place=x["place_id"])

	# 	r = requests.get(url)
	# 	data2 = json.loads(r.text)
	# 	x = data2["result"]
	# 	data3 = {"name": x.get("name",""),
	# 		   	 "address": x.get("formatted_address",""),
	# 		   	 "phone": x.get("formatted_phone_number", ""),
	# 		   	 "website": x.get("website",""),
	# 		   	 "ratings": x.get("rating",""),
	# 		   	 "price_level": x.get("price_level",""),
	# 		   	 "latitude": data2["result"]["geometry"]["location"]["lat"],
	# 		   	 "longitude": data2["result"]["geometry"]["location"]["lng"]
	# 		}
	# 	send.append(data3)

	# return send

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

def getHotels(latitude, longitude):
	city = getCity(latitude,longitude)
	url = "https://voyager.goibibo.com/api/v1/hotels_search/find_node_by_name/?params={%22limit%22:1,%22search_query%22:%22"+ city +"%22}&flavour=android"
	r = requests.get(url)
	data = json.loads(r.text)
	city_id = data["data"]["r"][0]["_id"]
	# print city_id
	url = str("https://www.goibibo.com/hotels/search-data/?vcid="+ str(city_id) +"&ci=20151018&co=20151019&r=1-1_0&pid=0&la="+ str(latitude) +"&lo="+ str(longitude) +"&s=nearby&f=%7B%22wl%22%3A%5B%5D%7D&flavour=android")

	r = requests.get(url)
	data = json.loads(r.text)
	return data[city_id]

# getHotels(12.9747865,77.560566)
# getCity(12.9747865,77.560566)
def rank(latitude, longitude, query):
	dataset = []
	for x in getHotels(latitude, longitude):
		lat = x["la"]
		lng = x["lo"]
		name = x["hn"]
		hid = x["hc"]
		gir_rat = x["gir_rat"]
		distance = x["dist"]

		gp = getPlaces(query, lat, lng)
		count = len(gp)
		data = {"hotel_name": name,
				"latitude": lat,
				"longitude": lng,
				"hid": hid,
				"count": count,
				"ratings":gir_rat,
				"distance": distance,
				"interest": gp}
		dataset.append(data)
		# ds = sorted(dataset.items(), key=lambda x: x["count"])
	return sorted(dataset, key=itemgetter('count'), reverse=True)

