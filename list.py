#Aqui vamos a trabajar con Listas

#Lista de frutas
frutas=["Manzanas","Pera","Uva"]
print(frutas)
numeros=[10,20,30,40,True]
print(numeros)

#acceder a un elemento de la lista
print(frutas[0])
print(frutas[1])
print(frutas[2])
#print(frutas[3]) aqui me genera un IndexError

print(numeros[4])

#Agregar Elementos
frutas.append("Banana") #Agrega al final de la lista
print(frutas)

frutas.insert(1,"Mango") #Insertar en una posicion especifica
print(frutas)

#Modificar un elemento
frutas[0]="Sandias"
print(frutas)

#Eliminar Elemento
frutas.remove("Sandias") #Indicando el valor
print(frutas)

frutas.pop(2) #Eliminar por posicion
print(frutas)



