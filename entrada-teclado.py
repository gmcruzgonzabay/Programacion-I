#Ingreso por teclado
#Trabajo autonomo, revisar como evitar si el usuario ingresa texto no se caiga o entre
#en un error el sistema
#strip elimina espacios
# upper convierte todo a mayusculas, lower(), upper(), capitalize(), title(),
#la longitud len()

nombre= input("Ingrese su nombre:").capitalize().strip()
edad= int(input("Ingrese su edad:").lower().strip())
precio= float(input("Ingrese el precio:"))

#La f antes de las comillas permite insertar variables directamente
#en una cadena de texto, f(cadena formateada)
print(f"Hola {nombre}, tienes {edad} años")
#print(edad.upper()) esta linea da error

print("Longitud de nombre", len(nombre))

#print("Hola", nombre)
#print("Su edad es: ",edad)

#Convertir en mayusculas

#Condicionales simplres
if edad >= 18:
    print("Es mayor de dedad")
else:
    print("Es menor de edad")

#= asogna un valor, == compara 2 valores, : indica el inicio de un bloque, identacion(sangria o espaciado), dentro de python no se usan llaves

#Estructuras repetitivas
for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

#
frutas=["Manzana", "Pera", "Uva"]
for fruta in frutas:
    print(fruta)

#Incremento de 2 en 2
for  i in range(0,11,2):
    print(i)

# i=0 esto me hace un ciclo infinito
#while i < 5:
#    print(i)

i= 0
while i<5:
    print(i)
    i=i+1  
    #break 

