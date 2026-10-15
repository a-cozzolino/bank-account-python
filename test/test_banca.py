from Banca import Banca, InvalidAccountError, AccountNotFoundError, SameAccountError, AmountNotAllowedError
import pytest
from Conto import Conto, NotEnoughFundsError
from ContoCorrente import ContoCorrente
from ContoRisparmio import ContoRisparmio

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

# Verifica polimorfismo: banca può conservare diversi tipi di conti correnti
def test_raccolta_conti():
    conto1 = Conto("005","Mario",2033)
    conto2 = ContoCorrente("P98","Antonio", 290, 2)
    conto3 = ContoRisparmio("L34","Angelica", 15000, 3)

    banca = Banca()
    banca.aggiungi_conto(conto1)
    banca.aggiungi_conto(conto2)
    banca.aggiungi_conto(conto3)
    assert banca.get_conto("005") is conto1
    assert banca.get_conto("P98") is conto2
    assert banca.get_conto("L34") is conto3

def test_prelievo_polimorfico():
    conto1 = Conto("005", "Mario", 1000)
    conto2 = ContoCorrente("P98", "Antonio", 1000, 2)
    conto3 = ContoRisparmio("L34", "Angelica", 1000, 3)

    conti = [conto1, conto2, conto3]

    for conto in conti:
        conto.preleva(100)

    assert conto1.saldo == 900
    assert conto2.saldo == 898
    assert conto3.saldo == 900


def test_salva_e_carica_conti(tmp_path):
    banca = Banca()
    banca.aggiungi_conto(Conto("001", "Alex", 1000))
    banca.aggiungi_conto(ContoCorrente("002", "Mario", 500, 2))
    banca.aggiungi_conto(ContoRisparmio("003", "Luigi", 2000, 3))

    banca.salva_su_file(tmp_path)

    banca_caricata = Banca().carica_conti_da_file(tmp_path)

    conti = banca_caricata.get_conti()

    assert len(conti) == 3

    assert type(conti["001"]) is Conto
    assert type(conti["002"]) is ContoCorrente
    assert type(conti["003"]) is ContoRisparmio

    assert conti["001"].saldo == 1000
    assert conti["002"].commissione == 2
    assert conti["003"].interesse == 3

def test_carica_conti_file_not_found(tmp_path):
    banca = Banca()

    percorso_inesistente = tmp_path / "cartella_inesistente"

    with pytest.raises(FileNotFoundError):
        banca.carica_conti_da_file(percorso_inesistente)
