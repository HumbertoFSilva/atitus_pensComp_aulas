def real_para_dolar(valor, tx_conversao):
    if valor <= -0.99:  
        return 'valor invalido'
    conversao = valor / tx_conversao  
    return round(conversao, 2)  

def test():
    assert real_para_dolar(500, 5.20) == 96.15 
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33  
    assert real_para_dolar(-1, 5.20) == 'valor invalido'