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

    def __init__(self, id, proprietario, saldo):
        if type(saldo) not in [int, float] or saldo < 0:
            raise InvalidAmountError("Saldo iniziale non valido. Deve essere un numero positivo o zero.")
            
        if type(id) != str or type(proprietario) != str:
            raise InvalidAccountError("ID e proprietario devono essere stringhe.")

        self.__id = id
        self.__proprietario = proprietario
        self.__saldo = saldo
        
    @property
    def id(self):
        return self.__id

    @property
    def proprietario(self):
        return self.__proprietario

    @property
    def saldo(self):
        return self.__saldo


    def deposita(self, somma):
        if type(somma) not in [int, float] or somma <= 0:
            raise InvalidDepositError("Somma da depositare non valida. Deve essere un numero positivo.")
        
        self.__saldo += somma
        return self.__saldo

    def preleva(self, somma):
    
        if type(somma) not in [int, float] or somma <= 0:
            raise InvalidWithdrawalError("Somma che stai cercando di prelevare non è valida.")
        if somma > self.__saldo:
            raise NotEnoughFundsError("Fondi insufficienti.")
        
        self.__saldo -= somma
    
        return self.__saldo

    def visualizza_saldo(self):
        return self.__saldo

