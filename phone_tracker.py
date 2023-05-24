#                                      TRACKING THE MOBILE LOACTION

#Before write code install all the bellow :
#1.pip install phonenumbers.
#2.pip install folium.
#3.pip install opencage.
# if you want key the follow the steps:
#1. go to google.
#2. then search the opencage.
#3. the register it and scroll_down the you find the API Keys the copy that the past in the key variable.  
import phonenumbers
from phonenumbers import geocoder
import folium
key = "94e205bba0a543258323ec53bc1145a9"
# from test import number
number = input("Enter phone_number with contry code: ")


check_number = phonenumbers.parse(number)
number_locatio = geocoder.description_for_number(check_number,"en")
print(number_locatio)  #Upto this if you type the it give only the which contry not proper location

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en")) #upto this it will give the country and service provider

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(number_locatio)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']  #it is lattitude
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_locatio).add_to(map_location)
map_location.save('mylocation.html') #if you want to save the file in the html format the directly access it.