from Conto import Conto, InvalidAmountError, InvalidWithdrawalError, InvalidDepositError, InvalidAccountError, NotEnoughFundsError
import os
from Banca import Banca, AccountNotFoundError, AmountNotAllowedError, SameAccountError
from ContoCorrente import ContoCorrente
from ContoRisparmio import ContoRisparmio

# serve per pulire la console prima di eseguire il codice
os.system("cls")

conto = Conto("001", "Alessandro", 1000)

print(conto.visualizza_saldo())

try:
    conto.deposita(200)
except InvalidDepositError as e:
    print(f"Errore durante il deposito: {e}")


print(conto.visualizza_saldo())
try:
    conto.preleva(200)
except InvalidWithdrawalError as e:
    print(f"Errore durante il prelievo: {e}")
except NotEnoughFundsError as e:
    print(f"Errore durante il prelievo: {e}")

print(f"il tuo saldo finale è: {conto.visualizza_saldo()}")

print(conto.id)

try:
    conto2 = Conto("002", "Giovanni", 400)
    banca = Banca()
    banca.aggiungi_conto(conto)
    banca.aggiungi_conto(conto2)

    banca.trasferisci_denaro("001", "002", 300)
except InvalidWithdrawalError as e:
    print(f"Errore durante il trasferimento: {e}")
except NotEnoughFundsError as e:
    print(f"Errore durante il trasferimento: {e}")

print(f"Saldo conto 001: {conto.visualizza_saldo()}")
print(f"Saldo conto 002: {conto2.visualizza_saldo()}")

try:
    conto3 = ContoCorrente("005","Deborah",1000,1)
    conto3.preleva(100)
except NotEnoughFundsError as e:
    print(f"Non si disponde dei fondi necessari al prelievo inserito: {e}")

print(f"Saldo conto 003: {conto3.saldo}")


#Aggiungo dei conti correnti e risparmio
conto_corrente = ContoCorrente("003", "Mario", 1000, 1)
conto_risparmio = ContoRisparmio("004", "Luigi", 2000, 2)

banca.aggiungi_conto(conto_corrente)
banca.aggiungi_conto(conto_risparmio)

for conto in banca.get_conti().values():
    print(f"Il saldo di {conto.id} è {conto.saldo}")
    
interesse_maturato = conto_risparmio.calcola_interesse()
conto_risparmio.paga_interessi()
print(conto_risparmio.saldo)

print("Ciao ")
print(0.1+0.2)
print(0.1+0.2 == 0.3)