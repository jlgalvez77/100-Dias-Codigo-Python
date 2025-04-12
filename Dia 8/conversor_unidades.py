def menu_principal():
    print('''=== Conversor de Unidades ===
          1. Temperatura
          2. Distancia
          3. Peso
          4. Tamaño de Archivo
          5. Salir''')
    
def convertir_temperatura():
    print('\n=== Conversión de Temperatura ===')
    valor = float(input('Ingresa el valor: '))
    print('Unidades disponibles: Celsius, Fahrenheit, Kelvin')
    origen = input('Unidad de origen: ').lower()
    destino = input('Unida de destino: ').lower()

    if origen == 'celsius':
        if destino == 'fahrenheit':
            resultado = valor * 9/5 + 32
        elif destino == 'kelvin':
            resultado = valor + 273.15
        else:
            resultado = valor
    elif origen == 'fahrenheit':
        if destino == 'celsius':
            resultado = (valor - 32) * 9 / 5
        elif destino == 'kelvin':
            resultado = (valor - 32) * 9 / 5 + 273.15
        else:
            resultado = valor
    elif origen == 'kelvin':
        if destino == 'celsius':
            resultado = valor - 273.15
        elif destino == 'fahrenheit':
            resultado = (valor - 273.15) * 9 / 5 + 32
        else:
            resultado = valor
    else:
        print('Unidad no válida')
        return
    
    print(f'{valor} {origen} = {resultado:.2f} {destino}')

def convertir_distancia():
    print('\n === Conversión de Distancia ===')
    unidades = {
        'metro': 1,
        'kilometro': 1000,
        'milla': 1609.34,
        'pie': 0.3048
    }

    print('Unidades disponibles: metro, kilometro, milla y pie')
    valor = float(input('Ingresa el valor: '))
    origen = input('Unidad de origen: ').lower()
    destino = input('Unidad de destino: ').lower()

    if origen not in unidades or destino not in unidades:
        print('Unidad no válida')
        return
    
    # Convertimos a metros primero
    valor_en_metros = valor * unidades[origen]

    # Convertimos de metros a la unidad destino
    resultado = valor_en_metros / unidades[destino]

    print(f'{valor} {origen}(s) = {resultado:.4f} {destino}(s)')

def convertir_peso():
    print('\n === Conversión de Peso ===')
    unidades = {
        'kilogramo': 1,
        'gramo': 0.001,
        'libra': 0.453592,
        'onza': 0.0283495
    }

    print('Unidades disponibles: kilogramos, gramo, libra, onza')
    valor = float(input('Ingresa el valor: '))
    origen = input('Unidad de origen: ').lower()
    destino = input('Unidad de destino: ').lower()

    if origen not in unidades or destino not in unidades:
        print('Unidad no válida.')
        return
    
    # Convertir a kilogramos primero
    valor_en_kg = valor * unidades[origen]

    # Convertir de kilogramos a unidad destino
    resultado = valor_en_kg * unidades[destino]

    print(f"{valor} {origen}(s) = {resultado:.4f} {destino}(s)")

def convertir_archivos():
    print('\n === Conversión de Tamaño de Archivos ===')
    unidades = {
        "bit": 1 / 8,              # 1 byte = 8 bits
        "byte": 1,
        "kb": 1024,
        "mb": 1024**2,
        "gb": 1024**3,
        "tb": 1024**4
    }

    print("Unidades disponibles: bit, byte, kb, mb, gb, tb")
    valor = float(input("Ingresa el valor: "))
    origen = input("Unidad de origen: ").lower()
    destino = input("Unidad de destino: ").lower()

    if origen not in unidades or destino not in unidades:
        print("Unidad no válida.")
        return

    # Convertimos a bytes primero
    valor_en_bytes = valor * unidades[origen]

    # Convertimos de bytes a unidad destino
    resultado = valor_en_bytes / unidades[destino]

    print(f"{valor} {origen}(s) = {resultado:.4f} {destino}(s)")

def main():
    while True:
        menu_principal()
        opcion = input('Elige una opción (1-5): ')

        if opcion == '1':
            convertir_temperatura()
        elif opcion == '2':
            convertir_distancia()
        elif opcion == '3':
            convertir_peso()
        elif opcion == '4':
            convertir_archivos()
        elif opcion == '5':
            print('Saliendo...')
        else:
            print('Opción invalida.')

if __name__ == '__main__':
    main()