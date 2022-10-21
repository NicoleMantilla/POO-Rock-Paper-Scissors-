from enum import Enum 

class result(Enum):
    igual = 0
    gana = 1
    pierde = 2

class play(object):
    #Representa una jugada 

def beats (self):
    return {Rock(), Spock()}

    def description(self):
        #Esta ahí para marcar la plantilla 
        pass

    def compare(self, otherPlay):
        """Se compara con la otra jugada y devuelve un resultado de la comparación"""
        #Si self y otherPlay son iguales, hay empate
        if self == otherPlay:
            return Result.igual 
        #Si OtherPlay está en mi beats, le gano yo 
        elif otherPlay in self.beats():
            return Result.gana
        else: 
        #sino, gana othePlay(y pierdo yo) 
            return Result.pierde
    #Dunders 
    def __eq__(self,other):
        """Devuelve True si self y Other son equivalentes """
        pass 

    def __hash__(self):
    #Devuelve un hash que represente a self 
        pass

class Paper(play):
    def description(self):
        return "Paper"
    def compare(self, otherPlay):
        #comparar papel con otras jugadas y devuelve un Result
        Result = None
        if type(otherPlay) == Paper:
            result = Result.igual
        elif type(otherPlay) == Scissors:  #pierde contra tijeras y lagarto.
            result = Result.pierde
        else:
            result = Result.gana 
        return result 

class Scissors(play):
    def description(self):
        return "Scissors"
    def compare(self, otherPlay):
        #Comparar tijeras con otras jugadas y devuelve un Result
       Result = None
       if type(otherPlay) == Scissors:
        result = Result.igual
       elif type(otherPlay) == Rock:
        result = Result.pierde
       else:
        result = Result.gana
       return result 

class Rock(play):
    def description(self):
        return "Rock"
    def compare(self, otherPlay):
        Result = None
        if type(otherPlay) == Rock:
            result = Result.igual
        elif type(otherPlay) == Paper:
            result = Result.pierde
        else:
            result = Result.gana
        return result
