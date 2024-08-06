import cusuario

print("bienvenidos a la biblioteca")
pregunta1 = input("¿desea retirar un libro? (si/no): ").lower()
if pregunta1 == "si":
    cusuario.usuario()
    cusuario.retiro()
elif pregunta1 == "no":
    print ("ok adios")