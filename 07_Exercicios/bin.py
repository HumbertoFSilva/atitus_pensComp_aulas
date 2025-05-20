def dec_to_bin(num):
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary  # Adiciona o bit à esquerda
        num = num // 2
    return binary

def bin_to_dec(val):
    decimal = 0
    for i, bit in enumerate(reversed(val)):
        decimal += int(bit) * (2 ** i)
    return decimal

def test():
    assert dec_to_bin(0) == '0'
    assert dec_to_bin(1) == '1'
    assert dec_to_bin(2) == '10'
    assert dec_to_bin(3) == '11'
    assert dec_to_bin(4) == '100'
    assert dec_to_bin(10) == '1010'

    assert bin_to_dec('0') == 0
    assert bin_to_dec('1') == 1
    assert bin_to_dec('10') == 2
    assert bin_to_dec('11') == 3
    assert bin_to_dec('100') == 4
    assert bin_to_dec('1010') == 10