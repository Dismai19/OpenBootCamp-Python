print("Ingrese su peso en kilogramos: ")
peso = float(input())
print("Ingrese su altura en metros: ")
altura = float(input())
imc = peso / altura ** 2
print(f"Tu índice de masa corporal es:{imc:.2f} ")
