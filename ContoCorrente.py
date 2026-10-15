from Conto import Conto, InvalidWithdrawalError
from typing import override

class InvalidCommissionError(Exception):
    pass

class ContoCorrente(Conto):
    def __init__(self, id: str, proprietario: str, saldo: int | float, commissione: int | float) -> None:
        """ Inizializza un ContoCorrente
        Args:
            id: identificativo del conto univoco
            proprietario: Nome del proprietario del conto
            saldo: Saldo iniziale del conto, può essere zero o positivo
            commissione: Commissione specifica del conto, utilizzata per i prelievi a pagamento
        Raises:
            InvalidCommissionError: se la commissione è negativa
            o non di tipo int/float        
        """

        if type(commissione) not in [int, float] or commissione < 0:
            raise InvalidCommissionError("Commissione inserita non valida. Deve essere un numero positivo o zero.")
                    
        super().__init__(id, proprietario, saldo)

        self.__commissione = commissione


    @property
    def commissione(self) -> int | float:
        """Restituisce la commissione specifica del conto."""
        return self.__commissione

    @override
    def preleva(self, somma: int | float) -> int | float:
        """Preleva la somma richiesta applicando la commissione del conto.

        Raises:
            InvalidWithdrawalError: se la somma richiesta non è valida.
        """
        if type(somma) not in [int, float] or somma <= 0:
            raise InvalidWithdrawalError(
                "Somma che stai cercando di prelevare non è valida."
            )

        return super().preleva(somma + self.__commissione)

    def to_dict(self):
        conto_dict = super().to_dict()
        conto_dict["tipo"] = "conto_corrente"
        conto_dict["commissione"] = self.commissione

        return conto_dict

    

