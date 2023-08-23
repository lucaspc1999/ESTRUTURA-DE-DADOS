num_par=[]
num_impar=[]

num=int(input("Insira um número: "))

for i in range(num+1):
    teste=i

    if teste%2==0:
        num_par.append(teste)
    else:
        num_impar.append(teste)

print(num_par)