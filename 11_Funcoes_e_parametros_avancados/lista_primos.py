def eh_primo(numero: int) -> bool:
    if numero <= 1:  # 0 and 1 are not primes
        return False
    for i in range(2, int(numero**0.5) + 1):  # More efficient checking up to square root
        if numero % i == 0:
            return False
    return True


def lista_primos(num: int) -> list:
    lista_primos = []
    for j in range(2, num + 1):  # Start from 2, the first prime number
        if eh_primo(j):
            lista_primos.append(j)
    return lista_primos


def test():
    assert lista_primos(10) == [2, 3, 5, 7]
    assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
    assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print("All tests passed!")

print(lista_primos(100))