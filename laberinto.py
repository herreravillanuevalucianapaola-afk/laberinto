import pygame

# ======================
# INICIALIZACIÓN
# ======================
pygame.init()

ANCHO = 700
ALTO = 500

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto - Un solo archivo")

####fondo####
fondo= pygame.transform.scale(pygame.image.load("laberinto\\fondo hola.jpg"), (ANCHO,ALTO))




RELOJ = pygame.time.Clock()
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 150, 255)
ROJO = (255, 80, 80)
VERDE = (80, 255, 120)



# ======================
# CLASE BASE
# ======================
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, color):
        super().__init__()

        # Creamos una superficie (rectángulo)
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(color)

        # Rectángulo para colisiones
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        ventana.blit(self.image, self.rect)

# ======================
# JUGADOR
# ======================
class Player(GameSprite):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40, AZUL)
        self.image =pygame.transform.scale(pygame.image.load("laberinto\holaaaa.png"), (40,40))
        self.vel_x = 0
        self.vel_y = 0

    def update(self, muros):
        # Movimiento horizontal
        self.rect.x += self.vel_x
        for muro in muros:
            if self.rect.colliderect(muro.rect):
                if self.vel_x > 0:
                    self.rect.right = muro.rect.left
                if self.vel_x < 0:
                    self.rect.left = muro.rect.right
# Movimiento vertical
        self.rect.y += self.vel_y
        for muro in muros:
            if self.rect.colliderect(muro.rect):
                if self.vel_y > 0:
                    self.rect.bottom = muro.rect.top
                if self.vel_y < 0:
                    self.rect.top = muro.rect.bottom

# ======================
# MUROS DEL LABERINTO
# ======================
class Muro(GameSprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto, NEGRO)
# ======================
# META
# ======================
class Meta(GameSprite):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40, AZUL)

# ======================
# CREACIÓN DE OBJETOS
# ======================
jugador=Player(50,50)
meta=Meta(620,420)

#creamos una lista
muros=[]
#bordes
muros.append(Muro(0,0,700,20))
muros.append(Muro(0,0,20,500))
muros.append(Muro(0,480,700,20))
muros.append(Muro(680,0,20,500))

#MUROS INTERNOS
muros.append(Muro(100,0,20,350))
muros.append(Muro(200,150,20,350))
muros.append(Muro(300,0,20,350))
muros.append(Muro(400,150,20,350))
muros.append(Muro(500,0,20,350))

pygame.mixer.music.load("laberinto/HOLAAAAA.mp3")
pygame.mixer.music.play()

winer_sound = pygame.mixer.Sound('laberinto\win.mp3')

#bucle principal
jugando=True
ganastes=False
while jugando:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            jugando = False
    teclas=pygame.key.get_pressed()        
    jugador.vel_x = 0
    jugador.vel_y = 0

    if teclas[pygame.K_a]:
        jugador.vel_x = -5
    if teclas[pygame.K_d]:
        jugador.vel_x = 5
    if teclas[pygame.K_w]:
        jugador.vel_y = -5
    if teclas[pygame.K_s]:
        jugador.vel_y = 5

    # Actualizamos jugador
    jugador.update(muros)

    # Verificamos victoria
    if jugador.rect.colliderect(meta.rect):
        winer_sound.play()
        ganaste = True
        jugando = False
# Dibujo
    ventana.blit(fondo,(0,0))
    for muro in muros:
        muro.draw()
    meta.draw()
    jugador.draw()

    pygame.display.update()
    RELOJ.tick(60)

# ======================
# PANTALLA FINAL
# ======================
ventana.blit(fondo,(0,0))
fuente = pygame.font.SysFont(None, 60)
if ganaste:
    texto = fuente.render("¡GANASTE!", True, VERDE)
else:
    texto = fuente.render("FIN DEL JUEGO", True, ROJO)

ventana.blit(texto, (220, 220))
pygame.display.update()

pygame.time.delay(3000)
pygame.quit()
