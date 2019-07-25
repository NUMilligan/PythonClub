from TextHandler import TextHandler

class Song:
    def  __init__ (self, howmany:int = 99, unit:str = "carboy",substance:str = "muriatic acid", location:str = "rack", speaker = None) -> None:
        self.howmany = howmany
        self.unit = unit
        self.substance = substance
        self.location = location
        self.speaker = speaker

    def display (self, text:str) -> None:
        print (text)

    def speak (self, text:str) -> None:
        if self.speaker != None:
            self.speaker.Speak (text)

    def display_and_speak (self, text:str) -> None:
        self.display(text)
        self.speak(text)

    def sing (self) -> None:
        th = TextHandler()

        self.display_and_speak(th.stringify ("The",th.pluralize(self.unit),"of",self.substance,"Song"))
        print()

        for unit_num in range(self.howmany,0,-1):
                self.display_and_speak(th.stringify (unit_num,th.pluralize(self.unit,unit_num),"of",self.substance,"on the",self.location))
                self.display_and_speak(th.stringify (unit_num,th.pluralize(self.unit,unit_num),"of",self.substance))

                if unit_num == 1:
                    self.display_and_speak(th.stringify("If that",self.unit,"should happen to fall"))
                    self.display_and_speak(th.stringify("There'll be no more",th.pluralize(self.unit),"of",self.substance,"on the",self.location))
                else:
                    self.display_and_speak(th.stringify ("If one of those",th.pluralize(self.unit,unit_num),"should happen to fall"))
                    self.display_and_speak(th.stringify ("That's",unit_num-1,th.pluralize(self.unit,unit_num-1),"of",self.substance,"on the",self.location))

                print()
        
        print("The end")
        print()
