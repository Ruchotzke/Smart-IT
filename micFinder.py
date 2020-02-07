import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
	print("Microphone: {1} with index {0} found.".format(index, name))
