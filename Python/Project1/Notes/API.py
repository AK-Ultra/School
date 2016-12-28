import requests
import json
from geopy.geocoders import GoogleV3

from geopy.distance import vincenty

def accessMicroveggies():
	res = requests.get('http://www.microveggies.com/data/get/temperature')
	'''
	You can access the data returned using res.text, which gives you a string.
	But, it's difficult to do anything with a string. We really need the 
	data in atomic units that we can use.

	There is a format called json that we can use to make the data more
	manageable.
	'''
	print res.text
	jsonData = res.json() 
	'''
	jsonData is a list of dictionaries. Now that we have a list, we can 
	index individual elements in the list, and since we have a dictionary,
	we can get the keys and the values in the dictionary. Lists and dictionaries
	are much easier to work with in this case than strings.
	'''

	print type(jsonData)
	print res.text[0:10]

	for item, value in jsonData[0].items():
		print item, value

def accessGeopy():
	'''
	This lecture uses python 2.7.
	'''
	'''
	geopy is a python frontend to the several geocoding APIs, 
	such as Google Maps, Bing, Yahoo, and OpenStreetMap. We downloaded
	and installed geopy with sudo pip install geopy. If you want to see 
	what geopy is, we can look at the source code that is stored in 
	/usr/local/lib/python2.7/dist-packages. This is where package manager
	stores third-party python packages for python 2.7.

	You can navigate to the geopy/geocoders directory and see that there is
	a googlev3.py file. When we look at that file, the first thing to notice
	is class GoogleV3. Classes are how we define more complex objects, that
	include properties and methods that we design. There are several built in
	to python, such as the string class. There are properties of strings, 
	such as the length, and there are methods that can be done on the string, 
	such as sort and reverse. 

	In GoogleV3, a class is defined that encapsulates the functionality we
	need to use the Google API. What's nice about this approach is we don't
	have to look at the nasty guts of the API calls, we just need to learn
	the class methods and properties and call those.

	We'll talk about classes more in C++. For now, we're going to use them,
	but not necessarily define our own.

	We can see from looking at the googlev3.py file that the class is called
	GoogleV3, so to use that class, we import it. Now our program is aware
	of the class and all of the properties and methods associated with it.
	'''

	#from geopy.geocoders import GoogleV3
	'''
	Here, we're importing the distance functionality from the distance.py
	file.
	'''
	#from geopy.distance import vincenty

	'''
	the point functionality from point
	'''
	from geopy.point import Point

	'''
	We need to create a variable that is the type of the class. This is 
	called an instance of the class. Here, we create an instance called
	geolocator by calling the GoogleV3 constructor. The constructor creates
	an instance of the class.
	'''
	geolocator = GoogleV3()

	'''
	Call the geocode method, which is shown on line 125 of googlev3.py. You
	give it a place and it generates the API call and returns lots of data
	about that place.
	'''
	address, (latitude, longitude) = geolocator.geocode("Engineering Center, Boulder, CO")
	print "Address: ", address, " lat: ", latitude, " long: ", longitude

	'''We can verify the output by going to maps.google.com
	and typing in the lat, long and seeing what comes back

	The lat, long shown above are in decimal degrees. There's another
	numbering system that uses degrees, minutes, seconds when talking about
	coordinates. In geopy, you can create a point to get that information,
	should you need to. There could be other libraries, such as a front-end
	for the Google Earth API that expects the coordination in the D,M,S 
	format. To make the softwares play nice together, the coordinates need
	to be converted. 
	'''

	#You can convert to a string
	#or pass it a tuple

	strPlace = str(latitude) + ", " + str(longitude)

	p1 = Point((latitude,longitude))#strPlace)
	print "point", p1

	#this returns a whole bunch of stuff
	print address
	#this is just lat and long
	print latitude, longitude

	'''
	There's another method in the class called reverse, this can be used
	to identify a place, given a set of lat, long coordinates. For example,
	if we use the lat, long from Engineering Center, we should get it to 
	say that that is the location of the engineering center.
	'''

	strPlace = str(latitude) + ", " + str(longitude)
	#print strPlace
	#print type(loc.latitude)
	locTuple = (latitude, longitude)
	pl = geolocator.reverse(locTuple)
	'''
	pl is a big list of locations and I'm not sure why. We can get the first
	item in the list and then grab it's address, and we should see 
	Engineering Center information. Or, we could put in another lat,long 
	pair and see what we get.

	Who lives here? 38.897936, -77.036514
	'''
	print pl[0].address 
	'''
	Knowing the coordinates of a location is also useful for calculating
	distances between two locations. We can see this in google maps where
	you click on two points and say distance and it uses some formula to
	tell you how far apart those places are. 

	Included in geopy is a file called distance and we can look at that and
	see that there are a few ways of calculating the distance between points,
	these are approximations due to shape of earth. We first need to import it
	before we can use it.

	Find lat,long of Austin, TX. This is going to give us a location in the
	middle of the city. Using the same instance of GoogleV3, just giving it
	a different argument.
	'''
	addrAustin, (latAustin, longAustin) = geolocator.geocode("Austin, TX")

	distanceBetweenCities = vincenty((latitude,longitude), (latAustin,longAustin)).miles

	print distanceBetweenCities

	#do calculation with great_circle distance

	#exercise: which is closer to boulder: Austin, TX or Minneapolis, MN?

def main():
	accessMicroveggies()
	accessGeopy()
	
main()
