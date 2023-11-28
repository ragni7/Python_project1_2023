import pyttsx3
import os
import pywhatkit
import smtplib
import geopy
import twilio
import certifi
import ssl
import geopy.geocoders 
import playsound
import multiprocessing
import wikipedia

while True:

	pyttsx3.speak("Welcome to python care, you can choose any of them and it'll do the needful")

	Choice = input("Enter your choice:")

	if Choice == "Skype":  	
		os.system("Skype")

	elif Choice == "Notepad":
 		os.system("Notepad")
		 	 
	elif Choice == "Chrome":
 		os.system('chrome')
	
	elif Choice == "Whatsapp":
		os.system('chrome')
		pywhatkit.sendwhatmsg("+918320862751","Hey, I'm from python",18,18)
		print("done!")
	
	elif Choice== "Gmail":
		Gmailconn = smtplib.SMTP('smtp.gmail.com', 587)
		Gmailconn.starttls()
		Gmailconn.login("ragnisshukla@gmail.com", "hpyl mnpp eqlt rjdz")
		Email_msg = """Hey. I hope you're well! 
		This is an email from python project"""
		Gmailconn.sendmail("ragnisshukla@gmail.com", "shuklaragni99@gmail.com", Email_msg)

	elif Choice == "SMS":
	
		from twilio.rest import Client 
		# Your Account Sid and Auth Token from twilio.com / console 
		SMS_sid = 'AC04be8fba24e9c5592d18017299d00c3b'
		SMS_auth_token = 'bbbe6bfc70132bca052c62fbd8c39826'

		client = Client(SMS_sid, SMS_auth_token) 

		SMS_message = client.messages.create( 
							from_='+15104883899', 
							body ='Hey SMS, This is from python project', 
							to ='+918320862751'
						) 

		print(SMS_message.sid)

	elif Choice == "Geo":

		from geopy.geocoders import Nominatim

		ctx = ssl.create_default_context(cafile=certifi.where())
		geopy.geocoders.options.default_ssl_context = ctx

		location = Nominatim(scheme = 'https', user_agent="GetLoc")
		getLocation = location.geocode("Vallabh Vidyanagar, Anand")

		print(getLocation.address)

		print("Latitude = ", getLocation.latitude, "\n")
		print("Longitude = ", getLocation.longitude)

	elif Choice == "audio":
		#import the library
		from playsound import playsound
		song = multiprocessing.Process(target=playsound, args=(r'E:/Ragni Mobile/songs/AUD-20150717-WA0018.mp3',))
		song.start()
		input("press ENTER to stop playback")
		song.terminate()

	elif Choice == "Wikipedia":
		data = wikipedia.summary("Ikea india")
	print(data)