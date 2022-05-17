import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import os
import cv2
import winsound

engine = pyttsx3.init()
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
try:
	import googlesearch
except ImportError:
    print("No module named 'google' found")

#searches in google for what the user asked for
def search(search_value, do_open=True):
    url = 'https://www.google.com/search?q=' + search_value
    if do_open is True:
        webbrowser.open(url)
    return url

# checks if the is an app by that name if no open it in google
def open(site_name):
    val = open_app(site_name,apps)
    if val != None:
        os.startfile(val)
    else:
        text2 = site_name.split("open")
        for j in googlesearch.search(text2, tld="co.in", num=1, stop=1):
            webbrowser.open(j)

def open_app(word,dict):
    for k in dict.keys():
        if k in word:
            return dict[k]
    return None


apps = {"word":"WINWORD.EXE","powerpoint":"POWERPNT.EXE","notepad":"notepad.exe","excel":"EXCEL.EXE","python":"python.exe","visual studio":"devenv.exe","steam":"C:\\Users\\gall_\\Desktop\\Steam\\steam.exe"}

#import subprocess
#cmd= '"C:\\Program Files\\Microsoft Office\\root\\\Office16\\POWERPNT.exe" %s'
#cmd = ""
#chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
#cmd = '"C:\\Program Files\\Microsoft Office\\root\\\Office16\\POWERPNT.exe"'
cmd = '"C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"'
cmd = '"C:\\Users\\gall_\\Desktop\\Steam\\steam.exe"'
cmd = '"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"'
#subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
#open("steam")
# the main function for listening to the user
def takeCommand():
    #recongizes your microphone
    r = sr.Recognizer()
    #using it
    with sr.Microphone() as source:
        #the AI speaks listening everytime the def is used
        speak("Listening...")
        #waits 1 second until there is silence
        r.pause_threshold = 1
        #get's the audio
        audio = r.listen(source)
        #tries to do it
    try:
        print("Recognizing...")
        #taking the audio and making it into a string and has the language set to english
        text = r.recognize_google(audio, language='en-in')
        #if error was raised because it couldn't idenify anything say he couldn't understand
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
    #returns the string
    return text
#like take_command but with no speaking or printing
def check_true():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)


    return text

#same as check_true and takecommand but returns the audio instead for recording audio files
def record():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        speak("recording...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    return audio
#for playing audio files
def play(text):
    #get's the name as text and adds ".wav" at the end to play it
    winsound.PlaySound(text + ".wav", winsound.SND_FILENAME)
    time.wait(1)
#same as check_true and takecommand but for naming files and the user
def name():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
    return text
def camera():
    #calls the fuction of the camera that opens
    cam = cv2.VideoCapture(0)
    #names the camera window "ugly"
    cv2.namedWindow("ugly")
