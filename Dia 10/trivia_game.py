import requests
import random
import html

def obtener_preguntas(cantidad=5):
    url = f"https://opentdb.com/api.php?amount={cantidad}&type=multiple"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos['results']

def jugar_trivia():
    preguntas = obtener_preguntas()
    puntaje = 0

    for i, pregunta in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {html.unescape(pregunta['question'])}")
        opciones = pregunta['incorrect_answers'] + [pregunta['correct_answer']]
        opciones = [html.unescape(opcion) for opcion in opciones]
        random.shuffle(opciones)

        for idx, opcion in enumerate(opciones):
            print(f"{idx + 1}) {opcion}")

        try:
            eleccion = int(input("Tu respuesta (1-4): "))
            if opciones[eleccion - 1] == html.unescape(pregunta['correct_answer']):
                print("✅ ¡Correcto!")
                puntaje += 1
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {html.unescape(pregunta['correct_answer'])}")
        except:
            print("❌ Entrada no válida. Saltando pregunta.")

    print(f"\n🎉 Has terminado. Tu puntaje fue: {puntaje}/{len(preguntas)}")

if __name__ == "__main__":
    jugar_trivia()