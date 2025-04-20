def fatorial(numero):
	if numero < 0:
		return None 
	if numero == 0:
		return 1
	resultado = 1
	for n in range(1, numero + 1):
		resultado *= n
		print(n, resultado )
	return resultado

def test():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120
    assert fatorial(-1) is None

fatorial(10)
