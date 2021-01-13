import pyttsx3
import PyPDF2
Path=open('D:\Python\Automate Text Message\AudioBook\FL.pdf','rb')
ReadPDF=PyPDF2.PdfFileReader(Path)
page=ReadPDF.numPages
print(page)
Reader=pyttsx3.init()
ReadFrom=ReadPDF.getPage(13)
Text=ReadFrom.extractText()
Reader.say(Text)
Reader.runAndWait()