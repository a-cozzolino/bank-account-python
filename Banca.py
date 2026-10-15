from Conto import Conto, InvalidAmountError, InvalidWithdrawalError, InvalidDepositError, InvalidAccountError, NotEnoughFundsError
import json
from pathlib import Path
from ContoCorrente import ContoCorrente
from ContoRisparmio import ContoRisparmio


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

    def to_dict(self) -> list[dict]:
        """Prepara i conti presenti in banca in dizionari per essere serializzati
        Returns la lista di oggetti dizionario opportunamente costruiti dai metodi to_dict di
        ogni sottoclasse di appartenenza."""
        conti = []

        for conto in self.__conti.values():
            conti.append(conto.to_dict())

        return conti

    def salva_su_file(self, percorso):
        percorso_file = Path(percorso) / "conti.json"

        with open(percorso_file, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=4, ensure_ascii=False)

    def carica_conti_da_file(self, percorso) -> Banca:
        percorso_file = Path(percorso) / "conti.json"

        try:
            with open(percorso_file, "r", encoding="utf-8") as file:
                # mi creo la lista di dizionari dal file json in lettura
                dict_list = json.load(file)
        except FileNotFoundError:
                raise FileNotFoundError(f"File dei conti non trovato: {percorso_file}")
      
        banca = Banca()    

        for conto in dict_list:
            if conto["tipo"] == "conto":
                banca.aggiungi_conto(Conto(conto["id"], conto["proprietario"], conto["saldo"]))
            elif conto["tipo"] == "conto_corrente":
                banca.aggiungi_conto(ContoCorrente(conto["id"], conto["proprietario"], conto["saldo"], conto["commissione"]))
            elif conto["tipo"] == "conto_risparmio":
                banca.aggiungi_conto(ContoRisparmio(conto["id"], conto["proprietario"], conto["saldo"], conto["interesse"]))
            else:
                raise ValueError(f"Tipo di conto sconosciuto: {conto['tipo']}")

        return banca


                    

    