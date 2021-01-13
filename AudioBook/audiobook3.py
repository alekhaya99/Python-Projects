import pyttsx3
import PyPDF2
Path=open('D:\Python\Automate Text Message\AudioBook\FL.pdf','rb')
ReadPDF=PyPDF2.PdfFileReader(Path)
page=ReadPDF.numPages
print(page)
Reader=pyttsx3.init()
for i in range(page):
    ReadFrom=ReadPDF.getPage(i)
    Text=ReadFrom.extractText()
    Reader.say(Text)
    Reader.runAndWait()