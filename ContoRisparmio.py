from Conto import Conto
from typing import override

class ContoRisparmio(Conto):
    def __init__(self, id, proprietario, saldo, interesse):
        super().__init__(id, proprietario, saldo)
        self.__interesse = interesse

    def calcola_interesse(self):
        interesse_maturato = (self.__interesse * self.saldo) /100
        return interesse_maturato

    def paga_interessi(self):
        interesse_maturato = self.calcola_interesse()
        
        if interesse_maturato > 0:
            self.deposita(interesse_maturato)