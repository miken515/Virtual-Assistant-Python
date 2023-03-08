import os # This is where we can have the assistant open up applications
from datetime import datetime
'''
Below is the creation to have timmy open certain applications on the desktop

A dictionary to open applications
This will only work for mac users simply because the file path is different from windows

'''

paths = {
    'discord': "open /Applications/Discord.app",
    'league of legends': "open /Applications/League\ of\ Legends.app",
    'google chrome': "open /Applications/Google\ Chrome.app",
    'spotify': "open /Applications/Spotify.app",

    # Needs /System front of "/Applications" because its a stock apple program
    'camera' : "open /System/Applications/Photo\ Booth.app",
    'notes' : "open /System/Applications/Notes.app",
    'calculator' : "open /System/Applications/Calculator.app",
}

# Functions for certain applications when asked to Timmy

def openDiscord():
    os.system(paths['discord'])

def openLoL():
    os.system(paths['league of legends'])

def openChrome():
    os.system(paths['google chrome'])

def openSpotify():
    os.system(paths['spotify'])

def openCamera():
    os.system(paths['camera'])

def openNotes():
    os.system(paths['notes'])

def openCalc():
    os.system(paths['calculator'])

def getTime():
    months = {1: "Januaury", 2: "Feburary", 3: "March",
              4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September",
              10: "Octover", 11: "November", 12: "December"}
    curr = datetime.now()

    return "Today is {} {}, {} and the time is {} {}.".format(months[curr.month],
                                                              curr.day, curr.year, curr.hour, curr.minute)




