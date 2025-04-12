import random
from datetime import datetime

# Archivo para registrar partidas
HISTORIAL = 'historial_adivina_numero.txt'

# Estadisticas
partidas_jugadas = 0
partidas_ganadas = 0

def registrar_partida(resultado, numero_secreto, dificultad, intetos_usados):
    with open(HISTORIAL, 'a') as file:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f'{fecha} - Resultado: {resultado}, Número secreto: {numero_secreto}, Dificultad: {dificultad}, Intentos usados: {intetos_usados}')

def jugar():
    global partidas_jugadas, partidas_ganadas

    print('Bienvenido al juego Adivina el Número')
    print('Elige dificultad: fácil, medio, dificil')
    dificultad = input('Dificultad: ').lower()

    if dificultad == "fácil":
        max_num = 10
        intentos = 5
    elif dificultad == 'medio':
        max_num = 50
        intentos = 7
    elif dificultad == 'dificil':
        max_num = 100
        intentos = 10
    else:
        print('Error al seleccionar dificultad, prueba de nuevo')
        return
    
    secreto = random.randint(1, max_num)
    print(f'\nAdivina el número del 1 al {max_num}. Tienes {intentos} intentos.\n')

    partidas_jugadas += 1
    for intento_num in range(1, intentos + 1):
        try:
            intento = int(input(f'Intento {intento_num}: '))
        except ValueError:
            print('Ingresa un número valido')
            continue

        if intento == secreto:
            print('Felicidades! Has adivinado el número')
            partidas_ganadas += 1
            registrar_partida('Ganada', secreto, dificultad, intento_num)
            break
        elif intento < secreto:
            print('El número es más alto')
        else:
            print('El número es más bajo')
    else:
        print(f'Se acabaron los intentos. El número era: {secreto}')
        registrar_partida('Perdida', secreto, dificultad, intentos)

while True:
    jugar()
    print(f'\n Estadísticas: {partidas_ganadas} ganadas / {partidas_jugadas} jugadas')
    jugar_de_nuevo = input('\n¿Quieres jugar de nuevo? (si/no)').lower()
    if jugar_de_nuevo != 'si':
        print('Gracias por jugar')
        break