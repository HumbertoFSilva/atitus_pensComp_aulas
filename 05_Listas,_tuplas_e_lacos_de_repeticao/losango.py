def desenha_losango(altura):
    if altura % 2 == 0:
        altura = altura + 1

    meio = altura // 2
    for line  in range(altura):
        if line <= meio:
            espacos =  meio - line
            estrelas = line * 2 + 1
        else:
            espacos = line - meio
            estrelas = altura - (line - meio)*2
        print(' ' * espacos + '*' * estrelas)
    
    


altura = int(input("Digite um valor ímpar para a altura do losango: "))
desenha_losango(altura)


#altura = int(input("Digite um valor ímpar para a altura do losango: "))
# Se a altura for par, incrementa em 1 para garantir uma linha central
#if altura % 2 == 0:
 #   altura = altura + 1
  #  print("O valor digitado era par, usaremos", altura, "no lugar")

#meio = altura // 2  # Linha do meio do losango (considere que a contagem inicia em 0)
#for linha_atual in range(altura):  # Itera de 0 até altura
    # Desenhando a parte superior do losango (primeira linha até meio, incluindo o meio)
#    if linha_atual <= meio:
#        num_espacos = meio - linha_atual
#       num_star = linha_atual * 2 + 1
#    else:  # Desenhando parte inferior do losango
#        num_espacos = linha_atual - meio
#        num_star = altura - (linha_atual - meio) * 2
#    print("." * num_espacos + "#" * num_star)