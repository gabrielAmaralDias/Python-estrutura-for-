r = int(input('Diste a razão'))
p = int(input('Digite o primeiro termo:'))
n = int(input('Digite o numero de Termos'))
pa = [p + (n -1) *  r for n in range(1 , n + 1)] 
print(pa)
