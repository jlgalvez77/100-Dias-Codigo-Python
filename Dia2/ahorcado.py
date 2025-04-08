import random

def obtener_palabra():
    palabras = ["python", "juego", "ahorcado", "codigo", "desarrollador"]
    return random.choice(palabras)

def mostrar_ahorcado(intentos):
    estados = [
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |    
         |
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |    
         |
        """,
        """
         ------
         |    |
         |    O
         |    |
         |    
         |
        """,
        """
         ------
         |    |
         |    O
         |    
         |    
         |
        """,
        """
         ------
         |    |
         |    
         |    
         |    
         |
        """
    ]
    return estados[6 - intentos]

def jugar():
    palabra = obtener_palabra()
    letras_adivinadas = []
    intentos = 6
    print("🎮 ¡Bienvenido al Ahorcado Avanzado!")

    while intentos > 0:
        print(mostrar_ahorcado(intentos))

        mostrar = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print("Palabra:", " ".join(mostrar))

        if "_" not in mostrar:
            print("🏆 ¡Ganaste! La palabra era:", palabra)
            break

        letra = input("Adivina una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("❗ Ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("🔁 Ya intentaste con esa letra.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra:
            intentos -= 1
            print(f"❌ Incorrecto. Te quedan {intentos} intentos.")

    else:
        print(mostrar_ahorcado(intentos))
        print("😢 ¡Perdiste! La palabra era:", palabra)

def main():
    while True:
        jugar()
        reiniciar = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if reiniciar != "s":
            print("¡Gracias por jugar! 👋")
            break

if __name__ == "__main__":
    main()
