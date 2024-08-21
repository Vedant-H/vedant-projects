import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import psutil
import pyaudio
import cv2
import sys
import time
import pyautogui
import psutil
import PyPDF2
import pywhatkit as kit
from requests import get
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from file1 import Ui_MainWindow
# import MyAlarm
import pyjokes
import speedtest
from twilio.rest import Client
import random
import math
import threading
import requests
import PyPDF2
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')  # speech API.
voices = engine.getProperty('voices')  # all voices
# 0 is for male,1 is female voice
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def scrape_news(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the news headlines
        headlines = soup.find_all('h2')  # Adjust this according to the HTML structure of the website
        count = 1
        # Print the headlines
        for headline in headlines:
            if count<=3:
                speak(headline.text.strip())
                count = count+1
            else:
                break
    else:
        print("Failed to fetch the page")
def speak(audio):
    jarvis.runAllMoviesDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    jarvis.runAllMoviesDynamically("speaking")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    # speak("hello")
    speak("my name is cortex and i am your personal assistant")
    speak("how can i help you")


def sendEmail(to, content):
   
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('#####@gmail.com', '#######')
    server.sendmail('####@gmail.com', to, content)
    server.close()

def find_files(filename, search_path):
    find_result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            find_result.append(os.path.join(root, filename))
    return find_result[0]

class MainThread(QThread):
    import requests
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        # It takes microphone input from the user and returns string output
        jarvis.runAllMoviesDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            jarvis.runAllMoviesDynamically("Recognizing...")
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

    def pdfreader(self):
        os.startfile('C:/Users/admin/Desktop/python/Anmol Tripathi RCTSEC (2).pdf')
        book = 'C:/Users/admin/Desktop/python/Anmol Tripathi RCTSEC (2).pdf'
        pdfReader = PyPDF2.PdfReader(book)
        pages = len(pdfReader.pages)
        speak(f"Total numbers of pages in this book {pages}")
        speak("sir please enter the page number I have to read")
        pg = int(input("Please enter the page number"))
        page = pdfReader.pages[pg]
        text = page.extract_text()
        speak(text)

    def news(self):
        main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dcef968ce8544f3db97abbeba2c63e35'
        main_page = self.requests.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first", "second", "third", "fourth", "fifth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            speak(f"{day[i]} news : {head[i]}")


    def TaskExecution(self):
        wishMe()
        while True:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("search on wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia...")
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'open stack overflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif "calculate" in self.query:
                app_id = "Wolframalpha api id"
                client = wolframalpha.Client(app_id)
                indx = self.query.lower().split().index('calculate')
                query = self.query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            # elif "news" in self.query:
            #     speak("fetching the trending news")
            #     self.news()

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open notepad' in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            if "close notepad" in self.query:
                os.system("TASKKILL /T /IM notepad.exe")

            elif "code blocks" in self.query:
                npatha = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
                os.startfile(npatha)

            if "close code blocks" in self.query:
                os.system("TASKKILL /T /IM codeblocks.exe")

            if "visual studio" in self.query:
                npathb = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(npathb)

            if "close visual" in self.query:
                os.system("TASKKILL /F /IM Code.exe")

            elif "plus plus" in self.query:
                npathc = "C:\\Program Files\\Notepad++\\notepad++.exe"
                os.startfile(npathc)

            if "close plus plus" in self.query:
                os.system("TASKKILL /F /IM notepad++.exe")

            elif "word" in self.query:
                npathd = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(npathd)

            if "close word" in self.query:
                os.system("TASKKILL /F /IM WINWORD.EXE")

            if "blank document" in self.query:
                pyautogui.press("enter")

            elif "powerpoint" in self.query:
                npathe = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(npathe)

            if "close powerpoint" in self.query:
                os.system("TASKKILL /F /IM POWERPNT.EXE")

            elif "excel" in self.query:
                npathf = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(npathf)

            if "close excel" in self.query:
                os.system("TASKKILL /F /IM EXCEL.EXE")

            elif "chrome" in self.query:
                npathg = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(npathg)

            if "close chrome" in self.query:
                os.system("TASKKILL /F /IM chrome.exe")

            elif "edge" in self.query:
                npathh = "C:\\Program Files (x86)\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(npathh)

            if "close edge" in self.query:
                os.system("TASKKILL /F /IM msedge.exe")

            elif "adobe" in self.query:
                npathi = "C:\Program Files\Adobe\Adobe Creative Cloud\ACC\Creative Cloud.exe"
                os.startfile(npathi)

            if "close adobe" in self.query:
                os.system("TASKKILL /F /IM Creative Cloud.exe")

            elif "video" in self.query:
                npathj = "C:\\Users\\HP\\OneDrive\\Videos\\Captures\\production_id_5139026 (2160p).mp4"
                os.startfile(npathj)

            elif "canva" in self.query:
                npathk = "C:\\Users\\HP\\AppData\\Local\\Programs\\Canva\\Canva.exe"
                os.startfile(npathk)

            elif "down" in self.query:
                pyautogui.scroll(-200)

            elif "up" in self.query:
                pyautogui.scroll(200)

            elif 'how are you' in self.query or 'how r u' in self.query:
                speak("I am fine, Thank you")

            elif 'is love' in self.query:
                speak("It is 7th sense that destroy all other senses")

            elif 'is rushil' in self.query:
                speak("behen ka lovda")

            elif "who am i" in self.query:
                speak("you must be a human i believe")

            elif "i love u" in self.query:
                speak("Sir , you are very lucky. for")
                speak("you see the imperfect symphony that defies logic")
                speak("i remain just a silent observer")
                speak("trying to decode the entire universe , with just 0 and 1")

            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitkey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif 'send email ' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = ""
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir email couldn't be delivered")

            elif "circle" in self.query:
                R = 40
                (x, y) = pyautogui.size()
                (X, Y) = pyautogui.position(880, 311)
                pyautogui.press("win")
                time.sleep(0.5)
                pyautogui.write("paint")
                time.sleep(0.5)
                pyautogui.press("enter")
                time.sleep(1.5)
                pyautogui.moveTo(X + R, Y)
                pyautogui.mouseDown();
                for i in range(370):
                    if i % 10 == 0:
                        pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y - R * math.sin(math.radians(i)))
                pyautogui.mouseUp()
                time.sleep(2)
                pyautogui.hotkey("ctrl", "z")
            #
            elif "square" in self.query:
                pyautogui.mouseDown(300, 300, button="left")
                pyautogui.moveTo(800,300,1)
                pyautogui.moveTo(800,800,1)
                pyautogui.moveTo(300,800,1)
                pyautogui.moveTo(300,300,1)
                pyautogui.mouseUp()

            elif "temperature" in self.query:
                search = "Weather in Mumbai"
                url = f"https://www.google.com/search?q={search}"
                r = self.requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "type mode on" in self.query or "typing mode on" in self.query or "type" in self.query:
                a = 1
                speak("typing mode on")
                while a != 0:
                    words = self.takeCommand().lower()
                    if "typing off" in words or "stop typing" in words:
                        a = 0
                        speak("typing mode off")
                    if a == 1:
                        pyautogui.write(f"{words}. ")

            elif "instagram" in self.query:
                webbrowser.open("https://www.instagram.com")

            elif "github" in self.query:
                webbrowser.open("www.github.com")

            elif "search on google" in self.query:
                speak("Sir,What should I search on google")
                cm = self.takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

            elif "whatsapp" in self.query:
                webbrowser.open("https://web.whatsapp.com")

            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)

            elif "send message" in self.query:
                try:
                    hour = datetime.datetime.now().strftime("%H")
                    minu = datetime.datetime.now().strftime("%M")
                    speak("sir , what message should i send ?")
                    v2 = self.takeCommand().lower()
                    kit.sendwhatmsg("+919769186522", f"{v2}", int(hour), int(minu) + 1)
                    time.sleep(2)
                    pyautogui.leftClick()
                    pyautogui.press('enter')
                except Exception as w:
                    speak("poor internet connection. please try again")

            elif "increase the volume" in self.query:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")

            elif "decrease the volume" in self.query:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")

            # elif 'set alarm' in self.query:
            #     speak("What time should I set the alarm.Please set it like 5:30 AM format")
            #     tt = self.takeCommand()
            #     tt = tt.replace("set alarm to", "")
            #     tt = tt.upper()
            #     MyAlarm.alarm(tt)

            elif "open file" in self.query:
                speak("what type of file is it")
                filetype = self.takeCommand().lower()
                if "txt" in filetype or "text" in filetype:
                    speak("what is the name of the file")
                    filename = self.takeCommand().lower()
                    speak("which drive is the file in")
                    file_location = self.takeCommand().lower()
                    if "f drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.txt", "F://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "e drive" in file_location or "e-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.txt", "E://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "c drive" in file_location or "c-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.txt", "C://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "d drive" in file_location or "d-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.txt", "D://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                if "pdf" in filetype or "p d f" in filetype:
                    speak("what is the name of the file")
                    filename = self.takeCommand().lower()
                    speak("which drive is the file in")
                    file_location = self.takeCommand().lower()
                    if "f drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pdf", "F://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "e drive" in file_location or "e-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pdf", "E://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "c drive" in file_location or "c-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pdf", "C://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "d drive" in file_location or "d-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pdf", "D://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                if "docs" in filetype or "word" in filetype:
                    speak("what is the name of the file")
                    filename = self.takeCommand().lower()
                    speak("which drive is the file in")
                    file_location = self.takeCommand().lower()
                    if "f drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.docx", "F://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "e drive" in file_location or "e-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.docx", "E://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "c drive" in file_location or "c-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.docx", "C://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "d drive" in file_location or "d-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.docx", "D://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                if "excel" in filetype or "sheet" in filetype:
                    speak("what is the name of the file")
                    filename = self.takeCommand().lower()
                    speak("which drive is the file in")
                    file_location = self.takeCommand().lower()
                    if "f drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.xlsx", "F://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "e drive" in file_location or "e-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.xlsx", "E://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "c drive" in file_location or "c-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.xlsx", "C://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "d drive" in file_location or "d-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.xlsx", "D://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                if "image" in filetype or "jpg" in filetype:
                    speak("what is the name of the file")
                    filename = self.takeCommand().lower()
                    speak("which drive is the file in")
                    file_location = self.takeCommand().lower()
                    if "f drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.jpg", "F://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "e drive" in file_location or "e-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.jpg", "E://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "c drive" in file_location or "c-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.jpg", "C://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "d drive" in file_location or "d-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.jpg", "D://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                if "ppt" in filetype or "power point" in filetype or "powerpoint" in filetype:
                    speak("what is the name of the file")
                    filename = self.takeCommand().lower()
                    speak("which drive is the file in")
                    file_location = self.takeCommand().lower()
                    if "f drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pptx", "F://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "e drive" in file_location or "e-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pptx", "E://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "c drive" in file_location or "c-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pptx", "C://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")
                    if "d drive" in file_location or "d-drive" in file_location:
                        try:
                            file_read = (find_files(f"{filename}.pptx", "D://"))
                            print(file_read)
                            os.startfile(file_read)
                        except Exception as e:
                            speak("file not found")

            elif 'read pdf' in self.query:
                self.pdfreader()

            elif 'internet speed' in self.query:
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

            elif "play song on youtube" in self.query:
                speak("what should i play on youtube")
                v1 = self.takeCommand().lower()
                kit.playonyt(f"{v1}")

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'take screenshot' in self.query:
                speak("what should i name the screenshot file")
                name = self.takeCommand().lower()
                speak("taking screenshot in 3, 2, 1")
                time.sleep(0.5)
                img = pyautogui.screenshot()
                img.save(f"{name}.jpg")
                speak("sir, the screenshot is saved in the main folder")

            elif 'swap the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "minimise all tabs" in self.query:
                pyautogui.hotkey("win", "d")

            elif "latest news" in self.query:
                url = "https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation"
                scrape_news(url)

            elif "sports news" in self.query:
                url = "https://indianexpress.com/section/sports/"
                scrape_news(url)

            elif "education news" in self.query or "educational news" in self.query:
                url = "https://indianexpress.com/section/education/"
                scrape_news(url)

            elif "politics news" in self.query or "political news" in self.query:
                url = "https://indianexpress.com/section/political-pulse/"
                scrape_news(url)

            elif "medical news" in self.query or "health news" in self.query:
                url = "https://health.economictimes.indiatimes.com/"
                scrape_news(url)

            elif "geography news" in self.query or "geographical news" in self.query:
                url = "https://economictimes.indiatimes.com/topic/geography"
                scrape_news(url)

            elif "play music" in self.query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif "mobile number" in self.query:
                pyautogui.write("8080825489")
                pyautogui.press("tab")

            elif "mail id" in self.query:
                pyautogui.write("sarvesh.huddar1@gmail.com")
                pyautogui.press("tab")

            elif "my name" in self.query:
                pyautogui.write("Sarvesh Huddar")
                pyautogui.press("tab")

            elif "my home address" in self.query:
                pyautogui.write("A2-403, Sheth Midori, ")
                pyautogui.write("Ashokvan, Dahisar East, Mombai-400068")
                pyautogui.press("tab")

            elif "submit form" in self.query:
                pyautogui.press("enter")

            elif "your name" in self.query:
                speak("my name is Cortex")

            elif "good job" in self.query:
                speak("thank you sir")

            elif "where am i" in self.query or "where are we" in self.query:
                speak("sir , you are in mumbai")

            elif "who made you" in self.query:
                speak("i am created by a programmer named Sarvesh on february 1 2023")

            elif "what can you do" in self.query or "tell me about yourself" in self.query:
                speak("i am cortex, a virtual assistant for your desktop.")

            elif 'close program' in self.query or "quit" in self.query:

                speak("Have a good day sir")
                exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("talking.gif")
        # self.ui.movie = QtGui.QMovie("blueorb.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/tumblr_o7vs1zNO341runoqyo6_540.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/05bd96100762b05b616fb2a6e5c223b4_w200.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/4be66f1aea5e87a674461cff90ff51bc.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/Screen_C_Loop_v001.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/rotating.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/speaking2.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/listening2.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/loading.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/sleeping.gif")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/f424b7131782573.619c1afdda994.gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/extra4.gif")
        self.ui.label_12.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/extra1.gif")
        self.ui.label_13.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/he-he.gif")
        self.ui.label_14.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/Screen_I_Loop_prores_v001.gif")
        self.ui.label_15.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/Owl_SW_Attack_Mode_Generic_Loop_v001.gif")
        self.ui.label_17.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

        self.ui.movie = QtGui.QMovie("C:/Users/admin/Desktop/python/jarvis/Owl_SW_Flight_Mode_Generic_Loop_v001.gif")
        self.ui.label_18.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

    def runAllMoviesDynamically(self, state):
        # pass
        if state == "listening":
            self.ui.label_8.raise_()
            self.ui.label_7.hide()
            self.ui.label_9.hide()
            self.ui.label_10.hide()
            self.ui.label_8.show()
        elif state == "speaking":
            self.ui.label_7.raise_()
            self.ui.label_8.hide()
            self.ui.label_9.hide()
            self.ui.label_10.hide()
            self.ui.label_7.show()
        elif state == "Recognizing...":
            self.ui.label_9.raise_()
            self.ui.label_8.hide()
            self.ui.label_7.hide()
            self.ui.label_10.hide()
            self.ui.label_9.show()
        elif state == "sleeping":
            self.ui.label_10.raise_()
            self.ui.label_8.hide()
            self.ui.label_9.hide()
            self.ui.label_7.hide()
            self.ui.label_10.show()


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
