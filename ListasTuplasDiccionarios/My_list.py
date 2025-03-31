my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
print(my_lista)
print(type(my_lista))
print(my_lista[0])

print("my_lista size: ", len(my_lista))
print(my_lista[1:2])
print(my_lista[4:6])
#Preguntar que valor es dado para cada elemento cuando se piden varios valores

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro')
print(my_lista)

my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)

print(my_lista.index('Rojo')) #Index: Nos informa cual valor corresponde a el objeto en la lista Ej: Azul es 1 y Rojo es 0

my_lista.remove('Marron')
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

print(my_lista.pop())
size = len(my_lista)
print("size = ", size)
