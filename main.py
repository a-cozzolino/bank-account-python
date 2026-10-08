from Conto import Conto, InvalidAmountError, InvalidWithdrawalError, InvalidDepositError, InvalidAccountError, NotEnoughFundsError
import os
from Banca import Banca, AccountNotFoundError, AmountNotAllowedError, SameAccountError

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