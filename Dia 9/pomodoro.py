import tkinter as tk
import time
import threading
import platform

# Detectar plataforma para usar sonido
if platform.system() == "Windows":
    import winsound
    def reproducir_sonido():
        winsound.Beep(1000, 500)
else:
    def reproducir_sonido():
        print("\a")  # En sistemas Unix, suena beep en consola

# Configuración de tiempos (en segundos)
TIEMPO_TRABAJO = 25 * 60
TIEMPO_DESCANSO = 5 * 60

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temporizador Pomodoro")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.tiempo_restante = TIEMPO_TRABAJO
        self.en_descanso = False
        self.temporizador_activo = False

        self.label = tk.Label(root, text="25:00", font=("Helvetica", 36))
        self.label.pack(pady=20)

        self.estado_label = tk.Label(root, text="En trabajo", font=("Helvetica", 14))
        self.estado_label.pack()

        self.boton_inicio = tk.Button(root, text="Iniciar", command=self.iniciar_temporizador)
        self.boton_inicio.pack(pady=5)

        self.boton_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack()

    def actualizar_tiempo(self):
        minutos = self.tiempo_restante // 60
        segundos = self.tiempo_restante % 60
        self.label.config(text=f"{minutos:02}:{segundos:02}")

    def cuenta_regresiva(self):
        while self.temporizador_activo and self.tiempo_restante > 0:
            time.sleep(1)
            self.tiempo_restante -= 1
            self.root.after(0, self.actualizar_tiempo)

        if self.temporizador_activo:
            reproducir_sonido()
            self.en_descanso = not self.en_descanso
            self.tiempo_restante = TIEMPO_DESCANSO if self.en_descanso else TIEMPO_TRABAJO
            self.root.after(0, lambda: self.estado_label.config(
                text="Descanso" if self.en_descanso else "En trabajo"))
            self.root.after(0, self.actualizar_tiempo)
            self.cuenta_regresiva()

    def iniciar_temporizador(self):
        if not self.temporizador_activo:
            self.temporizador_activo = True
            threading.Thread(target=self.cuenta_regresiva, daemon=True).start()

    def reiniciar(self):
        self.temporizador_activo = False
        self.en_descanso = False
        self.tiempo_restante = TIEMPO_TRABAJO
        self.estado_label.config(text="En trabajo")
        self.actualizar_tiempo()

# Crear ventana
root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()
