#Get address of a place using Googgle Maps API

import requests

def getAddress(location):
	URL = "http://maps.googleapis.com/maps/api/geocode/json"  # Google Maps API, plays with JSON back and forth
	PARAMS = {'address': location}  # The parameters for request

	try:
		req = requests.get(url=URL, params=PARAMS)  # Sending the request and saving the response as response object
		data = req.json()  # Extracting data in json format
	except Exception as err:  # Too lazy to use specific Exception but I'm pretty sure network error is most likely 
		print("Network Error")
		quit()  # Exit the program 

	try:
		formatted_address = data['results'][0]['formatted_address']  # If the Google Maps API returned no address then then data variable will be empty
		print(formatted_address)
	except Exception as err:
		print("Not Found") 

#Dry running the program
address = input("Enter Place whose address you want to find: ") 
getAddress()
