import speech_recognition as sr
import pyttsx3 # Text to speech
from datetime import datetime # importing time for greeting

# Initializing some global vairables the will be used in functions
timmy = pyttsx3.init() # Initializing timmy, the voice assistant
timmy.setProperty('rate', 100) # setting rate of speech
user = 'Mike'
botName = 'Timmy'

# User is speaking into the microphone
def userInput():
    listening = sr.Recognizer() # Speech recognizer...
    with sr.Microphone() as source:
        print("I am listening...")
        listening.pause_threshold = 1
        mySpeech = listening.listen(source, 10, 6)
    try:
            print("Trying to recognize")
            instruction = listening.recognize_google(mySpeech, language='en-in') #Using google's speech recognition
            if 'exit' in instruction:
                timmyResponse('Goodbye!')
                exit()
    except Exception:
        timmy.say("Sorry I did not get that")
        instruction = "None"
    return instruction

# Getting response back from virtual assistant
def timmyResponse(txt):
    timmy.say(txt)
    timmy.runAndWait()

# Greeting the user based on time of day
def timmyGreeting():
    hr = datetime.now().hour
    if hr >= 6 and hr < 12:
        timmy.say(f"Good morning {user}")
        timmy.runAndWait()
    elif hr >= 12 and hr < 16:
        timmy.say(f"Good afternoon {user}")
        timmy.runAndWait()
    elif hr >=16 and hr < 19:
        timmy.say(f"Good evening {user}")
        timmy.runAndWait()
    timmy.say(f"I am {botName}, how may I assist you?")
    timmy.runAndWait()

