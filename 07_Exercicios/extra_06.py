
def valor_pgto(valor, metodo):
    if metodo == 1:
        return valor * 0.85  
    elif metodo == 2:
        return valor * 0.90  
    elif metodo == 3:
        return valor         
    elif metodo == 4:
        return valor * 1.10  
    else:
        return None          

def interface_usuario():
    valor = float(input('Digite o valor do produto: R$ '))
    print('\nFormas de pagamento:')
    print('1 - PIX (15% de desconto)')
    print('2 - À vista no crédito (10% de desconto)')
    print('3 - Parcelado em 2x (sem juros)')
    print('4 - Parcelado em 3x (10% de juros)')
    
    metodo = int(input('\nQual a forma de pagamento? '))
    resultado = valor_pgto(valor, metodo)
    
    if resultado is None:
        print('Opção inválida!')
    elif metodo == 3:
        print(f'\nValor total: R$ {resultado:.2f} (2x de R$ {resultado/2:.2f})')
    elif metodo == 4:
        print(f'\nValor total: R$ {resultado:.2f} (3x de R$ {resultado/3:.2f})')
    else:
        print(f'\nValor total com desconto: R$ {resultado:.2f}')

def test():
    assert valor_pgto(100, 1) == 85
    assert valor_pgto(100, 2) == 90
    assert valor_pgto(100, 3) == 100
    assert round(valor_pgto(100, 4), 2) == 110  