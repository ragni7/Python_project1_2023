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
		pywhatkit.sendwhatmsg("Phone number","Hey, I'm from python",18,18)
		print("done!")
	
	elif Choice== "Gmail":
		Gmailconn = smtplib.SMTP('smtp.gmail.com', 587)
		Gmailconn.starttls()
		Gmailconn.login("email id", "password")
		Email_msg = """Hey. I hope you're well! 
		This is an email from python project"""
		Gmailconn.sendmail("sender's email id", "receiver's email id", Email_msg)

	elif Choice == "SMS":
	
		from twilio.rest import Client 
		# Your Account Sid and Auth Token from twilio.com / console 
		SMS_sid = 'Key'
		SMS_auth_token = 'auth key'

		client = Client(SMS_sid, SMS_auth_token) 

		SMS_message = client.messages.create( 
							from_='Phone number', 
							body ='Hey SMS, This is from python project', 
							to ='Phone number'
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
		song = multiprocessing.Process(target=playsound, args=(r'Path',))
		song.start()
		input("press ENTER to stop playback")
		song.terminate()

	elif Choice == "Wikipedia":
		data = wikipedia.summary("Ikea india")
	print(data)
