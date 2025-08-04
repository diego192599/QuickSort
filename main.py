def Nombre_estudiantes(lista):
    if len(lista)<=1:
        return lista
    else:
        pivote=lista[0]
        menores=[x for x in lista[1:] if x.lower<=pivote.lower()]
        mayores=[x for x in lista[1:] if x.lower>pivote.lower()]
        return Nombre_estudiantes(menores)+pivote+Nombre_estudiantes(mayores)

