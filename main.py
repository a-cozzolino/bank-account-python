from Conto import Conto, InvalidAmountError, InvalidWithdrawalError, InvalidDepositError, InvalidAccountError, NotEnoughFundsError
import os
from Banca import Banca, AccountNotFoundError, AmountNotAllowedError, SameAccountError
from ContoCorrente import ContoCorrente
from ContoRisparmio import ContoRisparmio

# serve per pulire la console prima di eseguire il codice
os.system("cls")



def main():
    banca = Banca()

    conto = Conto("001", "Alessandro", 1000)
    conto_corrente = ContoCorrente("003", "Mario", 1000, 1)
    conto_risparmio = ContoRisparmio("004", "Luigi", 2000, 2)

    banca.aggiungi_conto(conto)
    banca.aggiungi_conto(conto_corrente)
    banca.aggiungi_conto(conto_risparmio)

    # Operazioni dimostrative
    conto.deposita(200)
    conto.preleva(100)

    banca.trasferisci_denaro("001", "003", 150)

    conto_risparmio.paga_interessi()

    # Mostra il saldo finale di ogni conto
    print("=== Saldi finali ===")
    for conto in banca.get_conti().values():
        print(f"{conto.id} - {conto.proprietario}: {conto.saldo:.2f} €")

    banca.salva_su_file(".")
    print("\nConti salvati correttamente in conti.json")    


    banca_caricata = Banca().carica_conti_da_file(".")

    print("\n=== Conti ricaricati dal file ===")
    for conto in banca_caricata.get_conti().values():
        print(f"{conto.id} - {conto.proprietario}: {conto.saldo:.2f} €")

    try:
        conto.preleva(5000)
    except NotEnoughFundsError as errore:
        print(f"Prelievo non riuscito: {errore}")



if __name__ == "__main__":
    main()
