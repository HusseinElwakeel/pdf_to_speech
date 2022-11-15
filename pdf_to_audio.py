import pyttsx3
import PyPDF2

book = open("claude_gueux.pdf", 'rb')  # to open bpd and rb(read as binary book )
pdfReader= PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)

speaker = pyttsx3.init()    #initial library
for num in range(1, pages):
    page = pdfReader.getPage(num)
    print(page)
    text = page.extractText()
    speaker.say(text) # what i want  program to say
    speaker.runAndWait() # to run code