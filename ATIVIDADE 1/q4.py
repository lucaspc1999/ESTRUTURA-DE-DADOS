numeros=[]


    
while True:
    print("Sua lista atual: \n", numeros)
    
    num=float(input("Digite um número para inseri-lo na lista ou digite 0 para exibir o resultado: "))

    if num != 0:
        
        #INSERE NA LISTA O NÚMERO E COLOCA EM ORDEM CRESCENTE JUNTO AOS OUTROS
        numeros.append(num)
        numeros.sort()

        #DEFINE A PRIMEIRA POSIÇÃO E AULTIMA DA LISTA APÓES A ORDENAÇÃO CRESCENTE
        menor=numeros[0]
        maior=numeros[-1]
        

    else:
        break

print("O menor valor da sua lista: ", menor)
print("O maior valor da sua lista: ", maior)   
