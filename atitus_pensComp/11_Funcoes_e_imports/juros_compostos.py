def calcular_juros_compostos(principal, taxa, tempo):
    """
    Calcula o montante de um investimento com juros compostos.

    Argumentos:
    principal (float): O principal inicial investido.
    taxa (float): A taxa de juros (em decimal).
    tempo (int): O período de tempo em anos.

    Retorna:
    float: O montante total após o período de tempo especificado.
    """
    return principal * (1 + taxa) ** tempo


def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    """
    Calcula o montante de um investimento com juros compostos de forma recursiva.

    Argumentos:
    principal (float): O principal inicial investido.
    taxa (float): A taxa de juros (em decimal).
    tempo (int): O período de tempo em anos.

    Retorna:
    float: O montante total após o período de tempo especificado.
    """
    if tempo == 0:
        return principal
    return calcular_juros_compostos_recursivo(principal, taxa, tempo - 1) * (1 + taxa)


principal = 1000  # Principal inicial
taxa = 0.05  # Taxa de juros de 5% (em decimal) == 5 / 100
tempo = 5  # 5 anos

montante_total = calcular_juros_compostos(principal, taxa, tempo)
print(f"Montante total após {tempo} anos: R$ {montante_total}")

montante_total = calcular_juros_compostos_recursivo(principal, taxa, tempo)
print(f"Montante total após {tempo} anos: R$ {montante_total}")
