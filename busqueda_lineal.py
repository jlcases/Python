import random


def busqueda_lineal (lista,objetivo):
    match = False
    for elemento in lista: # O(n)
        if elemento==objetivo:
            match=True
            break
    
    return match


if __name__ == '__main__':
    tamamo_de_lista = int(input('De que tamaño será la lista'))
    objetivo = int(input('Que numero quieres encontrar?'))

    lista=[random.randint(0,100) for i in range (tamamo_de_lista)]
    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'el elemento {objetivo} {"está" if encontrado else "no está"}')
