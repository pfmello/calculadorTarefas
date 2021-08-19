def cria_lista_de_numeros_validos():
    lista =[]
    qtd_numeros = 101
    n = 0
    while n < qtd_numeros:
        n2 = str(n)
        decimais = ["",".1",".2",".3",".4",".5",".6",".7",".8",".9"]
        
        for digito in decimais:
            lista.append(n2 + digito)

        n += 1
    return lista
