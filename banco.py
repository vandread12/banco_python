menu = """"
[d] Depositar
[s] Sacar
[e] Extracto
[q] Salir

=> """

saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUES = 3


while True:
    opcion = input(menu)
    if opcion == "d":
        deposito = float(input("Ingrese el monto a depositar: "))
        saldo += deposito
        print(f"Su saldo actual es: {saldo}")
    elif opcion == "s":
        if numero_saque == LIMITE_SAQUES:
            print("Ha superado el limite de saques")
            continue
        saque = float(input("Ingrese el monto a sacar: "))
        if saque > saldo + limite:
            print("No puede sacar esa cantidad")
            continue
        saldo -= saque
        numero_saque += 1
        print(f"Su saldo actual es: {saldo}")
    elif opcion == "e":
        print(f"Su saldo actual es: {saldo}")
    elif opcion == "q":
        break
    else:
        print("Opcion invalida")
print("Gracias por utilizar nuestros servicios")
