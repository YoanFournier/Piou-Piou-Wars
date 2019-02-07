"""
Game parameters
Created by \
13 / 03 / 18
"""
import pygame
pygame.init()

# ------------------- Screen Parameters -------------------
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850
FPS = 60

# ------------------- Display and Clock -------------------
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS_CLOCK = pygame.time.Clock()

# ------------------- Player Parameters -------------------
PLAYER_START_POS = (200, 700)

# ------------------- Color, Sound, Font and Image Constants -------------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)

SHOOT_SOUND = pygame.mixer.Sound("sound/piou.wav")

FONT1 = pygame.font.Font('font/PressStart2P.ttf', 8)
FONT2 = pygame.font.Font('font/PressStart2P.ttf', 15)

BKG_IMG = pygame.image.load("images/bkg.png")

SHIP_IMG = pygame.image.load("images/ship.png")
SHIP_ICON_IMG = pygame.image.load("images/shipicon.png")
BUD_IMG = pygame.image.load("images/bud.png")
SHROOMY_IMG = pygame.image.load("images/shroomy.png")
CARLO_IMG = pygame.image.load("images/carlo.png")
LASER_1 = pygame.image.load("images/laser1.png")
LASER_2 = pygame.image.load("images/laser2.png")
LASER_3 = pygame.image.load("images/laser3.png")
LASER_4 = pygame.image.load("images/laser4.png")
SMILE = pygame.image.load("images/smile.png")
EXPLOSION = pygame.image.load("images/explosion.png")

REGI_IMG = pygame.image.load("images/regi.png")
REGI_PAWN_IMG = pygame.image.load("images/turtle.png")

ROGER_IMG = pygame.image.load("images/roger.png")

SHIELD_IMG = pygame.image.load("images/shield.png")
SHIELD_ICON_IMG = pygame.image.load("images/shieldicon.png")

INSTANT_KILL_IMG = pygame.image.load("images/instantkill.png")
INSTANT_KILL_ICON_IMG = pygame.image.load("images/instantkillicon.png")

# ------------------- Alien Constants -------------------
S = "Shroomy"
B = "Bud"
C = "Carlo"
REGIS = "Regi"
ROGER = "ROGER"
WAVE_HEIGHT = 25
WAVE_WIDTH = 5
ALIEN_Y_GAP = 50
ALIEN_X_GAP = 70
ALIEN_X_START = 100


