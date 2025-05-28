opcion = True
longitud = None
contador = None
lista_digitos = []
impares = []
pares = []
suma = None
numero1 = None

while opcion:
   print("INGRESE LA OPCION QUE USTED DESEA:")
   print("1. INGRESE EL NUMERO QUE  DESEA EVALUAR")
   print("2. LONGITUD DEL NUMERO QUE ACABO DE INGRESAR")
   print("3. SUMA DE LOS DIGITOS DEL NUMERO QUE ACABO DE INGRESAR")
   print("4. CANTIDAD DE PARES DEL NUMERO QUE ACABO  DE INGRESAR")
   print("5. CANTIDAD DE IMPARES DEL NUMERO QUE ACABO  DE INGRESAR")
   print("0. DESEA SALIR:")
   contador = int(input("INGRESE SU OPCION \n"))

   while contador > 5 or contador < 0:
     contador = int(input("INGRESE SU OPCION YA QUE LA QUE INGRESO NO ES VALIDA \n "))
   
   if contador == 1:
      numero = int(input("INGRESE EL NUMERO \n "))
      numero_str = str(numero)
      longitud = len(numero_str)
      while longitud < 4:
        numero = int(input("RECUERDA EU EL NUMERO TIENE QUE SER MAYOR O IGUAL A 4 DIGITOS \n "))
        numero_str = str(numero)
        longitud = len(numero_str)

   elif contador == 2:
      print(f" LA LONGITUD DEL NUMERO ES \n {longitud}  \n ")

   elif contador == 3:
      lista_digitos = []
      for digito in numero_str:
       lista_digitos.append(int(digito))
      suma = sum(lista_digitos)
      print(f"LOS NUMERO SON : \n {lista_digitos} \n ")
      print(f"LA SUMA ES : \n {suma}  \n")

   elif contador == 4:
      pares = []
      for numero1 in lista_digitos:
         if numero1 % 2 == 0:
          pares.append(numero1)
          numero_pares = len(pares)
      print(f" NUMEROS DE PARES SON : \n {numero_pares} \n ")
      print(f"LOS NUMEROS SON: \n {pares} \n ")
   elif contador == 5:
      impares = []
      for numero1 in lista_digitos:
         if numero1 % 2 != 0:
          impares.append(numero1)
          numero_impares = len(impares)
      print(f" NUMEROS DE IMPARES SON :  \n{numero_impares} ")
      print(f"LOS NUMEROS SON: \n {impares} ")
   elif contador == 0:
     break
print(" TE ACABAS DE SALIR DEL PROGRAMA \n ")