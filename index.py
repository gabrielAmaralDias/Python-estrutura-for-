ns = int(input('Digite um Numero'))
numb = int(input('Qual tabuada voce deseja executar?'))
lista = []
for num in range (0 , 11):
    print('{} X {} = {}'.format(numb, num ,numb*num))
for n in range(1,ns , 2 ):
   
    if  n % 3 == 0   :
        lista.append(n)   
print('A Soma dos pares deu {}'.format(sum(lista)))
print(lista)
print(len(lista))