import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import os
import cv2
import winsound
import pyjokes
import datetime
import keyboard
from games import Games
import googlesearch

engine = pyttsx3.init()
class Ai_Listening:
    def takeCommand(self):
        # recongizes your microphone
        r = sr.Recognizer()
        # using it
        with sr.Microphone() as source:
            # the AI Audio.speaks listening everytime the def is used
            Audio.speak("Listening...")
            # waits 1 second until there is silence
            r.pause_threshold = 1
            # get's the audio
            audio = r.listen(source)
            # tries to do it
        try:
            print("Recognizing...")
            # taking the audio and making it into a string and has the language set to english
            text = r.recognize_google(audio, language='en-in')
            # if error was raised because it couldn't idenify anything say he couldn't understand
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
        # returns the string
        return text

    def check_true(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='en-in')

        except Exception as e:
            print(e)

        return text

    def record(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            Audio.speak("recording...")
            r.pause_threshold = 1.5
            audio = r.listen(source)

        return audio

    def name(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:

            Audio.speak("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='en-in')

        except Exception as e:
            print(e)
        return text
class Audio:
    
    def speak(audio):
        print(audio)
        engine.say(audio)
        engine.runAndWait()

    def do_record(self):
        # listens to you until it hears 1 second of silence
        recording = Ai_Listening.record()
        while True:
            try:
                # asks the name of the file to be
                Audio.speak("what name will you give it?")
                name_file = Ai_Listening.name()
                # wants to confirm if you want to name it as
                Audio.speak("are you sure you want to save it as '" + name_file + "'")
                print("Yes                          No")
                check = Ai_Listening.check_true().lower()
                if check.lower() == "yes":
                    # of yes opens/create a file as wav and writes the recording in it, if already there is a wav file called that it will overwrite it
                    with open(name_file + ".wav", "wb") as file:
                        file.write(recording.get_wav_data())
                    Audio.speak("saving...")
                    break
                elif check.lower() == "no":
                    # returns to the name selection
                    pass
                else:
                    Audio.speak("please choose one, yes or no")
            except:
                Audio.speak("sorry I couldn't understand")
        # closes the audio file
        file.close()

    def play_file(self):
        Audio.speak("which file should I play?")
        try:
            # get's the name of the file and plays it
            name_file = Ai_Listening.name()
            Audio.play(name_file)
        except:
            # if the files does not exist it will raise an error and go to the except and it will say it
            Audio.speak("sorry the file '" + name_file + "' does not exist")

    def play(text):
        # get's the name as text and adds ".wav" at the end to play it
        winsound.PlaySound(text + ".wav", winsound.SND_FILENAME)
        time.wait(1)
class Sites_and_Apps:
    def search(search_value, do_open=True):
        url = 'https://www.google.com/search?q=' + search_value
        if do_open is True:
            webbrowser.open(url)
        return url

    def open_site(site_name):
        val = Sites_and_Apps.open_app(site_name, apps)
        if val != None:
            os.startfile(val)
        else:
            text2 = site_name.split("open")
            for j in googlesearch.search(text2, tld="co.in", num=1, stop=1):
                webbrowser.open(j)

    def open_app(word, dict):
        for k in dict.keys():
            if k in word:
                return dict[k]
        return None

    def do_open(text):
        # get's the text for the website
        # opens the website
        Sites_and_Apps.open_site(text)
        # says he is opening that
        Audio.speak("opening" + text.replace("open", ""))

    def do_search(text):
        text2 = text.lower().replace("search", "").replace("luigi", "")
        Sites_and_Apps.search(text2)
        Audio.speak("searching" + text2)
class Extra:
    def camera(self):
        # calls the fuction of the camera that opens
        cam = cv2.VideoCapture(0)
        # names the camera window "ugly"
        cv2.namedWindow("ugly")

    def joke(self):
        # the language is english and it gives all jokes
        My_joke = pyjokes.get_joke(language="en", category="all")
        # Audio.speaks the joke
        Audio.speak(My_joke)

    def pause(check):
        Audio.speak("pausing...")
        # enters an always running while for it not to hear the user
        while True:
            try:
                # checks if you said "continue" if yes he will start the program again
                check = Ai_Listening.check_true().lower()
                if check.lower() == "continue":
                    Audio.speak("continuing...")
                    break
            except:
                pass
class Note:
    def do_note(self):
        file = open("note.txt", "a")
        while True:
            try:
                # the note get's name and listening for what the user said
                Audio.speak("What should I write?")
                note = Ai_Listening.name()
                Audio.speak("Should I include date and time?")
                # asks if you want to add date and time to the note
                print("yes                      no")
                break
            except:
                pass
        try:
            # checks if check is yes or no if it isn't it will return to the start of the while true
            check = Ai_Listening.check_true().lower()
            while True:
                if check == "yes":
                    # get's the datetime through the libary of date time
                    e = datetime.datetime.now()
                    # makes the date as day, month, year (you can also add minutes,hours and seconds)
                    date = e.strftime((e.strftime("%d/%m/%Y")))
                    # writes the date
                    file.write(date)
                    # adds a :- for better visual exprience
                    file.write(" :- ")
                    # writes the actual note and goes down a line
                    file.write(note + '\n')
                    Audio.speak("ok the note has been added")
                    # breaks into the main while true loop
                    break
                    # if note it will just write the note
                elif check == "no":
                    file.write(note + '\n')
                    Audio.speak("ok the note has been added")
                    break
                else:
                    Audio.speak("please choose one")
        except:
            Audio.speak("sorry I couldn't understand")
        # closes note
        file.close()
        # reads the note

    def read_note(self):
        # opens the note
        file = open("note.txt")
        # starts reading it
        Audio.speak(file.read())
        # closes note
        file.close()

    def write(text):
        # writes what ever the user said
        text2 = text.lower().replace("write", "")
        keyboard.write(text2)

    def delete_notes(self):
        # opens the note with r+ meaning overwrite
        file = open("note.txt", "r+")
        # ask you to confirm to delete them
        Audio.speak("are you sure you want to delete your notes?")
        print("yes                        no")
        while True:
            try:
                check = Ai_Listening.check_true().lower()
                if check == "yes":
                    # if yes it sets the notes to 0 value meaning nothing
                    Audio.speak("okay deleting your notes")
                    file.truncate(0)
                    break
                elif check == "no":
                    # if no it will just break out of the loop
                    break
                else:
                    # will return to the start of the while true
                    Audio.speak("please choose one")
            except:
                Audio.speak("sorry couldn't understand")
class User:
    def username(self):
        # opens the name and reads the name
        file = open("name.txt")
        username = file.read()
        if username == "":
            # if user did not have a previous name it will say it
            Audio.speak("you don't have a name. what should I call you?")
            while True:
                try:
                    # asks to what to call you and gets it
                    username = Ai_Listening.name()
                    Audio.speak("are you sure you want me to name you " + username)
                    print("yes                       no")
                    check = Ai_Listening.check_true().lower()
                    # confirms if you want to name your self as that
                    if "yes" == check:
                        # if yes it opens name text and starts to write
                        file = open("name.txt", "w")
                        file.write(username)
                        Audio.speak("okay your name is now " + username)
                        break
                    elif "no" == check:
                        # returns to the while true start
                        Audio.speak("okay what is your name then?")
                    else:
                        Audio.speak("please choose yes or no")
                except:
                    pass
        else:
            # if the user already has a name it will say it
            Audio.speak("your name is " + username)
        # closes file
        file.close()

    def change_name(self):
        # will change your name to your choosing
        file = open("name.txt", "r+")
        Audio.speak("ok what should I change it to?")
        while True:
            try:
                # asks to what to change and gets it
                username = Ai_Listening.name()
                Audio.speak("are you sure you want to change it to " + username)
                print("yes                      no")
                # asks you to confirm
                check = Ai_Listening.check_true().lower()
                if check == "yes":
                    # if it is yes it will delete the name and write it for what you said
                    file.truncate(0)
                    file.write(username)
                    break
                elif check == "no":
                    # if no it will return to the while true
                    Audio.speak("ok what should I change it to then?")
                else:
                    Audio.speak("please choose one yes or no")
            except:
                Audio.speak("sorry I don't understand")
        # says your name
        Audio.speak("ok your name is now " + username)
        # closes file
        file.close()
class Time:
    def time(self):
        # get's the time
        e = datetime.datetime.now()
        # Audio.speaks the time as hour, minute and seconds
        Audio.speak("the time is " + (e.strftime("%H:%M:%S")))

    def day(self):
        # get's the time and Audio.speaks it as the day(sunday,monday ect.), month, day (08 or 12 ect) and year
        e = datetime.datetime.now()
        Audio.speak("today is " + (e.strftime("%a, %b %d, %Y")))

apps = {"word":"WINWORD.EXE","powerpoint":"POWERPNT.EXE","notepad":"notepad.exe","excel":"EXCEL.EXE","python":"python.exe","visual studio":"devenv.exe","steam":"C:\\Users\\gall_\\Desktop\\Steam\\steam.exe"}

def games():
    # asks the user which game it wants to play
    Audio.speak("which game should we play?")
    print("tic tac toe       snake       ball(pong)")
    while True:
        try:
            # checks the game and says how to play them
            check = Ai_Listening.check_true().lower()
            if check == "snake":
                Audio.speak("the keys are the arrow keys")
                games.snake()
                break
            elif "tic-tac-toe" in check:
                games.tictactoe()
                break
            elif check == "ball":
                Audio.speak("the keys are w and s")
                games.pong()
                break
            elif check == "stop":
                break
            else:
                Audio.speak("please choose one")
        except:
            Audio.speak("sorry I don't understand")
            break
