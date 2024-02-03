from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
backgroud = transform.scale(image.load('1438095291_0.jpg'),(700, 500))

run = True
clock = time.Clock()
FPS = 60

x1 = 100
y1 = 250
x2 = 250
y2 = 250
sprite1 = transform.scale(image.load('87-874440_hebergeur-dimage-смешарики-клипарт.png'),(100, 100))
sprite2 = transform.scale(image.load('завантаження.jfif'),(100, 100))

while run:
    window.blit(backgroud, (0,0))
    window.blit(sprite1, (x1,y1))
    window.blit(sprite2, (x2,y2))
    for e in event.get():
        if e.type == QUIT:
            run = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 3:
        x1 -= 10
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += 10
    if keys_pressed[K_UP] and y1 > 3:
        y1 -= 10
    if keys_pressed[K_DOWN] and y1< 395:
        y1 += 10
    if keys_pressed[K_a] and x2 > 3:
        x2 -= 10
    if keys_pressed[K_d] and x2 < 595:
        x2 += 10
    if keys_pressed[K_w] and y2 > 3:
        y2 -= 10
    if keys_pressed[K_s] and y2 < 395:
        y2 += 10

    display.update()
    clock.tick(FPS)
