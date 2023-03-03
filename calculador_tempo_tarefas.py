from time import *

import os
def clear(): os.system('cls') #on Windows System

def boas_vindas():
    print("================================================")
    print("Auxiliar de tarefas !")
    print("Criado por pfmello !")
    print("================================================")

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

def verifica_se_digitou_numero(acumulador, lista):
    passou = False
    for numero in lista:
        if acumulador == numero:
            passou = True

    if (passou):
        return True
    else:
        return False

def concertar_erro(lista):
    n = lista.pop()
    print("================================================")
    print(f"{n} removido da lista !")
    print(lista)
    print("================================================")
    return lista

def checa_erros(erros_totais):
    if erros_totais < 0:
        erros_totais = 0
    return erros_totais

def teste_de_paciencia(erros_totais):
    if erros_totais == 2:
        print("ESTÁ ME TESTANDO ? É MELHOR PARAR...")
    if erros_totais == 3:
        print("VOCÊ ESTÁ BRINCANDO COM QUEM NÃO DEVE !")
    if erros_totais == 4:
         print("ESTE É O SEU ÚLTIMO AVISO ANTES DA PUNIÇÃO !")
    if erros_totais == 5:
        print("VAI TOMAR NO SE FUDER !!!!!!!")
        sleep(3)
        for numero in range(99999):
            print("MORRE DIABO !!!")
        exit()
        
    print("================================================")
    print("Lista até agora: ")
    print(total)
    
def finalizar(total):
    resultado = 0
    
    for numero in total:
        numero = float(numero)
        resultado += numero
                
    tarefas = len(total)
    resultado = round(resultado, 2)
    mensagem = f"ACABOU ! No total, deu {resultado} minutos e {tarefas} tarefas !"
    
    print(mensagem)
    arquivo = open("registro.txt","w")
    arquivo.write("Este programa foi criado por DevGordo ! \n")
    arquivo.write(mensagem + "\n")
    arquivo.write("Abaixo, veja o tempo de cada tarefa registrado como log ! \n")
    
    for item in total:
        arquivo.write(item + "\n")
        
    arquivo.close()
    print("Os resultados foram registrados em um arquivo chamado registro.txt, na mesma pasta deste programa !")
    print("================================================")
    input("Aperte ENTER para sair !")
    
    exit()
########################## INICIO DO SCRIPT #############################
boas_vindas()

iniciou = True
total = []
erros_totais = 0


while iniciou:
    erros_totais = checa_erros(erros_totais)
    #print("erros totais está em :",erros_totais)
    
    print("Digite SAIR para terminar ! Pode ser em minúsculo !")
    print("================================================")
    acumulador = input("Insira o tempo da tarefa em MINUTOS: ")
        
    lista = cria_lista_de_numeros_validos()
    
    numero_valido = verifica_se_digitou_numero(acumulador, lista)
    errou = acumulador.upper() == "ERRO"

    if errou:
        clear()
        erros_totais -= 1
        concertar_erro(total)

    elif not numero_valido:
        clear()
        print("================================================")
        print("Está trolando ? É PARA DIGITAR NÚMERO VÁLIDO!")
        print("DE 1 A 101 ! INTEIRO OU DECIMAL !")
        print("ÉS MONGOLÓIDE ??! É MELHOR NÃO ME ESTRESSAR OU ME VINGAREI !")
        erros_totais += 1
        teste_de_paciencia(erros_totais)

    else:
        total.append(acumulador)
        clear()
        print("================================================")
        print("Lista de minutos adicionados até agora: ")
        print(total)
        print ("Errou algo porque é BURRO ? Digite ERRO para remover o último da lista ! ")
        print("================================================")

    if acumulador.upper() == "SAIR":
        clear()
        erros_totais -= 1
        print("================================================")
        print("================================================")
        print("Você realmente acabou ?")
        print("Lista até agora:", total)
        decisao = input("Digite SIM para realmente terminar :")
        print("================================================")
        print("================================================")
        
        if decisao.upper() == "SIM":
            finalizar(total)
            
        else:
            clear()
            print("Então vamos continuar essa zoeira !")
            print(total)
            continue
#fim
