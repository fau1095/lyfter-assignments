nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

if 0 < edad < 4:
    print(f"Usted es un bebé")
elif 4 <= edad < 12:
    print(f"Usted es un niño")
elif 12 <= edad < 14:
    print(f"Usted es un preadolescente")    
elif 14 <= edad < 18:
    print(f"Usted es un adolescente")
elif edad >= 18:
    print(f"Usted es un adulto")
    
print(f"Su edad es: {edad} y su nombre es: {nombre} {apellido}")