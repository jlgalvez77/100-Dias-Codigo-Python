
tareas = []

while True:
    print('''--- Organizador de Tareas ---
          1.- Ver Tareas
          2.- Agregar Tarea
          3.- Eliminar Tarea
          4.- Salir''')
    seleccion = int(input('Selecciona una opción: '))

    if seleccion == 1:
        if not tareas:
            print('No hay tareas aún')
        else:
            for i, tarea in enumerate(tareas, start=1):
                print(f'{i} - {tarea}')
    elif seleccion == 2:
        agregar_tarea = input('Ingresa la tarea a agregar: ')
        tareas.append(agregar_tarea)
        print('Tarea agregada')
    elif seleccion == 3:
        if not tareas:
            print('No hay tareas para eliminar')
        else:
            for i, tarea in enumerate(tareas, start=1):
                print(f'{i} - {tarea}')
            try:
                indice = int(input('Escribe elnúmero de la tarea a eliminar'))
                if 1 <= indice <= len(tareas):
                    tarea_eliminada = tareas.pop(indice -1)
                    print(f'Tarea {tarea_eliminada} eliminada')
                else:
                    print('Número inválido')
            except ValueError:
                print('Escribe un número valido')
    elif seleccion == 4:
        print('Saliendo...')
        break
    else:
        print('Opción no valida')