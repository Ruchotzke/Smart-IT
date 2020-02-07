#Filename:	VoiceAssistantAPI.py
#Author:	Ethan Ruchotzke, 2020
#Organization:	IT-Adventures, Smart IT 2020
#Purpose:	Create a high level API for students to use in creating their voice assistant.

#Import relevant modules
import speech_recognition as sr
from gtts import gTTS
import os
import pyaudio
import playsound

#Module Variables
timeout = 1		#Timeout is the amount of silence before a listener stops listening.
num = 0			#Temporary name for TTS filenames

#setTimeout()
#		Sets the amount of time before a timeout to a positive
#		amount of seconds.
# amt:		The new value. Must be greater than zero.
# return:	Nothing.
def setTimeout(amt):
	if(amt <= 0):
		print("Timeout must be greater than zero. Not setting.")
	else:
		timeout = amt

#textToSpeech(text, writeToConsole)
#		Speaks the provided text out loud.
#		Relies on gTTS and OS commands.
# text:		The text to be spoken out loud.
# write:	A bool, true when the console should write the text as well.
# return:	Nothing.
def textToSpeech(text, write):
	global num

	num += 1
	if(write):
		print("Assistant: " + text)

	toSpeak = gTTS(text=text, lang='en', slow=False)
	file = str(num) + ".mp3"
	toSpeak.save(file)

	playsound.playsound(file, True)
	os.remove(file)

#getSpeech()
#		Listens using the mic, and turns speech
#		into text (a string).
# return:	A string representing the spoken text.
def getSpeech(index):
	global timeout

	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone(device_index=index) as source:
		print("Speak...")
		audio = rObject.listen(source, phrase_time_limit=timeout)
	print("Stop.")

	try:
		text = rObject.recognize_google(audio, language='en-US')
		print("User: " + text)
		return text

	except:
		textToSpeech("Could not understand your command. Please try again.", True)
		return ""
