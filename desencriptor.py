
a = "pepperoni"
k = "pizza"

lista_a=[]
for letra in a:
    lista_a.append(letra)
    #print(lista_a)

lista_key = []
f = len(a)//len(k)
#print(f)

lis_a = []
for letra in k:
    lis_a.append(letra)
    #print(lis_a)

Li=lista_key+lis_a*(f+1)
#print(Li)

#suma
passes = []
nunu = []
for i in range(0,len(a)):
    num = ord(Li[i])+ord(lista_a[i])-97*2
    #print(ord(Li[i]),ord(lista_a[i]))
    nume = num % 26 + 97
    letr = chr(nume)
    nunu.append(nume-97)
    passes.append(letr)


print(passes)

    
    
