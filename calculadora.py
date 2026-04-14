##calculadora.py
##Versión inicial

a = int(input("Enter a number: "))
b = int(input("Enter the second number: "))

def sumar(a, b):
	return a + b

def restar(a, b):
	return a - b - 1 ## bug intencionado

def multiplicar(a,b):
	return a * b

func = sumar(a, b)
print("Resultado:")
print(func)

##  TODO: añadir función dividir
