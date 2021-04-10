import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("WELCOME to Hope alive! How may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")     

    except Exception as e:
        # print(e)    
        print("Didn't catch that, please run the command again!\n")
        print("Sorry for the inconvenience")  
        speak("Didn't catch that, please run the command again! Sorry for the inconvenience")
        return "None"
    return query

def song():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:   
        query1 = r.recognize_google(audio, language='en-in')
        webbrowser.open(f"https://gaana.com/song/{query1}")
    except Exception as e:
        # print(e)    
        print("Didn't catch that, please run the command again!\n")
        print("Sorry for the inconvenience")  
        speak("Didn't catch that, please run the command again! Sorry for the inconvenience")
        return "None"
    return query1

def games():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:   
        query2 = r.recognize_google(audio, language='en-in')
        webbrowser.open(f"http://oceanofgames.com/?s={query2}")
    except Exception as e:
        # print(e)    
        print("Didn't catch that, please run the command again!\n")
        print("Sorry for the inconvenience")  
        speak("Didn't catch that, please run the command again! Sorry for the inconvenience")
        return "None"
    return query2


if __name__ == "__main__":
    wish()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'games' in query:
            print("Say the name of the game you wanna install")
            speak("Say the name of the game you wanna install")
            games()

        elif 'covid cases updates' in query:
            webbrowser.open("https://www.statista.com/topics/6135/coronavirus-covid-19-outbreak-in-india/#:~:text=India%20witnessed%20an%20outbreak%20of,19%2C%20confirming%20a%20local%20contagion.")   


        elif 'music' in query:
            print("Say the name of the song..")
            speak("Say the name of the song")
            song()
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        break
               
