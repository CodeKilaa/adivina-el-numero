import random


def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("🎯 ¡Adivina el número!")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        entrada = input("Tu número: ").strip()

        if entrada.lower() == "salir":
            print(f"El número era {numero_secreto}. ¡Hasta luego!")
            break

        try:
            numero = int(entrada)
        except ValueError:
            print("Introduce un número entero.")
            continue

        if not 1 <= numero <= 100:
            print("El número debe estar entre 1 y 100.")
            continue

        intentos += 1

        if numero < numero_secreto:
            print("El número secreto es mayor.")
        elif numero > numero_secreto:
            print("El número secreto es menor.")
        else:
            print(f"¡Acertaste! Lo lograste en {intentos} intentos.")
            break


if __name__ == "__main__":
    jugar()