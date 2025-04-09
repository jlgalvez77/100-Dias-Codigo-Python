

peso = int(input('Ingresa tu peso en kg: '))
altura = float(input('Ingresa tu altura en mwtros: '))

imc = peso / altura**2

print(f'Tu IMC es: {imc:.2f}')

if imc < 18.5:
    print('Tu peso es bajo')
elif imc >= 18.5 and imc < 25:
    print('Tu peso es normal')
elif imc >= 25 and imc < 30:
    print('Tienes sobrepeso')
elif imc > 30:
    print('Tienes obesidad')