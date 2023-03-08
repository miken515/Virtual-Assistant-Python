from timmy_functions import * # Importing all functions from timmy_functions.py file
from offline_functions import * # Importing all functions for offline use
from online_functions import * # Importing all functions for online use

timmyGreeting()
while True:
    myInput = userInput().lower()

    if 'open discord' in myInput:
        openDiscord()
    elif 'open league of legends' in myInput:
        openLoL()
    elif 'open chrome' in myInput:
        openChrome()
    elif 'open spotify' in myInput:
        openSpotify()
    elif 'open camera' in myInput:
        openCamera()
    elif 'open notes' in myInput:
        openNotes()
    elif 'open calculator' in myInput:
        openCalc()
    elif 'today\'s date' in myInput:
        timmyResponse("Sure!")
        timmyResponse(getTime())
    elif 'wikipedia' in myInput:
        timmyResponse("What would you like to search on wikipedia?")
        mySearch = userInput().lower()
        timmyResponse("Perfect. Working on it.")
        timmyResponse(wikiSearch(mySearch))
    elif 'youtube' in myInput:
        timmyResponse("Sure. What would you like to watch?")
        myVideo = userInput().lower()
        timmyResponse("Perfect. Working on it.")
        playVideo(myVideo)
    elif 'google' in myInput:
        timmyResponse("No problem. What would you like to search up?")
        googleSearch(userInput().lower())
    elif 'joke' in myInput or 'jokes' in myInput:
        timmyResponse(jokes())
    elif 'exit' in  myInput:
        exit()











