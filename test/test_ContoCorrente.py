import pytest
from ContoCorrente import ContoCorrente, InvalidCommissionError
from Conto import InvalidAmountError, NotEnoughFundsError, InvalidWithdrawalError

def test_costruttore_invalid_commission_negative():

    with pytest.raises(InvalidCommissionError):
        ContoCorrente("001", "Alessandro", 1000, -1)
    
def test_costruttore_invalid_commission_str():

    with pytest.raises(InvalidCommissionError):
        ContoCorrente("001", "Alessandro", 1000, "dieci") 

def test_costruttore_commissione_zero():
    conto = ContoCorrente("003", "Maria", 1403, 0)

    assert conto.commissione == 0

def test_costruttore_saldo_inferiore_a_zero():

    with pytest.raises(InvalidAmountError):
        ContoCorrente("009", "Mattia", -394, 1)

def test_prelievo_con_commissione():
    conto = ContoCorrente("A93", "Luciano", 1000, 2)

    conto.preleva(100)
    # Verifica che il saldo totale sia di 1000 - 100 - 2(commissione) = 898
    assert conto.saldo == 898

def test_prelievo_fondi_insufficienti():
    conto = ContoCorrente("A93", "Luciano", 1000, 2)

    with pytest.raises(NotEnoughFundsError):
        conto.preleva(999)

    #verifica anche che il saldo rimanga invariato dopo l'eccezione
    assert conto.saldo == 1000

def test_prelievo_importo_pari_al_saldo_con_commissione():
    conto = ContoCorrente("A93", "Luciano", 1000, 2)

    with pytest.raises(NotEnoughFundsError):
        conto.preleva(1000)

    #verifica anche che il saldo rimanga invariato dopo l'eccezione
    assert conto.saldo == 1000

def test_prelievo_importo_sfora_con_commissione():
    conto = ContoCorrente("A93", "Luciano", 999, 2)

    with pytest.raises(NotEnoughFundsError):
        conto.preleva(998)

    #verifica anche che il saldo rimanga invariato dopo l'eccezione
    assert conto.saldo == 999

def test_preleva_input_stringa():
    conto = ContoCorrente("A93", "Luciano", 1000, 2)

    with pytest.raises(InvalidWithdrawalError):
        conto.preleva("100")

    #verifica anche che il saldo rimanga invariato dopo l'eccezione
    assert conto.saldo == 1000