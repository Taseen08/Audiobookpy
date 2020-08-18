import pyttsx3
import PyPDF2
book = open('ms-17.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7,10):
  page = pdfReader.getPage(num)
  text = page.extractText()
  speaker.say(text)
  speaker.runAndWait()

