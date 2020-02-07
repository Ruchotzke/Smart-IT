import speech_recognition as sr
from gtts import gTTS
import os
import pyaudio
import playsound


num = 0

def assistantSpeaks(text):
	global num

	num += 1
	print("Assistant: " + text)

	toSpeak = gTTS(text = text, lang = 'en', slow=False)
	file = str(num) + ".mp3"
	toSpeak.save(file)

	os.system("omxplayer -o local " + file)



assistantSpeaks("Hello There")
