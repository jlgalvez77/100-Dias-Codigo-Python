import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🎮 Pong - Día 3")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Paletas
PAL_ANCHO, PAL_ALTO = 10, 100
jugador = pygame.Rect(20, ALTO//2 - PAL_ALTO//2, PAL_ANCHO, PAL_ALTO)
oponente = pygame.Rect(ANCHO - 30, ALTO//2 - PAL_ALTO//2, PAL_ANCHO, PAL_ALTO)

# Pelota
pelota = pygame.Rect(ANCHO//2 - 15, ALTO//2 - 15, 30, 30)
velocidad_pelota = [7, 7]

# Reloj para FPS
reloj = pygame.time.Clock()

# Puntuación
puntos_jugador = 0
puntos_oponente = 0

# Fuente
fuente = pygame.font.Font(None, 50)  # Fuente por defecto, tamaño 50

# Puntuaje para ganar el juego
PUNTAJE_MAX = 5

# Movimiento del jugador
vel_jugador = 0

def mover_oponente():
    if oponente.centery < pelota.centery:
        oponente.y += 6
    elif oponente.centery > pelota.centery:
        oponente.y -= 6

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                vel_jugador = -10
            if evento.key == pygame.K_DOWN:
                vel_jugador = 10
        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_UP, pygame.K_DOWN):
                vel_jugador = 0

    jugador.y += vel_jugador
    jugador.clamp_ip(VENTANA.get_rect())  # No salir de pantalla

    mover_oponente()

    # Movimiento de la pelota
    pelota.x += velocidad_pelota[0]
    pelota.y += velocidad_pelota[1]

    # Colisiones
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        velocidad_pelota[1] *= -1
    if pelota.colliderect(jugador) or pelota.colliderect(oponente):
        velocidad_pelota[0] *= -1

# Comprobar si alguien anotó
    if pelota.left <= 0:
        puntos_oponente += 1
        pelota.center = (ANCHO // 2, ALTO // 2)
        velocidad_pelota[0] *= -1
        velocidad_pelota[1] *= random.choice([-1, 1])
        pygame.time.delay(500)

    if pelota.right >= ANCHO:
        puntos_jugador += 1
        pelota.center = (ANCHO // 2, ALTO // 2)
        velocidad_pelota[0] *= -1
        velocidad_pelota[1] *= random.choice([-1, 1])
        pygame.time.delay(500)

    # 🔽 AQUÍ pega el bloque de verificación de Game Over
    if puntos_jugador == PUNTAJE_MAX or puntos_oponente == PUNTAJE_MAX:
        ganador = "¡Ganaste! 🏆" if puntos_jugador == PUNTAJE_MAX else "Perdiste 😢"
        
        texto_game_over = fuente.render(ganador, True, BLANCO)
        texto_reiniciar = fuente.render("Presiona R para reiniciar o ESC para salir", True, BLANCO)
        
        VENTANA.blit(texto_game_over, (ANCHO // 2 - texto_game_over.get_width() // 2, ALTO // 2 - 40))
        VENTANA.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 20))
        pygame.display.flip()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        puntos_jugador = 0
                        puntos_oponente = 0
                        pelota.center = (ANCHO // 2, ALTO // 2)
                        velocidad_pelota[0] *= random.choice([-1, 1])
                        velocidad_pelota[1] *= random.choice([-1, 1])
                        esperando = False
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()


    

    # Dibujar elementos
    VENTANA.fill(NEGRO)
    pygame.draw.rect(VENTANA, BLANCO, jugador)
    pygame.draw.rect(VENTANA, BLANCO, oponente)
    pygame.draw.ellipse(VENTANA, BLANCO, pelota)
    pygame.draw.aaline(VENTANA, BLANCO, (ANCHO//2, 0), (ANCHO//2, ALTO))

    marcador = fuente.render(f"{puntos_jugador}  -  {puntos_oponente}", True, BLANCO)
    VENTANA.blit(marcador, (ANCHO // 2 - marcador.get_width() // 2, 20))

    pygame.display.flip()
    reloj.tick(60)
