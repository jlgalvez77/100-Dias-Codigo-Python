import random
import string

print("🔐 Generador de Contraseñas Seguras (Avanzado) 🔐")

# Preguntar al usuario qué quiere incluir
usar_letras = input("¿Incluir letras? (s/n): ").lower() == "s"
usar_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

# Construir el conjunto de caracteres
caracteres = ""
if usar_letras:
    caracteres += string.ascii_letters
if usar_numeros:
    caracteres += string.digits
if usar_simbolos:
    caracteres += string.punctuation

# Verificar que haya al menos una opción seleccionada
if not caracteres:
    print("Debes elegir al menos un tipo de carácter. Intenta de nuevo.")
    exit()

# Pedir longitud
longitud = int(input("¿Cuántos caracteres quieres en tu contraseña?: "))

# Asegurarse de incluir al menos un carácter de cada tipo seleccionado
password = []

if usar_letras:
    password.append(random.choice(string.ascii_letters))
if usar_numeros:
    password.append(random.choice(string.digits))
if usar_simbolos:
    password.append(random.choice(string.punctuation))

# Completar el resto de la contraseña
while len(password) < longitud:
    password.append(random.choice(caracteres))

# Mezclar los caracteres para que no empiece siempre por letras/números/etc.
random.shuffle(password)

# Mostrar la contraseña final
print("Tu contraseña es:", "".join(password))