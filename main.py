#Calculadora Básica en Python
print("Calculadora Básica en Python")

#Entrada de datos
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

#Selección de la operacion
print("Selecciona una operación")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion= input("Introduce el número de la operación que deseas realizar")

#Operaciones

if opcion=="1":
    print("La suma de",numr1."+",num2,"es igual a".num1+num2)
elif opcion=="2":
    print("La resta de",num1,"-",num2,"es igual a",num1-num2)
elif opcion=="3":
    print("La multiplicación de",num1,"*",num2,"es igual a",num1*num2)
elif opcion=="4":
    print("La división de",num1,"/",num2,"es igual a",num1/num2)
    else:
        print("Error: Introduce un número válido")
    