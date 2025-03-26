import pygame
import math
import random
import time
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('src/background.jpeg')

pygame.display.set_caption("Turtle")
icon = pygame.image.load('src/Graphics/turtle.png')
pygame.display.set_icon(icon)

scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def menu():
    welcome_font = pygame.font.Font('freesansbold.ttf', 50)
    welcome = welcome_font.render('Welcome to Turtle!', True, (255, 255, 255))
    instruction = font.render('Press any arrow key to start', True, (255, 255, 255))
    screen.blit(welcome, (165, 250))
    screen.blit(instruction, (170, 310))


def show_score(x, y):
    score = font.render('Score: ' + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 10, 10))
    report = font.render('Your score this time was ' + str(scoreValue), True, (255, 255, 255))
    try_again = font.render('Press ESC to reset', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    screen.blit(try_again, (255, 360))
    screen.blit(report, (185, 320))


playerImg = pygame.image.load('src/Graphics/turtle-up.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


foodImg = pygame.image.load('src/Graphics/apple.png')
foodX = random.randint(136, 634)
foodY = random.randint(116, 534)


def player(x, y):
    screen.blit(playerImg, (x, y))


def food(x, y):
    screen.blit(foodImg, (x, y))


def is_collision(apple_x, apple_y, snake_x, snake_y):
    distance = math.sqrt((math.pow(apple_x-snake_x, 2)) + (math.pow(apple_y-snake_y, 2)))
    if distance < 40:
        return True
    return False


def defeat(x, y):
    if (x <= 110 or x >= 640 or y <= 100 or y >= 548) and x < 1000 and y < 1000:
        return True
    return False


mixer.music.load('src/SFX/background-music.wav')
mixer.music.play(-1)

baseSpeed = 0.05
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerImg = pygame.image.load('src/Graphics/turtle-left.png')
            playerY_change = 0
            playerX_change = -baseSpeed - 0.002 * scoreValue
        if event.key == pygame.K_RIGHT:
            playerImg = pygame.image.load('src/Graphics/turtle-right.png')
            playerY_change = 0
            playerX_change = baseSpeed + 0.002 * scoreValue
        if event.key == pygame.K_UP:
            playerImg = pygame.image.load('src/Graphics/turtle-up.png')
            playerX_change = 0
            playerY_change = -baseSpeed - 0.002 * scoreValue
        if event.key == pygame.K_DOWN:
            playerImg = pygame.image.load('src/Graphics/turtle-down.png')
            playerX_change = 0
            playerY_change = baseSpeed + 0.002 * scoreValue

    playerX += playerX_change
    playerY += playerY_change

    collision = is_collision(foodX, foodY, playerX, playerY)
    if collision:
        eatingSound = mixer.Sound('src/SFX/snake-eating.wav')
        eatingSound.play()
        scoreValue += 10
        foodX = random.randint(136, 634)
        foodY = random.randint(116, 534)

    gameOver = defeat(playerX, playerY)
    if playerX >= 800 or playerY >= 600:
        game_over_text()
    if gameOver:
        mixer.music.stop()
        defeatSound = mixer.Sound('src/SFX/game-over.wav')
        defeatSound.play()
        playerX += 2000
        foodX += 2000
        playerX_change = 0
        playerY_change = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            playerX = 370
            playerY = 480
            playerX_change = 0
            playerY_change = 0
            foodX = random.randint(136, 634)
            foodY = random.randint(116, 534)
            scoreValue = 0
            mixer.music.play(-1)
            time.sleep(0.2)

    if playerX < 1000 and playerY < 1000 and playerX_change == 0 and playerY_change == 0:
        menu()

    player(playerX, playerY)
    food(foodX, foodY)
    show_score(textX, textY)
    pygame.display.update()