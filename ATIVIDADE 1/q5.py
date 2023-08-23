num_par=[]
num_impar=[]


while True:
    num=float(input("Insira um número para adiciona-lo na lista, para exibir a média dos numeros digite 0: "))

    if num==0:
        break
    elif num%2==0:
        num_par.append(num)
    else:
        num_impar.append(num)

media=sum(num_par)/len(num_par)
print("A média é: ", media)