from Banca import Banca, InvalidAccountError, AccountNotFoundError, SameAccountError, AmountNotAllowedError
import pytest
from Conto import Conto, NotEnoughFundsError

def test_aggiungi_conto():
    banca = Banca()
    conto = Conto("001", "Alessandro", 0)

    banca.aggiungi_conto(conto)

def test_aggiungi_conto_fail():
    banca = Banca()
    with pytest.raises(InvalidAccountError):
        banca.aggiungi_conto(("AAA", 200))

def test_aggiunta_conti_con_ID_diversi():
    banca = Banca()
    
    conto1 = Conto("A34", "Luca", 4500)
    conto2 = Conto("B32", "Alex", 4500)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

def test_conti_same_ID():
    banca = Banca()
    with pytest.raises(InvalidAccountError):
        conto1 = Conto("B32", "Luca", 4500)
        conto2 = Conto("B32", "Alex", 2500)

        banca.aggiungi_conto(conto1)
        banca.aggiungi_conto(conto2)

def test_rimuovi_conto_pass():
    conto1 = Conto("B32", "Luca", 4500)
    conto2 = Conto("N35", "Alex", 2500)

    banca = Banca()
    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    #Ora cerco di rimuovere il conto 1 e verifico che Banca abbia solo il conto 2
    banca.rimuovi_conto("B32")

    #controllo che conto 2 è in banca
    assert banca.get_conto("N35") == conto2

    #controlla che il conto 1 non c'è più
    with pytest.raises(AccountNotFoundError):
        banca.get_conto("B32")

def test_rimuovi_conto_inesistente():
    banca = Banca()

    with pytest.raises(AccountNotFoundError):
        banca.rimuovi_conto("001")

def test_trasferisci_denaro():
    banca = Banca()
    conto1 = Conto("001", "Alex", 5000)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    banca.trasferisci_denaro("001", "002", 1000)

    assert conto2.visualizza_saldo() == 3000
    assert conto1.visualizza_saldo() == 4000

def test_trasferisci_denaro_idmittente_missing():
    banca = Banca()
    conto1 = Conto("001", "Alex", 5000)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    with pytest.raises(AccountNotFoundError):
        banca.trasferisci_denaro("003", "002", 1000)

def test_trasferisci_denaro_iddestinatario_missing():
    banca = Banca()
    conto1 = Conto("001", "Alex", 5000)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    with pytest.raises(AccountNotFoundError):
        banca.trasferisci_denaro("001", "003", 1000)

def test_trasferisci_denaro_stesso_account():
    banca = Banca()
    conto1 = Conto("001", "Alex", 5000)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    with pytest.raises(SameAccountError):
        banca.trasferisci_denaro("001", "001", 1000)

def test_trasferisci_denaro_somma_non_numero():
    banca = Banca()
    conto1 = Conto("001", "Alex", 5000)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    with pytest.raises(AmountNotAllowedError):
        banca.trasferisci_denaro("001", "002", "cinquecento")

def test_trasferisci_denaro_zero():
    banca = Banca()
    conto1 = Conto("001", "Alex", 5000)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    with pytest.raises(AmountNotAllowedError):
        banca.trasferisci_denaro("002", "001", 0)

def test_trasferisci_denaro_somma_negativa():
    banca = Banca()
    conto1 = Conto("001", "Alex", 5000)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    with pytest.raises(AmountNotAllowedError):
        banca.trasferisci_denaro("001", "002", -542.25)

def test_trasferisci_denaro_fondi_insufficienti():
    banca = Banca()
    conto1 = Conto("001", "Alex", 500)
    conto2 = Conto("002", "Deborah", 2000)

    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)

    with pytest.raises(NotEnoughFundsError):
        banca.trasferisci_denaro("001", "002", 1000)

    assert conto1.saldo == 500
    assert conto2.saldo == 2000