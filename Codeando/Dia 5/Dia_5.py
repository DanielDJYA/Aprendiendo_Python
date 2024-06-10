from random import randint
def lanzar_dados():
    dado_1= randint(1,6)
    dado_2= randint(1,6)
    return dado_1,dado_2

def evaluar_jugada(r_dado_1,r_dado_2):
    suma= r_dado_1+ r_dado_2
    if suma <= 6:
        print(f"La suma de tus dados es {suma}. Lamentable")
    elif 6 < suma > 10:
        print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    else: 
        print(f"La suma de tus dados es {suma}. Excelente tieens buena suerte")

r_dado_1, r_dado_2= lanzar_dados()
print(f"el primer dado es: {r_dado_1}\nel segundo dado es: {r_dado_2}")
evaluar_jugada(r_dado_1,r_dado_2)
