import pygame
import random
from pygame import mixer
pygame.init()

# setup display
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game!")
# sound
mixer.music.load('love_me_like_that_2.mp3')
mixer.music.play(-1, 0.0, 6000)

# game variable
hangman_status = 0
game_over = False
# colors
black = (0, 0, 0)

# Fonts
btn_font = pygame.font.SysFont('arial', 30)
letter_font = pygame.font.SysFont('arial', 60)
game_font = pygame.font.SysFont('arial', 80)

# word
word = ['NONVEG', 'PANEER']
WORD = random.choice(word)
GUESSED = []

# button variables
ROWS = 2
COLS = 13
GAP = 20
SIZE = 40
BOXES = []
for row in range(ROWS):
    for col in range(COLS):
        x = ((col * GAP) + GAP) + (SIZE * col)
        y = ((row * GAP) + GAP) + (SIZE * row) + 410
        box = pygame.Rect(x, y, SIZE, SIZE)
        BOXES.append(box)

BUTTONS = []
A = 65
for ind, box in enumerate(BOXES):
    letter = chr(A + ind)
    button = [box, letter]
    BUTTONS.append(button)
# load images
images = []
for i in range(0, 7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)


# draw buttons
def draw_btn(BUTTONS):
    for box, letter in BUTTONS:
        btn_text = btn_font.render(letter, True, black)
        btn_rect = btn_text.get_rect(center=(box.x + 20, box.y + 20))
        win.blit(btn_text, btn_rect)


# clock
FPS = 120
clock = pygame.time.Clock()

run = True

while run:
    clock.tick(FPS)
    win.fill((255, 160, 200))
    win.blit(images[hangman_status], (90, 90))
    draw_btn(BUTTONS)
    won = True

    for letter in WORD:
        if letter not in GUESSED:
            won = False
    if won:
        game_over = True
        game_over_message = 'YOU WON!!'
    else:
        game_over_message = 'YOU LOST!!'

    display_text = ''

    for letter in WORD:
        if letter in GUESSED:
            display_text += f"{letter}"
        else:
            display_text += '_ '
    text = letter_font.render(display_text, True, black)
    win.blit(text, (400, 200))

    for box in BOXES:
        pygame.draw.rect(win, black, box, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # pos = pygame.mouse.get_pos()
            pos = event.pos
            for button, letter in BUTTONS:
                if button.collidepoint(pos):
                    if letter not in WORD:
                        hangman_status += 1
                    if hangman_status == 6:
                        game_over = True
                    GUESSED.append(letter)
                    BUTTONS.remove([button, letter])
    if game_over:
        win.fill((255, 160, 200))
        text = game_font.render(game_over_message, True, black)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        win.blit(text, text_rect)
    pygame.display.update()
