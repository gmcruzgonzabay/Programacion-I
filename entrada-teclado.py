#Ingreso por teclado
#Trabajo autonomo, revisar como evitar si el usuario ingresa texto no se caiga o entre
#en un error el sistema
#strip elimina espacios
# upper convierte todo a mayusculas, lower(), upper(), capitalize(), title(),

nombre= input("Ingrese su nombre:").strip().capitalize()
edad= int(input("Ingrese su edad:"))
precio= float(input("Ingrese el precio:"))

#La f antes de las comillas permite insertar variables directamente
#en una cadena de texto, f(cadena formateada)
print(f"Hola {nombre}, tienes {edad} años")

#print("Hola", nombre)
#print("Su edad es: ",edad)

#Convertir en mayusculas


