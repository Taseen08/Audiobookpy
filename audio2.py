import pyttsx3
speaker = pyttsx3.init()
text = "Waterloo is gonna be fun yet challenging"
speaker.say(text)
speaker.runAndWait()