p=int(input('Ingrese un numero: '))
n=int(input('Ingrese otro numero: '))
 
def recur(n,p,acumulado):
  while n>0 :
    acumulado+=n*p
    n-=1
    recur(n,p,acumulado)
  return acumulado
 
print(recur(n,p,0))