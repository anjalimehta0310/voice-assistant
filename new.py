import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import playsound
import wikipedia
import operator
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pywhatkit as kit
#from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
#from Googlesearch import search
import urllib
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning!")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon!")

	else:
		speak("Good Evening!")

	    
	speak("I am jarvis,how can i help you")
	assname()
		#speak(assname)
	

def assname():
	speak("What should i call you")
	uname = takeCommand()
	speak("Welcome")
	speak(uname)
	#columns = shutil.get_terminal_size().columns
	
	print("#####################")
	print("Welcome", uname)
	print("#####################")
	
	speak("How can i Help you")

def takeCommand():

	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said:{query}\n")

	except Exception as e:
		#print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	email = input('enter your email')
	password = input('enter password')
	server.login(email,password)     
	server.sendmail('nupursharmau0310@gmail.com', to ,content)
	server.close()
    
if __name__ == '__main__':
	#clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	#clear()
	wishMe()
	#username()
	
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be
		# stored here in 'query' and will be
		# converted to lower case for easily
		# recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 2)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stack overflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query:
			speak("Here you go with music")
			music_dir = 'C:\\Users\\mayus\\Music'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir,songs[1]))
			
		
           
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")
			print(f"Sir, the time is {strTime}")

		elif 'open code' in query:
			codePath = "C:\\Users\\mayus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)

		elif 'email to Anjali' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "Receiver email address"
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("sorry by default,I am not able to send this email")

		elif 'send email' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input()
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			print("I am fine, Thank you")
			speak("How are you, Sir")
			

		elif 'fine' in query or "good" in query:
			speak("It's good to know that you are fine")
			print("It's good to know that you are fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak("Jarvis 1 point o")
			print("My friends call me Jarvis 1 point o")

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Anjali.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			print(pyjokes.get_joke())
			
		elif "do some calculation" in query:
			r = sr.Recognizer()
			my_mic_device = sr.Microphone(device_index=1)
			with sr.Microphone() as source:
				speak("Say what you want to calculate,ex: 3 plus 3") 
				print("listening.....")
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
			my_string = r.recognize_google(audio)
			print(my_string)
			def get_operator_fn(op):
				return{
					'+':operator.add,
					'-':operator.sub,
					'*':operator.mul,
					'/':operator.__truediv__,
					}[op]
			def eval_binary_expr(op1,oper,op2):
				op1,op2 = int(op1),int(op2)
				return get_operator_fn(oper)(op1,op2)
			speak("your result is")
			print("your result is")
			print(eval_binary_expr(*(my_string.split())))			

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("Thanks to Anjali. further It's a secret")

		elif 'open powerpoint presentation' in query:
			speak("opening Power Point presentation")
			power = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
			os.startfile(power)

		elif 'what is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Gaurav")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Miss Anjali ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
			speak("Background changed successfully")

		elif 'open bluestack' in query:
			appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
			os.startfile(appli)
				

		elif 'news' in query:
			url = 'https://www.bbc.com/news'
			response = requests.get(url)
			soup = BeautifulSoup(response.text, 'html.parser')
			headlines = soup.find('body').find_all('h3')
			unwanted = ['BBC World News TV', 'BBC World Service Radio','News daily newsletter', 'Mobile app', 'Get in touch']
			for x in list(dict.fromkeys(headlines)):
				if x.text.strip() not in unwanted:
					print(x.text.strip())
					speak(x.text.strip())

		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif "update assistant" in query:
			speak("After downloading file please replace this file with the downloaded one")
			url = '# url after uploading file'
			r = requests.get(url, stream = True)
			
			with open("Voice.py", "wb") as Pypdf:
				
				total_length = int(r.headers.get('content-length'))
				
				for ch in progress.bar(r.iter_content(chunk_size = 2391975),
									expected_size =(total_length / 1024) + 1):
					if ch:
					    Pypdf.write(ch)

		elif "temperature" in query:
			
			# Google Open weather website
			# to get API of Open weather
			search = "temperature in delhi"
			url = f"http://www.google.com/search?q={search}"
			r = requests.get(url)
			data = BeautifulSoup(r.text,"html.parser")
			temp = data.find("div",class_="BNeawe").text
			speak(f"current{search} is {temp}")
			print(f"current{search} is {temp}")

		elif "send a message " in query:
			kit.sendwhatmsg("+918318250670","this is testing protocol",23,36)

		elif "wikipedia" in query:
			speak("searching wikipedia...")
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query , sentences = 2)
			speak("accprding to wikipedia...")
			speak(results)
			print(results)


		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

	#agpovvqhkjesocli

            

