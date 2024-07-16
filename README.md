# Pensamento Computacional - Execícios de aula

- [Prof Matheus Jardim Bernardes](https://matheusjardimb.com/)
- [Atitus.edu.br](https://atitus.edu.br/)

Exercícios de aula da disciplina de Pensamento Computacional.

## Sobre mim

PREENCHER

## Fork do projeto

Para criar o seu próprio projeto, clique no botão 'Fork' no topo da tela
em [https://github.com/matheusjardimb/atitus_pensComp_aulas/](https://github.com/matheusjardimb/atitus_pensComp_aulas/).

Após isso, será necessário ativar a execução das 'Actions'. Para isso, acesse o menu 'Actions' no topo da tela e clique
na opção de ativar workflows.

## Testes automatizados

Este repositório está configurado para que os testes automatizados sejam executados a cada novo commit diretamente no
GitHub.

Para mais informações, consulte o arquivo [.github/workflows/tests.yml](.github/workflows/tests.yml).

Para executar os testes em seu computador:

```bash
# Instale as dependências (apenas necessário executar uma vez)
pip install -r requirements.txt

# Execute os testes
pytest
```

## Ao desenvolver no seu computador

Considere instalar o [PyEnv](https://github.com/pyenv/pyenv) para gerenciar múltiplas versões de Python em seu
computador.

A versão de Python sugerida/necessária para executar as atividades deste projeto está no
arquivo [.python-version](.python-version).

Caso esteja usando o [Git](https://git-scm.com/), considere utilizar o pre-commit:

```bash
pre-commit install
```