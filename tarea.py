name=input("pon esta palabra electroencefalografistaelectroencefalografiaelectroenceflograma")

lista=list(name)

lista=list(set(lista))

lista.sort

inverse_list= lista[::-1]
print("inverse list", inverse_list)

odd=[lista[i] for i in range (len(lista)) if i % 2!=0 ]
print("letras in position odd", odd)

for i in range (0,len(lista),2):
    lista[i]="*"

lista = lista[:-2]
lista.sort()
print("Final result", lista)