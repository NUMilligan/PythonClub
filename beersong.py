import re

unit = "carboy"
substance = "muriatic acid"
location = "rack"

def pluralize (word:str, quantity:int=2) -> str:
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

for unit_num in range(99,0,-1):
        print (unit_num,pluralize(unit,unit_num),"of",substance,"on the",location)
        print (unit_num,pluralize(unit,unit_num),"of",substance)
        
        if unit_num == 1:
            print ("If that",unit,"should happen to fall")
            print ("There'll be no more",pluralize(unit),"of",substance,"on the",location)
        else:
            print ("If one of those",pluralize(unit,unit_num),"should happen to fall")
            print ("That's",unit_num-1,pluralize(unit,unit_num-1),"of",substance,"on the",location)
        
        print()

print("The end")
print()