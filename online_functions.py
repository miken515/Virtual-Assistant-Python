import wikipedia # importing information from wiki if we ask timmy a question
import pywhatkit as kt # This library enables us to do online functions such as youtube or google search
import requests # API requests for jokes


'''
These functions below will require an online connection and the tasks that timmy can do
'''

# User can get a wikipedia summary on any topic they choose
def wikiSearch(userInput):
    return wikipedia.summary(userInput, sentences=2)

# Play a youtube video by utilizing pywhatkit library...
def playVideo(video):
    kt.playonyt(video)

# Find anything that a user wants
def googleSearch(search):
    kt.search(search)

# Finding an api where we can generate random jokes
def jokes():
    joke = requests.get('https://geek-jokes.sameerkumar.website/api?format=json').json()
    return joke["joke"]
