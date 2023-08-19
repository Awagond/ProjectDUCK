import pygame
from pygame import gfxdraw
import time

print("XYU")  # вывести на экран мой большой и тяжёлый


pygame.init()

WIDTH = 1280
HEIGHT = 720
make_jump = False
jump_counter = 30


#=============================================================== настройки игры здесь
screen = pygame.display.set_mode((WIDTH, HEIGHT))
map = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("ProjectDUCK")
#pygame.display.toggle_fullscreen() # включение полноэкранного режима
tickrate = pygame.time.Clock()  # здесь FPS задавать нельзя
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


RUN = True

#================================================================ GEYPAD

#pygame.joystick.init() # инициализация геймпада
#js = pygame.joystick.Joystick(0) # задаём переменной js первый(0) инициализированный геймпад

#pygame.event.pump()
#print(js.get_numbuttons())



"""
xxx
js_name = js.get_name() 
print(js_name) #  вывод имени геймпада

js_count = pygame.joystick.get_count()
print(js_count) #  вывод количества геймпадов

js_init = pygame.joystick.get_init()
print(js_init) #  проверка инициализации геймпада

print(js.get_power_level()) #  проверка подключения и питания геймпада
print(js.get_numaxes()) # вывод количества осей на геймпаде

pygame.event.pump()
print(js.get_axis(0))
print(js.get_axis(1))
print(js.get_axis(2))
print(js.get_axis(3))
print(js.get_axis(4))
print(js.get_axis(5))

#print(pygame.joystick.get_id())
#pygame.event.pump()
#print(js.get_axis(1))
"""

#=============================================================== игра здесь
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    screen.fill("grey")  # заполнение экрана цветом для очистки от прошлых кадров

    color = (0,0,0)
    radius = 30
    green = (0, 200, 64)
    place1 = pygame.Rect((0, 500, 600, 50)) # первые два это x и y положение, вторые это ширина и высота
    pygame.draw.rect(screen, green, place1)
    #screen.blit(map, (0, 0))
    map.set_alpha(128)
    print(screen.get_rect())

    pygame.gfxdraw.aacircle(screen, int(player_pos.x), int(player_pos.y), radius, color) # рисовка кольца(незаполненного круга) для сглаживания основного круга
    pygame.gfxdraw.filled_circle(screen, int(player_pos.x), int(player_pos.y), radius, color) # основной круг (персонаж)
    

    pygame.display.update()

    #pygame.draw.circle(screen, "black", player_pos, 20, width=10)
    #pygame.event.pump() # что-то вроде отправки событий с геймпада
    keys = pygame.key.get_pressed()
    #print(js.get_button(0))




# управление геймпадом (пока гейспада нет - закоментировано)


#    if js.get_axis(0) > 0.5:
#        if player_pos.x > WIDTH - radius:
#            ...
#        else:
#            player_pos.x += 300 * dt
#    if js.get_axis(0) < -0.5:
#        if player_pos.x < radius:
#            ...
#        else:
#            player_pos.x -= 300 * dt
#    if js.get_axis(1) > 0.5:
#        if player_pos.y > HEIGHT-radius:
#            ...
#        else:
#            player_pos.y += 300 * dt
#    if js.get_axis(1) < -0.5:
#        if player_pos.y < radius:
#           ...
#       else:
#           player_pos.y -= 300 * dt



# управление клавиатурой

    if keys[pygame.K_UP]:
        if player_pos.y <= radius:
            ...
        else:
            player_pos.y -= 700 * dt
    if keys[pygame.K_DOWN]:
        if player_pos.y >= HEIGHT-radius:
            ...
        else:
            player_pos.y += 700 * dt
    if keys[pygame.K_LEFT]:
        if player_pos.x <= radius:
            ...
        else:
            player_pos.x -= 700 * dt
    if keys[pygame.K_RIGHT]:
        if player_pos.x >= WIDTH-radius:
            ...
        else:
            player_pos.x += 700 * dt

    if player_pos.y > HEIGHT - radius:
        ...
    else:
        pass
        #player_pos.y += 400 * dt

    if keys[pygame.K_SPACE]:
    #if js.get_button(0) == 1:
        make_jump = True
    if make_jump == True:
        if jump_counter >= 0:
            #print(jump_counter / 2.5)
            player_pos.y -= jump_counter / 2.5 # формула инерции прыжка
            jump_counter -= 1 # счётчик инерции
        else:
            #print("else", jump_counter / 2.5)
            player_pos.y -= jump_counter / 2.5
            jump_counter -= 1
            if (player_pos.y - jump_counter / 2.5) >= HEIGHT - radius: # если инерция рискует выйти за границы экрана, то идёт просчёт оставшегося пути для падения
                #print("if", jump_counter / 2.5)
                #print("if", player_pos.y)
                player_pos.y += (HEIGHT-radius) - player_pos.y
                jump_counter = 30
                make_jump = False # Прыжок окончен
        #else:  # изначальная концовка прыжка
        #    jump_counter = 30
        #    make_jump = False




    pygame.display.flip()  # для отображения всего на экране (и для обновления содержимого)
    dt = tickrate.tick(60) / 1000  # dt — это дельта-время в секундах с момента последнего кадра, используемое для частоты кадров. # независимая физика.

#=============================================================== игра кончилась
pygame.quit()