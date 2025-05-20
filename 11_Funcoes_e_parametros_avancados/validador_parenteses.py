def validador_parenteses(entrada: str) -> bool:
    balance = 0
    for char in entrada:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


def test_validos():
    assert validador_parenteses("()")
    assert validador_parenteses("()()")
    assert validador_parenteses("(())")
    assert validador_parenteses("(()()())")
    assert validador_parenteses("(((())()))")


def test_invalidos():
    assert not validador_parenteses(")")
    assert not validador_parenteses("(")
    assert not validador_parenteses("()(")
    assert not validador_parenteses("()()())")
    assert not validador_parenteses("(((())())")