class InvalidAmountError(Exception):
    pass   

class InvalidWithdrawalError(Exception):
    pass

class InvalidDepositError(Exception):
    pass

class InvalidAccountError(Exception):
    pass   

class NotEnoughFundsError(Exception):
    pass

class Conto:

    def __init__(self, id: str, proprietario: str, saldo: int | float) -> None:
        """Inizializza un conto bancario.

        Args:
            id: identificativo del conto univoco
            proprietario: Nome del proprietario del conto
            saldo: Saldo iniziale del conto, può essere zero o positivo
        Raises:
            InvalidAmountError: se il saldo è negativo o non di tipo int/float
            InvalidAccountError: se id o proprietario non sono stringhe
        """
        
        if type(saldo) not in [int, float] or saldo < 0:
            raise InvalidAmountError("Saldo iniziale non valido. Deve essere un numero positivo o zero.")
            
        if type(id) != str or type(proprietario) != str:
            raise InvalidAccountError("ID e proprietario devono essere stringhe.")

        self.__id = id
        self.__proprietario = proprietario
        self.__saldo = saldo
        
    @property
    def id(self) -> str:
        """Restituisce l'id del conto."""
        return self.__id

    @property
    def proprietario(self) -> str:
        """Restituisce il nome del proprietario del conto."""
        return self.__proprietario

    @property
    def saldo(self) -> int | float:
        """Restituisce il saldo del conto."""
        return self.__saldo


    def deposita(self, somma: int | float) -> int | float:
        """Deposita una somma strettamente positiva sul conto e restituisce il saldo aggiornato.

        Raises:
            InvalidDepositError: se la somma non è valida o è minore o uguale a zero.
        """
        if type(somma) not in [int, float] or somma <= 0:
            raise InvalidDepositError("Somma da depositare non valida. Deve essere un numero positivo.")
        
        self.__saldo += somma
        return self.__saldo

    def preleva(self, somma: int | float) -> int | float:
        """Preleva una somma dal conto e restituisce il saldo aggiornato.

        Raises:
            InvalidWithdrawalError: se la somma non è valida
            oppure è minore o uguale a zero.
            NotEnoughFundsError: se il saldo è insufficiente.
        """
    
        if type(somma) not in [int, float] or somma <= 0:
            raise InvalidWithdrawalError("Somma che stai cercando di prelevare non è valida.")
        if somma > self.__saldo:
            raise NotEnoughFundsError("Fondi insufficienti.")
        
        self.__saldo -= somma
    
        return self.__saldo

    def visualizza_saldo(self) -> int | float:
        """Restituisce il saldo del conto"""
        return self.__saldo

