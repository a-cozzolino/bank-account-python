from Conto import Conto
from typing import override

class InvalidCommissionError(Exception):
    pass

class ContoCorrente(Conto):
    def __init__(self, id, proprietario, saldo, commissione):

        if type(commissione) not in [int, float] or commissione < 0:
            raise InvalidCommissionError("Commissione inserita non valida. Deve essere un numero positivo o zero.")
                    
        super().__init__(id, proprietario, saldo)

        self.__commissione = commissione


    @property
    def commissione(self):
        return self.__commissione

    @override
    def preleva(self, somma):
        return super().preleva(somma + self.__commissione)

    

