from TextHandler import TextHandler

class Stanza: 
    def __init__ (self) -> None:
        self.lines = []

    def add (self, line:str) -> None:
        self.lines.append(line)

class Song:
    def  __init__ (self, howmany:int = 99, unit:str = "carboy",substance:str = "muriatic acid", location:str = "rack") -> None:
        self.howmany = howmany
        self.unit = unit
        self.substance = substance
        self.location = location
        self.stanzas = []
        self.title = ""

        self.compose()

    def perform (self, *args) -> None:
        for func in args:
            func(self.title)
            func("")

        for stanza in self.stanzas:
            for line in stanza.lines:
                for func in args:
                    func(line)
            
            for func in args:
                func("")

        for func in args:
            func("The End")

    def compose (self) -> None:
        th = TextHandler()

        self.title = th.stringify ("The",th.pluralize(self.unit),"of",self.substance,"Song")

        for unit_num in range(self.howmany,0,-1):
            stanza = Stanza()

            stanza.add(th.stringify (unit_num,th.pluralize(self.unit,unit_num),"of",self.substance,"on the",self.location))
            stanza.add(th.stringify (unit_num,th.pluralize(self.unit,unit_num),"of",self.substance))

            if unit_num == 1:
                stanza.add(th.stringify("If that",self.unit,"should happen to fall"))
                stanza.add(th.stringify("There'll be no more",th.pluralize(self.unit),"of",self.substance,"on the",self.location))
            else:
                stanza.add(th.stringify ("If one of those",th.pluralize(self.unit,unit_num),"should happen to fall"))
                stanza.add(th.stringify ("That's",unit_num-1,th.pluralize(self.unit,unit_num-1),"of",self.substance,"on the",self.location))

            self.stanzas.append(stanza)
    