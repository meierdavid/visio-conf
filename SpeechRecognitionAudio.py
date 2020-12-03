import speech_recognition as sr
import sys

r = sr.Recognizer()
for x in range (1, len(sys.argv)):
	with sr.AudioFile(str(sys.argv[x])) as source:
	    audio = r.listen(source)
	    try:
	        text = r.recognize_google(audio, language = "fr-FR")
	        print("You said : {}".format(text))
	        text_file = open("sample.txt", "a")
	        text_file.write(str(format(text))+"\n")
	        text_file.close()
	    except:
	        print("Sorry could not recognize what you said")
	        text_file = open("sample.txt", "a")
	        text_file.write("Sorry could not recognize what you said \n")
	        text_file.close()