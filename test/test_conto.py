from Conto import Conto, InvalidDepositError, InvalidWithdrawalError, NotEnoughFundsError, InvalidAmountError, InvalidAccountError
import pytest 


def test_costruttore_saldo_non_numerico():
    with pytest.raises(InvalidAmountError):
        Conto("001", "Alex", "200")

def test_costruttore_saldo_negativo():
    with pytest.raises(InvalidAmountError):
        Conto("001", "Alex", -200)

def test_costruttore_proprietario_not_str():
    with pytest.raises(InvalidAccountError):
        Conto("001", 20 , 2003)

def test_costruttore_ID_not_str():
    with pytest.raises(InvalidAccountError):
        Conto(25, "Luca", 2003)

def test_costruttore_saldo_zero():
    conto = Conto("001", "Alex", 0)

    assert conto.saldo == 0

def test_saldo_iniziale():
    
    # Test iniziale del saldo
    conto = Conto("001", "Alessandro", 1000)
    assert conto.saldo == 1000

def test_deposito_valido():
    conto = Conto("001", "Alessandro", 1000)
    conto.deposita(200)
    assert conto.visualizza_saldo() == 1200

def test_deposito_non_valido():
    conto = Conto("001", "Luca", 2500)

    with pytest.raises(InvalidDepositError):
        conto.deposita(-100)

def test_deposito_zero():
    conto = Conto("001", "Luca", 2500)
    
    with pytest.raises(InvalidDepositError):
        conto.deposita(0)

def test_deposito_valore_non_valido():
    conto = Conto("001", "Luca", 2500)

    with pytest.raises(InvalidDepositError):
        conto.deposita("100")

def test_preleva_importo_non_numerico():
    conto = Conto("004", "Maria", 1500)

    with pytest.raises(InvalidWithdrawalError):
        conto.preleva("300")

def test_preleva_importo_negativo():
    conto = Conto("004", "Maria", 1500)

    with pytest.raises(InvalidWithdrawalError):
        conto.preleva(-250.20)

def test_preleva_fondi_insufficienti():
    conto = Conto("004", "Maria", 1500)

    with pytest.raises(NotEnoughFundsError):
        conto.preleva(3000)

def test_preleva_zero():
    conto = Conto("004", "Maria", 1500)

    with pytest.raises(InvalidWithdrawalError):
        conto.preleva(0)

def test_preleva_valido():
    conto = Conto("01A", "Mario", 2000)
    conto.preleva(400)

    assert conto.visualizza_saldo() == 1600