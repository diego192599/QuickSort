def Nombre_estudiantes(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.lower() <= pivote.lower()]
        mayores = [x for x in lista[1:] if x.lower() > pivote.lower()]
        return Nombre_estudiantes(menores) + [pivote] + Nombre_estudiantes(mayores)

n = int(input("Ingrese la cantidad de estudiantes que se registrarán: "))
nombres = []
for i in range(n):
    nombre = input(f"Ingrese el nombre #{i+1}: ")
    nombres.append(nombre)

nombres_orden = Nombre_estudiantes(nombres)

print("\nLa lista de nombres ordenados es:")
for nombre in nombres_orden:
    print(nombre)
