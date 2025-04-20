def hora_para_minuto(valor):
    return valor * 60

def minuto_para_segundo(valor):
    return valor * 60

def hora_para_segundo(valor):
    return valor * 60 * 60 

def dia_para_segundo(valor):
    return valor * 60 * 60 * 24

def test():
    assert hora_para_minuto(0) == 0
    assert hora_para_minuto(1) == 60
    assert hora_para_minuto(2) == 120
    assert hora_para_minuto(5) == 300

    assert minuto_para_segundo(0) == 0
    assert minuto_para_segundo(1) == 60
    assert minuto_para_segundo(2) == 120

    assert hora_para_segundo(0) == 0
    assert hora_para_segundo(1) == 3600  
    assert hora_para_segundo(2) == 7200  

    assert dia_para_segundo(0) == 0
    assert dia_para_segundo(1) == 86400
    assert dia_para_segundo(2) == 172800

print(hora_para_minuto(5))

print(minuto_para_segundo(5))

print(hora_para_segundo(5))

print(dia_para_segundo(1))