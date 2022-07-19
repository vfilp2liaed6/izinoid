import pygame as py
import random


class bordeS(py.sprite.Sprite):
	def __init__(self, anchox, anchoy, enx, eny):
		super().__init__()
		self.image = py.Surface((anchox, anchoy))
		self.image.fill(gris)
		self.rect = self.image.get_rect()
		self.rect.x = enx
		self.rect.y = eny

class jugador(py.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = py.image.load("recursos/bolaceleste2.png").convert()
		self.image.set_colorkey(negro)
		self.rect = self.image.get_rect()
		self.radius = 30
		self.rect.centerx = ancho // 2
		self.rect.bottom = alto - 110
		self.velocidadx = 0
		self.velocidady = 0

	def update(self):
		
		keystate = py.key.get_pressed()
		if keystate[py.K_SPACE]:
			a, b = py.mouse.get_pos()
			tempx = (a - 300) // 100
			tempy = (b - 800) // 100
			self.velocidadx = tempx
			self.velocidady = tempy

		self.rect.x += self.velocidadx 
		self.rect.y += self.velocidady

		if self.rect.right > 691 or self.rect.left < 111:
			self.velocidadx *= -1
		if self.rect.y < 111:
			self.velocidady *= -1
		if self.rect.bottom > 750 :
			self.kill
			self.rect.centerx = ancho // 2
			self.rect.bottom = alto - 110
			self.velocidadx = 0
			self.velocidady = 0
		#if self.rect.top

class bloqueS(py.sprite.Sprite):
	def __init__(self, posicionx, restablecer):
		super().__init__()
		self.image = py.Surface((70, 30))
		self.image.fill(celeste)
		self.rect = self.image.get_rect()
		self.rect.x = posicionx #ancho - self.rect.width)
		self.rect.y = restablecer
		self.velocidady = 0

	def update(self):
		if player.rect.y > 720:
			self.velocidady = 35
			self.rect.y += self.velocidady
		if self.rect.bottom > 650:
			self.rect.kill()

ancho = 800
alto = 800

negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
azul = (0, 0, 230)
gris = (128, 128, 128)
celeste = (12, 183, 242)

letras = py.font.match_font('consolas')#curier
letras2 = py.font.match_font('curier')
py.mixer.init()
py.mixer.Sound('recursos/colision.wav')
sonidoColision = py.mixer.Sound('recursos/colision.wav')



def textO(pantalla, letras, texto, color, dimensiones ,x ,y):
	tipoLetra = py.font.Font(letras, dimensiones)
	superficie = tipoLetra.render(texto, True, color) #antialised true
	rectangulo = superficie.get_rect()
	rectangulo.center = (x, y)
	pantalla.blit(superficie, rectangulo)

temp = 110
temp1 = 110
py.init()
pantalla = py.display.set_mode((ancho, alto))
py.display.set_caption("IZINOID")
clock = py.time.Clock()
py.mouse.set_visible(1)

posicionx, posiciony = (400,590)

puntuacion = 0

jugar = py.sprite.Group()
bloquess = py.sprite.Group()
bordes = py.sprite.Group()

player = jugador()
jugar.add(player)

bor = bordeS(10,500, 100, 100)
jugar.add(bor)
bor = bordeS(10,500, 700, 100)
jugar.add(bor)
bor = bordeS(600,10, 100, 100)
jugar.add(bor)

for i in range(random.randrange(1, 3)):
	temp = temp1

	if temp < 620:
		posx =random.randrange(temp , 620)
		bloq = bloqueS(posx, restablecer=110)
		#jugar.add(bloq)
		bloquess.add(bloq)
		temp1 = posx+70
	

running = True
while running:

	clock.tick(60)
	for event in py.event.get():
		if event.type == py.QUIT:
			running = False

	colision =py.sprite.spritecollide(player, bloquess, True)
	if colision:
		sonidoColision.play()
		puntuacion +=1


	if player.rect.y > 720:
		temp1 = 110
		for i in range(random.randrange(1, 3)):
			temp = temp1

			if temp < 620:
				posx =random.randrange(temp , 620)
				bloq = bloqueS(posx, restablecer=110)
				#jugar.add(bloq)
				bloquess.add(bloq)
				temp1 = posx+70
	
	jugar.update()
	bloquess.update()
	#pantalla
	pantalla.fill(blanco)
	jugar.draw(pantalla)
	bloquess.draw(pantalla)
	textO(pantalla, letras2, "IZINOID", negro, 60, 400, 40)
	textO(pantalla, letras, "puntuacion:", rojo, 30, 590, 80)
	textO(pantalla, letras, str(puntuacion), negro, 30, 700, 80)
	py.display.flip()


py.quit()