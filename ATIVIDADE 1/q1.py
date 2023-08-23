numeros=[]

for i in range(3):
    num=float(input("Digite um número: "))
    numeros.append(num)

media=float(sum(numeros)/len(numeros))
print(f"A média dos números inseridos é: {media}")
