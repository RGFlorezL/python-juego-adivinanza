import random

def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras líneas del juego donde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar el número entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    # Mueve el ciclo while dentro de la función
    while not adivinado:
        # Solicitar un número del 1 al 100
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Pasamos un texto a un entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(f"¡Felicitaciones has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos.")
                adivinado = True
        else:
            print("Por favor introduzca un número válido entre el 1 al 100")

# Llamar a la función para iniciar el juego
juego_adivinanza()
