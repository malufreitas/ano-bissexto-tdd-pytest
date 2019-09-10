'''
Um ano é bissexto se:

O ano for divisivel por 4, mas não divisível por 100, exceto se ele for também 
divisivel por 400.

Exemplo anos bissexto: 1600, 1732, 1944, 2008

Exemplo anos não bissexto: 1742, 1889, 1951, 2011
'''

import pytest

# Função para calcular ano bissexto
def eh_bissexto(ano):
    resto4 = ano % 4
    resto100 = ano % 100
    resto400 = ano % 400

    if ((not resto4) and (resto100)) or (not resto400):
        return True
    return False


### Não deve ser bissexto
@pytest.mark.parametrize('ano', [500, 600, 1500, 1742, 1889, 1951, 2011])  # Setup 
def test_nao_deve_ser_bissexto(ano):
    resp = eh_bissexto(ano)  # Execução do teste
    
    assert resp is False  # Verificação do resultado do teste


### Deve ser bissexto
@pytest.mark.parametrize('ano', [1600, 1732, 1944, 2008])  # Setup
def test_deve_ser_bissexto(ano):
    resp = eh_bissexto(ano)  # Execução do teste
    
    assert resp is True  # Verificação do resultado do teste