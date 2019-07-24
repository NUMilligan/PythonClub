import re
import win32com.client

howmany = 99
unit = "carboy"
substance = "muriatic acid"
location = "rack"
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def pluralize (word:str, quantity:int=2) -> str:
    """ Create correct English-language plurals """
    if quantity == 1:
        retval=word
    else:
        if re.match(r'\w+[^aeiou]y$',word):
            retval=word[:-1] + "ies"
        elif re.match(r'\w+[^aeiou]o$',word):
            retval=word[:-1] + "oes"
        else:
            retval=word + "s"

    return retval


def speechify (*words) -> str:
    """ Add spaces and stringify any integers so they won't break text-to-speech """
    retval = ""
    for word in words:
        retval += str(word) + " "

    return retval


def display_and_speak (words:str):
    """ Display and speak a string """
    print (words)
    speaker.Speak (words)

display_and_speak(speechify ("The",pluralize(unit),"of",substance,"Song"))
print()

for unit_num in range(howmany,0,-1):
        display_and_speak(speechify(unit_num,pluralize(unit,unit_num),"of",substance,"on the",location))
        display_and_speak(speechify(unit_num,pluralize(unit,unit_num),"of",substance))

        if unit_num == 1:
            display_and_speak(speechify("If that",unit,"should happen to fall"))
            display_and_speak(speechify("There'll be no more",pluralize(unit),"of",substance,"on the",location))
        else:
            display_and_speak(speechify ("If one of those",pluralize(unit,unit_num),"should happen to fall"))
            display_and_speak(speechify ("That's",unit_num-1,pluralize(unit,unit_num-1),"of",substance,"on the",location))
        
        print()

print("The end")
print()