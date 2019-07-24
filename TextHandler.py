import re

class TextHandler:
    def stringify (self,*words) -> str:
        """ Add spaces and stringify any integers so they won't break text-to-speech """
        retval = ""
        for word in words:
            retval += str(word) + " "

        return retval

    def pluralize (self, word:str, quantity:int=2) -> str:
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
        