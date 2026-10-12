from Conto import Conto, InvalidAmountError, InvalidWithdrawalError, InvalidDepositError, InvalidAccountError, NotEnoughFundsError

class AccountNotFoundError(Exception):
    pass

class AmountNotAllowedError(Exception):
    pass

class SameAccountError(Exception):
    pass


class Banca :
    def __init__(self):
        self.__conti = {}

    def get_conto(self, id_conto):
        if id_conto not in self.__conti:
            raise AccountNotFoundError(f"Nessun conto trovato con ID {id_conto}")
        
        return self.__conti[id_conto]

    def aggiungi_conto(self, conto):
        if not isinstance(conto, Conto):
            raise InvalidAccountError("L'oggetto fornito non è un'istanza della classe Conto.")
        
        if conto.id in self.__conti:
            raise InvalidAccountError(f"Un conto con ID {conto.id} esiste già.")
        
        self.__conti[conto.id] = conto

    def rimuovi_conto(self, id_conto):
        if id_conto not in self.__conti:
            raise AccountNotFoundError(f"Nessun conto trovato con ID {id_conto}.")
        
        del self.__conti[id_conto]

    def trasferisci_denaro(self, id_mittente, id_destinatario, somma):
	
        if id_mittente not in self.__conti:
            raise AccountNotFoundError(f"Nessun conto trovato con ID {id_mittente}.")
        
        if id_destinatario not in self.__conti:
            raise AccountNotFoundError(f"Nessun conto trovato con ID {id_destinatario}.")

        if id_mittente == id_destinatario:
            raise SameAccountError("Non è possibile trasferire denaro allo stesso conto.")

        if type(somma) not in [int, float] or somma <= 0:
            raise AmountNotAllowedError(f"Inserire importo numerico da trasferire > 0.0 euro")
        
        
        conto1 = self.__conti[id_mittente]
        conto2 = self.__conti[id_destinatario]

        conto1.preleva(somma)
        conto2.deposita(somma)


    def get_conti(self):
        return self.__conti.copy()
    