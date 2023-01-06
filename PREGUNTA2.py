#Implemente un programa para convertir un número decimal a hexadecimal
#ejm. el número 8642 en forma hexadecimal es: 21C2
def convertirDecimalHexadecimal(numero):
  dic_val = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

  if (numero < 16):
    return dic_val[numero]

  respuesta = convertirDecimalHexadecimal(numero//16) + dic_val[numero%16]
  print(respuesta)
  return respuesta

convertirDecimalHexadecimal(8642)