# A couple of text to speech libraries
import win32com.client
import pyttsx3
# The Song creator and handler
from Song import Song

# Pass a set of parameters to the constructor
beer_song_params = {
    'howmany': 2,
    'unit': 'bottle',
    'substance': 'beer',
    'location': 'wall' }

beer_song = Song(**beer_song_params)
# Just display it
beer_song.perform(print)

# Provide a list of ways to output the song
# Create an output destination for text to speech
pyttsx3_output = pyttsx3.init()
# Choose a different voice
voices = pyttsx3_output.getProperty('voices')
pyttsx3_output.setProperty('voice', voices[1].id)
lemonade_song = Song(howmany = 1,unit = "bottle",substance = "lemonade",location = "counter")
# Pass two output destinations, print and the sound output
lemonade_song.perform(print,pyttsx3_output.say)
# pyttsx3 engine requires runAndWait() and stop() before it will actually speak
pyttsx3_output.runAndWait()
pyttsx3_output.stop()

# Do it again with a different engine
win32com_output = win32com.client.Dispatch("SAPI.SpVoice")
oil_song = Song(howmany = 1,unit = "can",substance = "oil",location = "shelf")
oil_song.perform(print,win32com_output.Speak)
# win32com engine doesn't need to run/wait/stop
