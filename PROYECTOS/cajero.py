dinero  = [10,]

billetec_50 = 0
billetec_20 = 0
billetec_10 = 0
billetec_5 = 0

while True :
    valor = int(input("ingrese el valor que quiere retirar "))
    while valor > 50000 :
        billetec_50 = billetec_50 + 1
        valor = valor - 50000
    while valor < 50000 and valor >= 20000 :
        billetec_20 = billetec_20 + 1
        valor = valor - 20000
    while valor < 20000 and valor >= 10000:
        billetec_10 = billetec_10 + 1
        valor = valor - 10000
    while valor < 10000 and valor >= 5000:
        billetec_5 = billetec_5 + 1
        valor = valor -5000
    
    print("billetes de 50.000 ", billetec_50)
    print("billetes de 20.000 ", billetec_20)
    print("billetes de 10.000 ",billetec_10)
    print("billetes de 5.000 ",billetec_5)
    print("el valor que sobra es ", valor)



