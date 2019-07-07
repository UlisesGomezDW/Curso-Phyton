# Mi Primer cooigo en Phyton :D
codigo = "Hola Mundo"
print("Y yo digo "+codigo)
#Hay tres tipos de datos: Enteros, flotantes, complejos (Exactos) y booleanos
 
#Operaciones Basicas
Num_one = 10
Num_two = 4

result = Num_one + Num_two
print("La suma es: ",result)

result = Num_one - Num_two
print("La resta es: ",result)

result = Num_one * Num_two
print("La multiplicación es: ",result)

result = Num_one / Num_two
print("La división es: ",result) #Regresa un float 

result = Num_one // Num_two
print("La división entera es: ",result) #Regresa un entero (Porque es el cociente) 

result = Num_one ** Num_two
print("La exponencial es: ",result) #Regresa un exponencial


#Espacios 
print("_______")
new_text = "Hola \nesto es Phyton"
print(new_text)
print("_______") 

#Concatenar cadenas de caracteres 
name = "Ulises"
text="Phyton 3"
string = "Este es un texto escrito por "+name+" en "+text #1
print(string)
string = "Este es un texto escrito por %s en %s" %(name, text) #2
print(string)
string = "Este es un texto escrito por {} en {}" .format(name, text) #3
print(string)

#Strings como listas
list_text = "HOLA Phyton"
print(list_text[0]) #Imprime la posicion 0 de la lista de caracteres
print(list_text[1]) #Imprime la posicion 1 de la lista de caracteres
print(list_text[2]) #Imprime la posicion 2 de la lista de caracteres
print(list_text[3]) #Imprime la posicion 3 de la lista de caracteres
print(list_text[0:5]) #Imprime rango de lista de caracteres