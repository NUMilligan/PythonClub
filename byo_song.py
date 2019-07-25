import win32com.client
from Song import Song

beer_song_params = { 'speaker': win32com.client.Dispatch("SAPI.SpVoice"),
    'howmany': 2,
    'unit': 'bottle',
    'substance': 'beer',
    'location': 'wall' }

#beer_song = Song(**beer_song_params)
#beer_song.sing()

#acid_song = Song(speaker = win32com.client.Dispatch("SAPI.SpVoice"),howmany = 2,unit = "carboy",substance = "muriatic acid",location = "rack")
#acid_song.say()

# Provide a list of ways to output the song
sound_output = win32com.client.Dispatch("SAPI.SpVoice")
oil_song = Song(speaker = sound_output,howmany = 1,unit = "can",substance = "oil",location = "shelf")
oil_song.perform(print,sound_output.Speak)