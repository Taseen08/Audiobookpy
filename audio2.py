import pyttsx3
speaker = pyttsx3.init()
text = "I dont want to study"
speaker.say(text)
speaker.runAndWait()