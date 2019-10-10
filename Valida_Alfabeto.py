import re

class Valida_Alfabeto():

    def __init__(self,expresion):
        self.expresion=expresion


    def valida_expresion(self):
        patron = re.compile(r'^([abc]+)$')
        val=patron.search(self.expresion)
        try:
           val.start()
           return True
           

        except:
            return False
