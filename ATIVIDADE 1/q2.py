while True:
    num = float(input("Digite um número para verificar se é par ou ímpar. Para encerrar a aplicação, digite 0: "))
    
    if num == 0:
        print("Aplicação Finalizada! \n")
        break

    elif num%2==0:
        print("PAR \n")
        
    else:
        print("IMPAR \n")
    
