import random

print('*** Juego de Adivinar el número ***')

intentos = 6
numero_secreto = random.randint(1, 100)
print('*** Tienes que adivinar un número entre el 1 y el 1oo ***')

while intentos > 0:
    numero_jugador = int(input('¿Cual es el número secreto?: '))
    intentos -= 1
    if numero_jugador == numero_secreto:
        print(f'Felicidades has adivinado el número secreto con {intentos} intentos restates')
        break
    if numero_jugador > numero_secreto:
        print('El número secreto es menor')
    if numero_jugador < numero_secreto:
        print('El número secreto es mayor')
if intentos == 0 and numero_jugador != numero_secreto:
    print(f'Has agotado los intentos, el número era {numero_secreto}')