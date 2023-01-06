#Convertir un Número Entero a Cualquier Base Numérica,
#El programa debe pedir al usuario que ingrese un número n, y un número p,
def convertirDecimalBase(numero, base):
  representacion = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

  if (numero < base):
    respuesta = representacion[numero]
    print(respuesta)
    return respuesta

  respuesta=convertirDecimalBase(numero//base, base) + representacion[numero%base]
  print(respuesta)
  return respuesta
numero=int(input("Ingrese el número:"))
base=int(input("Ingrese la base:"))
convertirDecimalBase(numero,base)