def suma_lista(lista):
    suma = 0 
    for elementos in range(len(lista)):
        suma += lista[elementos]
    return suma 


list = [1, 22, 14, 4, 64, 7, 5]
resultado = suma_lista(list)
print(resultado)