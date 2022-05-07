import sys
import time
from bs4 import BeautifulSoup
import self
import math
import instaloader
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
import wikipedia
from requests import get
import webbrowser
import pywhatkit as kit
import smtplib
import pyjokes
import pyautogui
import datetime
from playsound import playsound
import psutil
import speedtest
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)
'''voices[0].id gives the voice of TTS_MS_EN-US_DAVID_11.0 
if voices[1] is there then it will gives the voice of TTS_MS_EN-US_ZIRA_11.0 '''


# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Eric. Please tell me how can I help you")

#SEND MESSAGES ON WHATSAPP 
def whatsapp_msg():
    speak("To whom you want to send the message?")
    name = takecommand()
    number = whatsapp_contact[name]
    speak(f"what message you want to send to {name} ")
    content = takecommand()
    speak("set the time ,in what time you want to send the message. set the time in 24 hour format")

    kit.sendwhatmsg(f"+91{number}", f"{content}", int(input()), int(input()))
    # kit.sendwhatmsg("+917781041625", "Hi this message is sent by a desktop assistant", 13,30,00)
    speak("Your message is sent")




whatsapp_contact = {
    'Sonal': '7781041625',
    'Tejaswini': '9307405066',
    'Anvi': '9822695617',
    'Janvi': '9146226162'
}

#Fetch NEWS ----------- WORKING
def news():
    # take a news from newsapi.org
    main_url = 'http://newsApi.org/v2/top-headlines?sources=techcrunch&apiKey=e455b81623214aeabb34eeac5e8c489d'
    # print(main_page)
    main_page = requests.get(main_url).json()
    # store articles in variable
    article = main_page["articles"]

    # empty list
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")




if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
# Logic building for tasks
        #OPEN NOTEPAD WORKS
        if "open notepad" in query:
            npath = "C:\\windows\\system32\\notepad.exe"
           
            os.startfile(npath)

# To close notepad
        elif "Close notepad" in query:
            speak("Closing Notepad.")
            os.sys("taskkill /f /im notepad.exe")

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)

# Open different editors by os module ---- ***
        elif "open Editor" in query:
            speak("Which editor you want to open ?")
            editor = takecommand().lower()
            if "vs code" in editor:
                path = "C:\Program Files\Microsoft VS Code\Code.exe"
                os.startfile(path)
            elif "pycharm" in editor:
                path = "C:\Program Files\JetBrains\PyCharm Community Edition 2022.1\bin\pycharm64.exe"
                os.startfile(path)
        elif "open command prompt" in query:
            # open command prompt by os module
            os.system("start cmd")

        elif "open skype" in query:
            path = "C:\Program Files\Microsoft Office\root\Office16\SkypeSrv\SKYPESERVER.EXE"
            os.startfile(path)

# To open camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

# To find ip address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

# To search Wikipedia
        elif "wikipedia" in query:
            

            speak("Searching Wikipedia")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)


#OPEN DIFFERENT SITES 

# Social browsing
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            
        elif "open twitter" in query:
            webbrowser.open("www.twitter.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
        elif "search on google" in query:
            speak("What should i search on google")
            search = takecommand().lower()
            webbrowser.open(f"{search}")

#Sending msg on different social media platform
        elif "send message" in query:
            whatsapp_msg()

        elif "who am I" in query:
            speak("If you talk then definitely you are a human.")



# Play music on youtube
        elif "play music on youtube" in query:
            speak("which song you want to listen on youtube")
            song_name = takecommand().lower()
            kit.playonyt(f"{song_name}")

# To close any application *****
        elif "close notepad" in query:
            
            speak("okay, closing notepad")
            os.system("taskkill /f /im notepad.exe")



           
           

# To shut down the system
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        


# To restart the system -- works
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

# To sleep the system
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dil,SetSuspendState 0,1,0")

# Switch the tab or window
        elif "Switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

# Tell the news - first fetch the online data then convert it in list then by for loop it iterate then gives the
# headlines
        elif "tell the news" in query:
            speak("please wait, fetching the latest news")
            news()

# Location ------- ****
        elif "Where am I ?" in query or "Where are we ?" in query:
            speak("wait, let me check")
            try:
                ip_add = requests.get('https://api.ipify.org').text
                print(ip_add)

                url = 'https://get.geojs.io/v1/ip/geo' + ip_add + '.json'
                geo_requests = requests.get(url)
                # Scrap the data in json and in json it is in form of dict.
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state]
                country = geo_data['country']
                speak(f"I think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry , Due to network problem I am not able to find where we are")
                My_location()
                


 # To download instagram profile photo
        elif "instagram profile" in query or "insta profile" in query:
            speak("Please enter the username correctly")
            name = input("Enter the name: ")
            webbrowser.open(f"www.instagram.com/{name}")
            time.sleep(5)
            speak("Would you like to download the profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("Task is done, profile picture is saved in our main folder")
            else:
                pass

# # To take a screenshot
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("Please hold the screen for few seconds , I am taking the screenshot")
            img = pyautogui.screenshot(f"{name}.png")
            speak("Task is done, the screenshot is saved in our main folder")

# # To stop JARVIS
        elif "You can sleep now" in query:
            speak("Thank you for using me. Have a good day.")
            sys.exit()
            


        elif 'volum up' in query:
            pyautogui.press("volumeup")
             
        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")
        

        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"our system has{percentage}percent battery " )

    
        elif 'temperature' in query:
            search = "temperature in Nagpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            teep = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {teep}")

        elif "internet speed" in query:

            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"we have{dl} mb per second downloading speedand {up} mb  per second uploading speed")


        elif "read pdf" in query:
            pdf_reader()

    
        def pdf_reader():
             book = open('Greedy Algorithm.pdf','rb')
             pdfReader  = PyPDF2.PdffileReader(book)
             pages = pdfReader.numPages
             speak(f"Total number of pages in this PDF is{pages} ")
             speak("please enter the page number I have to Read")
             pg = int(input("please enter the page number: "))
             page = pdfReader.getPage(pg)
             text = page.extractText()
             speak(text)

        
            