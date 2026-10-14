from ContoRisparmio import ContoRisparmio, InvalidInteresseError
import pytest

def test_calcolo_interesse():

    conto = ContoRisparmio("001", "Alex", 2000, 2)

    interesse_maturato = conto.calcola_interesse()
    assert interesse_maturato == 40.0

def test_paga_interessi():

    conto = ContoRisparmio("001", "Alex", 2000, 2)
    
    interesse_maturato = conto.calcola_interesse()
    assert interesse_maturato == 40.0

    conto.paga_interessi()
    assert conto.saldo == 2040.00

def test_paga_interesse_zero():

    conto = ContoRisparmio("001", "Alex", 2000, 0)
    
    interesse_maturato = conto.calcola_interesse()
    
    conto.paga_interessi()
    assert conto.saldo == 2000.00

def test_costruttore_invalid_interesse_str():

    with pytest.raises(InvalidInteresseError):
        ContoRisparmio("001", "Alex", 2000, "5")

def test_costruttore_invalid_interesse_negative():

    with pytest.raises(InvalidInteresseError):
        ContoRisparmio("001", "Alex", 2000, -2)