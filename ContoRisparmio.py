from Conto import Conto

class InvalidInteresseError(Exception):
    pass

class ContoRisparmio(Conto):
    def __init__(self, id: str, proprietario: str, saldo: int | float, interesse: int | float) -> None:

        """
        Args:
            id: identificativo del conto univoco
            proprietario: Nome del proprietario del conto
            saldo: Saldo iniziale del conto, può essere zero o positivo
            interesse: interesse specifico del conto, utilizzata per maturare interessi
        Raises:
            InvalidInteresseError: se la commissione è negativa
            o non di tipo int/float 
        """
        super().__init__(id, proprietario, saldo)

        if type(interesse) not in [int, float] or interesse < 0:
            raise InvalidInteresseError("L'interesse inserito non è numerico o è inferiore a zero.")
        
        self.__interesse = interesse

    @property
    def interesse(self) -> int | float:
        """Restituisce il tasso di interesse del conto."""
        return self.__interesse

    def calcola_interesse(self) -> float:
        """Calcola l'interesse specifico del conto e ne restituisce il valore maturato"""
        interesse_maturato = (self.__interesse * self.saldo) /100
        return interesse_maturato

    def paga_interessi(self) -> float:
        """Aggiunge l'interesse maturato al saldo del conto. Returns il saldo aggiornato."""
        interesse_maturato = self.calcola_interesse()

        if interesse_maturato > 0:
            self.deposita(interesse_maturato)

    def to_dict(self):
        conto_dict = super().to_dict()
        conto_dict["tipo"] = "conto_risparmio"
        conto_dict["interesse"] = self.interesse

        return conto_dict