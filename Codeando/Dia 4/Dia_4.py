from random import * 
aleatorio = randint(1,100)
print(aleatorio)

nombre = input("Ingrese su nombre: ")
print(f"Buno {nombre}, he pensado un número\n entre 1 y 100, y tienes solo ocho intentos\n para adivinar cuál crees que es el número")

intentos = 8
while intentos >=1:
    numero = int(input("Ingrese un Numero: "))

    if intentos == 1:
        print("Ops!! te quedaste sin intentos")
        break
    else:
        if (numero < 0) or (numero > 101):
            print("************************************")
            print("Numero Incorrecto")
            print("elija entre el [1 - 100]")
            print("************************************")
        else:
            if numero > aleatorio:
                print("El numero debe ser mas BAJO")
                print("************************************")
                intentos -= 1
            elif numero < aleatorio:
                print("El numero debe ser mas dALTO")
                print("************************************")
                intentos -= 1
            elif numero == aleatorio:
                print(f"Has Acertado el Numero era {aleatorio} ")
                print("************************************")
                break
    
    print(f"Te quedan {intentos} para adivinar")
    print("************************************")