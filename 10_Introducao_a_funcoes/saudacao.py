from typing import Optional

def saudacao(nome, sobrenome: Optional[str] = None, titulo: Optional[str] = 'Sr.') -> str:
    if nome == '':
        return f'Olá!'
    if sobrenome is None:
        return f'Olá, {titulo} {nome}'
    elif titulo is None:
        return f'Olá, {titulo} {nome} {sobrenome}'
    elif titulo is not None:
        return f'Olá, {titulo} {nome} {sobrenome}'
    else:
        return f'Olá, {titulo} {nome} {sobrenome}'


def test():
    assert saudacao("Matheus") == "Olá, Sr. Matheus"
    assert saudacao("Matheus", "Jardim") == "Olá, Sr. Matheus Jardim"
    assert saudacao("Matheus", "Jardim", "Prof") == "Olá, Prof Matheus Jardim"
    assert saudacao("Matheus", titulo="Prof") == "Olá, Prof Matheus"
    assert saudacao("") == "Olá!"

print(saudacao('Daniel', 'Rockenbach', 'estudante'))