import pyttsx3
speaker = pyttsx3.init()
text = "Hi"
speaker.say(text)
speaker.runAndWait()