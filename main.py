import pyttsx3
import PyPDF2
import tkinter
from tkinter.filedialog import *


book =  askopenfile(mode='rb')
pdfreader =PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for num in range ( 0, pages) :
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
    rate = player.getProperty('rate')
    print(rate)
    player.setProperty('rate', 125)


