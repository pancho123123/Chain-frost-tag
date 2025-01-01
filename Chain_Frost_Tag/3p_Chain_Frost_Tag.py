import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chain Frost Tag")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 7
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def distance(a,b):
	#pitagoras distancia entre a y b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#vector unitario desde a a b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/terrorblade.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.hp = 1000
		self.counter = True

class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y = 133

	def update(self):
		self.hp += 0.04
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 1000:
			self.hp = 1000
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -3
		if keystate[pygame.K_d]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -3
		if keystate[pygame.K_s]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 900
		self.rect.y = 133
				
	def update(self):
		self.hp += 0.04
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 1000:
			self.hp = 1000
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -3
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -3
		if keystate[pygame.K_DOWN]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Player3(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y =  366
			
	def update(self):
		self.hp += 0.04
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 1000:
			self.hp = 1000
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			self.speed_x = -3
		if keystate[pygame.K_h]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_t]:
			self.speed_y = -3
		if keystate[pygame.K_g]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Penguin(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/penguin.png").convert(),(65,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(300,1000)
		self.rect.y = random.randrange(200,650)
		self.speedx = randint(-1,1)
		self.speedy = randint(-1,1)
		self.hp = 100
		self.a = randint(1000,3000)
		self.b = randint(1000,3000)
		self.counter = True
		self.counter1 = True
		self.counter2 = False
		self.counter3 = False
		self.start_time = pygame.time.get_ticks()
		
	def update(self):
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time
		alist = [-1,1]
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 200:
			self.rect.top = 200
		if self.rect.bottom > 600:
			self.rect.bottom = 600
		if self.counter1:
			self.counter1 = False
			self.counter2 = True
			self.a = randint(1000,3000)
			self.b = randint(1000,3000)
			self.start_time = pygame.time.get_ticks()
		
		elif self.counter2:
			if elapsed_time >= self.a:
				self.counter2 = False
				self.speedx = random.choice(alist)
				self.speedy = random.choice(alist)
				self.counter3 = True
				self.start_time = pygame.time.get_ticks()
		elif self.counter3:
			if elapsed_time >= self.b:
				self.counter3 = False
				self.speedx = 0
				self.speedy = 0
				self.counter1 = True
				self.start_time = pygame.time.get_ticks()

class Penguin1(Penguin):
	def __init__(self):
		super().__init__()
		
class Penguin2(Penguin):
	def __init__(self):
		super().__init__()
		
class Penguin3(Penguin):
	def __init__(self):
		super().__init__()
		
class Penguin4(Penguin):
	def __init__(self):
		super().__init__()
		
class Penguin5(Penguin):
	def __init__(self):
		super().__init__()
		
class Penguin6(Penguin):
	def __init__(self):
		super().__init__()
		
class Penguin7(Penguin):
	def __init__(self):
		super().__init__()

class Penguin8(Penguin):
	def __init__(self):
		super().__init__()
		
class Penguin9(Penguin):
	def __init__(self):
		super().__init__()
		
class Frost1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = frost_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 700
		self.rect.centery = 266
		self.speed = 4
		self.target = None
		self.hit = True

	def update(self):
		if self.hit:
			target_list = [player1, player2, player3, penguin1, penguin2, penguin3, 
			penguin4, penguin5, penguin6, penguin7, penguin8, penguin9]
			target_list = [t for t in target_list if t.hp >0 and t is not self.target]
			distance_list = [(distance(self,t),t) for t in target_list]
			if len(distance_list)==0:
				distance_list=[(0,self.target)]
			self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
			self.hit = False

		if (self.target.rect.centerx - self.rect.centerx) == 0:
			if self.target.rect.centery > self.rect.centery:
				self.rect.centery += self.speed 
			elif self.rect.centery > self.target.rect.centery:
				self.rect.centery -= self.speed
			else:
				self.rect.centery += 0
		elif (self.target.rect.centerx - self.rect.centerx) != 0:
			x,y = direction(self, self.target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y

def show_go_screen():
	
	screen.fill(BLACK)
	draw_text1(screen, "Chain Frost Tag", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Avoid the Lich's Chain Frosts ", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
		
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False


frost_images = []
frost_list = ["img/2.png", "img/3.png", "img/4.png" ,"img/5.png", "img/6.png", "img/7.png"]
for img in frost_list:
	frost_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(25,30)))


def show_game_over_screenp1():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp3():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 3 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(), (1300,700))

game_over1 = False
game_over2 = False
game_over3 = False
running = True
start = True
while running:
	if game_over1:

		show_game_over_screenp1()
				
		screen.blit(background,(0,0))
		game_over1 = False
				
		all_sprites = pygame.sprite.Group()
		frost_list = pygame.sprite.Group()
		penguin1 = Penguin1()
		penguin2 = Penguin2()
		penguin3 = Penguin3()
		penguin4 = Penguin4()
		penguin5 = Penguin5()
		penguin6 = Penguin6()
		penguin7 = Penguin7()
		penguin8 = Penguin8()
		penguin9 = Penguin9()
		all_sprites.add(penguin1, penguin2, penguin3, penguin4, penguin5, penguin6, penguin7, penguin8, penguin9)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)
		
		frost1 = Frost1()
		all_sprites.add(frost1)
		frost_list.add(frost1)
		start_time = pygame.time.get_ticks()

	elif game_over2:

		show_game_over_screenp2()
				
		screen.blit(background,(0,0))
		game_over2 = False
		all_sprites = pygame.sprite.Group()
		frost_list = pygame.sprite.Group()
		penguin1 = Penguin1()
		penguin2 = Penguin2()
		penguin3 = Penguin3()
		penguin4 = Penguin4()
		penguin5 = Penguin5()
		penguin6 = Penguin6()
		penguin7 = Penguin7()
		penguin8 = Penguin8()
		penguin9 = Penguin9()
		all_sprites.add(penguin1, penguin2, penguin3, penguin4, penguin5, penguin6, penguin7, penguin8, penguin9)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)
		
		frost1 = Frost1()
		all_sprites.add(frost1)
		frost_list.add(frost1)
		start_time = pygame.time.get_ticks()

	elif game_over3:

		show_game_over_screenp3()
				
		screen.blit(background,(0,0))
		game_over3 = False
		all_sprites = pygame.sprite.Group()
		frost_list = pygame.sprite.Group()
		penguin1 = Penguin1()
		penguin2 = Penguin2()
		penguin3 = Penguin3()
		penguin4 = Penguin4()
		penguin5 = Penguin5()
		penguin6 = Penguin6()
		penguin7 = Penguin7()
		penguin8 = Penguin8()
		penguin9 = Penguin9()
		all_sprites.add(penguin1, penguin2, penguin3, penguin4, penguin5, penguin6, penguin7, penguin8, penguin9)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)
		
		frost1 = Frost1()
		all_sprites.add(frost1)
		frost_list.add(frost1)
		start_time = pygame.time.get_ticks()

	elif start:
		show_go_screen()
		
		start = False
		
		screen.blit(background,(0,0))
		all_sprites = pygame.sprite.Group()
		frost_list = pygame.sprite.Group()
		penguin1 = Penguin1()
		penguin2 = Penguin2()
		penguin3 = Penguin3()
		penguin4 = Penguin4()
		penguin5 = Penguin5()
		penguin6 = Penguin6()
		penguin7 = Penguin7()
		penguin8 = Penguin8()
		penguin9 = Penguin9()
		all_sprites.add(penguin1, penguin2, penguin3, penguin4, penguin5, penguin6, penguin7, penguin8, penguin9)
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)
				
		frost1 = Frost1()
		all_sprites.add(frost1)
		frost_list.add(frost1)
		start_time = pygame.time.get_ticks()
		
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	now = (pygame.time.get_ticks() - start_time)//1000
		
	if player1.hp <= 0 and player2.hp <= 0:
		game_over3 = True
	if player2.hp <= 0 and player3.hp <= 0:
		game_over1 = True
	if player1.hp <= 0 and player3.hp <= 0:
		game_over2 = True
	all_sprites.update()
		
	# Checar colisiones - penguin1 - frost
	hits = pygame.sprite.spritecollide(penguin1, frost_list, False)
	for hit in hits:
		if frost1.target == penguin1:
			penguin1.counter = False
			penguin1.hp -= 34
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True
			
	# Checar colisiones - penguin2 - frost
	hits = pygame.sprite.spritecollide(penguin2, frost_list, False)
	for hit in hits:
		if frost1.target == penguin2:
			penguin2.counter = False
			penguin2.hp -= 34
			penguin1.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True

	# Checar colisiones - penguin3 - frost
	hits = pygame.sprite.spritecollide(penguin3, frost_list, False)
	for hit in hits:
		if frost1.target == penguin3:
			penguin3.counter = False
			penguin3.hp -= 34
			penguin1.counter = True
			penguin2.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True

	# Checar colisiones - penguin4 - frost
	hits = pygame.sprite.spritecollide(penguin4, frost_list, False)
	for hit in hits:
		if frost1.target == penguin4:
			penguin4.counter = False
			penguin4.hp -= 34
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True

	# Checar colisiones - penguin5 - frost
	hits = pygame.sprite.spritecollide(penguin5, frost_list, False)
	for hit in hits:
		if frost1.target == penguin5:
			penguin5.counter = False
			penguin5.hp -= 34
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True
		
	# Checar colisiones - penguin6 - frost
	hits = pygame.sprite.spritecollide(penguin6, frost_list, False)
	for hit in hits:
		if frost1.target == penguin6:
			penguin6.counter = False
			penguin6.hp -= 34
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True
		
	# Checar colisiones - penguin7 - frost
	hits = pygame.sprite.spritecollide(penguin7, frost_list, False)
	for hit in hits:
		if frost1.target == penguin7:
			penguin7.counter = False
			penguin7.hp -= 34
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True
		
	# Checar colisiones - penguin8 - frost
	hits = pygame.sprite.spritecollide(penguin8, frost_list, False)
	for hit in hits:
		if frost1.target == penguin8:
			penguin8.counter = False
			penguin8.hp -= 34
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True

	# Checar colisiones - penguin9 - frost
	hits = pygame.sprite.spritecollide(penguin9, frost_list, False)
	for hit in hits:
		if frost1.target == penguin9:
			penguin9.counter = False
			penguin9.hp -= 34
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			player1.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True

	# Checar colisiones - player1 - frost
	hits = pygame.sprite.spritecollide(player1, frost_list, False)
	for hit in hits:
		if frost1.target == player1:
			player1.counter = False
			player1.hp -= 90
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player2.counter = True
			player3.counter = True
			frost1.hit = True
		
	# Checar colisiones - player2 - frost
	hits = pygame.sprite.spritecollide(player2, frost_list, False)
	for hit in hits:
		if frost1.target == player2:
			player2.counter = False
			player2.hp -= 90
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player3.counter = True
			frost1.hit = True

	# Checar colisiones - player3 - frost
	hits = pygame.sprite.spritecollide(player3, frost_list, False)
	for hit in hits:
		if frost1.target == player3:
			player3.counter = False
			player3.hp -= 90
			penguin1.counter = True
			penguin2.counter = True
			penguin3.counter = True
			penguin4.counter = True
			penguin5.counter = True
			penguin6.counter = True
			penguin7.counter = True
			penguin8.counter = True
			penguin9.counter = True
			player1.counter = True
			player2.counter = True
			frost1.hit = True
		
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_text1(screen, "P1", 20, 110, 6)
	draw_text1(screen, "P2", 20, 400, 6)
	draw_text1(screen, "P3", 20, 700, 6)
	
	draw_hp_bar(screen, 120, 5, player1.hp//10)
	draw_text2(screen, str(int(player1.hp)) + "/1000", 10, 145, 6)
	if player1.hp > 0:
		draw_hp_bar(screen, player1.rect.x, player1.rect.y, player1.hp//10)

	draw_hp_bar(screen, 415, 5, player2.hp//10)
	draw_text2(screen, str(int(player2.hp))+ "/1000", 10, 435, 6)
	if player2.hp > 0:
		draw_hp_bar(screen, player2.rect.x, player2.rect.y, player2.hp//10)

	draw_hp_bar(screen, 715, 5, player3.hp//10)
	draw_text2(screen, str(int(player3.hp))+ "/1000", 10, 735, 6)
	if player3.hp > 0:
		draw_hp_bar(screen, player3.rect.x, player3.rect.y, player3.hp//10)

	if penguin1.hp > 0:
		draw_hp_bar2(screen, penguin1.rect.x, penguin1.rect.y, penguin1.hp)
	if penguin2.hp > 0:
		draw_hp_bar2(screen, penguin2.rect.x, penguin2.rect.y, penguin2.hp)
	if penguin3.hp > 0:
		draw_hp_bar2(screen, penguin3.rect.x, penguin3.rect.y, penguin3.hp)
	if penguin4.hp > 0:
		draw_hp_bar2(screen, penguin4.rect.x, penguin4.rect.y, penguin4.hp)
	if penguin5.hp > 0:
		draw_hp_bar2(screen, penguin5.rect.x, penguin5.rect.y, penguin5.hp)
	if penguin6.hp > 0:
		draw_hp_bar2(screen, penguin6.rect.x, penguin6.rect.y, penguin6.hp)
	if penguin7.hp > 0:
		draw_hp_bar2(screen, penguin7.rect.x, penguin7.rect.y, penguin7.hp)
	if penguin8.hp > 0:
		draw_hp_bar2(screen, penguin8.rect.x, penguin8.rect.y, penguin8.hp)
	if penguin9.hp > 0:
		draw_hp_bar2(screen, penguin9.rect.x, penguin9.rect.y, penguin9.hp)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
		
	pygame.display.flip()
pygame.quit()