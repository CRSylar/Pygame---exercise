import pygame
import sys
import random

pygame.init()
pygame.font.init()

# SPRITE
_sfondo_ = pygame.image.load('immagini/sfondo.png')
_bird_	= pygame.image.load('immagini/uccello.png')
_ground_ = pygame.image.load('immagini/base.png')
_gameover_ = pygame.image.load('immagini/gameover.png')
_pipedwn_ = pygame.image.load('immagini/tubo.png')
_pipeup_ = pygame.transform.flip(_pipedwn_, False, True)

# WINDOWS, FRAME RATE & LATERAL SPEED
WIN	= pygame.display.set_mode((288, 512))
FPS	= 60
GRND_VEL = 5
FONT = pygame.font.SysFont('Comic Sans MC', 40, bold=True)
pygame.display.set_caption("Flappy Bird!")

# PIPE
class	pipe_class:
	def	__init__(self) :
		self.x = 350
		self.y = random.randint(-75, 150)

	def	go_and_draw(self) :
		self.x -= GRND_VEL
		WIN.blit(_pipedwn_, (self.x, self.y + 210))
		WIN.blit(_pipeup_, (self.x, self.y - 210))

	def collision(self, _bird_, _birdx, _birdy) :
		spread = 5
		_bird_dx = _birdx + _bird_.get_width() - spread
		_bird_sx = _birdx + spread
		_bird_up = _birdy + spread
		_bird_dwn = _birdy + _bird_.get_height() - spread
		_pipe_dx = self.x + _pipedwn_.get_width()
		_pipe_sx = self.x
		_pipe_up = self.y + 110
		_pipe_dwn = self.y +215
		if _bird_dx > _pipe_sx and _bird_sx < _pipe_dx :
			if _bird_up < _pipe_up or _bird_dwn > _pipe_dwn:
				_game_over()

	def	pass_thrugh(self, _bird_, _birdx) :
		spread = 5
		_bird_dx = _birdx + _bird_.get_width() - spread
		_bird_sx = _birdx + spread
		_pipe_dx = self.x + _pipedwn_.get_width()
		_pipe_sx = self.x
		if _bird_dx > _pipe_sx and _bird_sx < _pipe_dx :
			return True

# DRAW ALL OBJ ON SCREEN
def	draw_obj():
	WIN.blit(_sfondo_, (0,0))
	for pipe in _pipes:
		pipe.go_and_draw()
	WIN.blit(_bird_, (_birdx, _birdy))
	WIN.blit(_ground_, (_grndx, 450))
	_scoretab = FONT.render(str(_score), 0, (240, 240, 240))
	WIN.blit(_scoretab, (200, 0))

# REFRESH SCREEN
def	refresh():
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

# INIZIALIZE GLOBAL VAR
def	_initialize():
	global	_birdx, _birdy, _birdvel
	global	_grndx
	global _pipes
	global _score
	global _thrugh
	_birdx, _birdy = 60, 150
	_birdvel = 0
	_grndx = 0
	_score = 0
	_pipes = []
	_pipes.append(pipe_class())
	_thrugh = False

# GAME OVER
def	_game_over():
	WIN.blit(_gameover_, (50,180))
	refresh()
	restart = False
	while not restart:
		for event in pygame.event.get() :
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				_initialize()
				restart = True
				loop = True
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

# PROGRAM START
_initialize()

while True:
	# LATERAL & BIRD MOVEMENT
	_grndx -= GRND_VEL
	if _grndx < -46 :
		_grndx = 0
	_birdvel += 1
	_birdy += _birdvel
	# KEY EVENT
	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) :
			_birdvel = -10
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
	# PIPE GENERATION
	max_pipesx = 0
	for pipe in _pipes:
		if pipe.x > max_pipesx:
			max_pipesx = pipe.x
	if max_pipesx < 150:
		_pipes.append(pipe_class())
# PIPE COLLISION
	for pipe in _pipes:
		pipe.collision(_bird_, _birdx, _birdy)
	if not _thrugh:
		for pipe in _pipes:
			if pipe.pass_thrugh(_bird_, _birdx):
				_thrugh = True
				break
	if _thrugh:
		_thrugh = False
		for pipe in _pipes:
			if pipe.pass_thrugh(_bird_, _birdx):
				_thrugh = True
				break
		if not _thrugh:
			_score += 1
# GROUND COLLISION
	if _birdy >= 445 :
		_game_over()
# FINALLY PRINT ALL
	draw_obj()
	refresh()
