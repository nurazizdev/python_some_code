import pygame
from pygame.locals import *

pygame.init()

ekran_eni = 500
ekran_uzunligi = 500

ekran = pygame.display.set_mode((ekran_eni, ekran_uzunligi))
pygame.display.set_caption(' Krestik-nolik ')

font = pygame.font.SysFont(None, 30, True, True)
game_over = False
winner = 0

orqa_fon = (200, 255, 210)
line_color = (190, 150, 30)
liniya_qalinligi = 4
clicked = False
pozitsiya = (0, 0)
markerlar = []
uyunchi = 1


def ekranni_buyash():
    ekran.fill(orqa_fon)
    for x in range(1, 5):
        pygame.draw.line(ekran, line_color, (0, x * 101), (ekran_eni, x * 101), liniya_qalinligi)
        pygame.draw.line(ekran, line_color, (x * 101, 0), (x * 101, ekran_uzunligi), liniya_qalinligi)


for x in range(5):
    qator = [0] * 5
    markerlar.append(qator)


def chizish():
    x_pozitsiya = 0
    for x in markerlar:
        y_pozitsiya = 0
        for y in x:
            if y == 1:
                pygame.draw.line(ekran, line_color, (x_pozitsiya * 100 + 15, y_pozitsiya * 100 + 15),
                                 (x_pozitsiya * 100 + 85, y_pozitsiya * 100 + 85), liniya_qalinligi)
                pygame.draw.line(ekran, line_color, (x_pozitsiya * 100 + 85, y_pozitsiya * 100 + 15),
                                 (x_pozitsiya * 100 + 15, y_pozitsiya * 100 + 85), liniya_qalinligi)
            if y == -1:
                pygame.draw.circle(ekran, line_color, (x_pozitsiya * 100 + 50, y_pozitsiya * 100 + 50), 38.0,
                                   liniya_qalinligi)
            y_pozitsiya += 1
        x_pozitsiya += 1


def uyin_logikasi():
    global game_over
    global winner

    x_pozitsiya = 0
    for x in markerlar:
        # ustun tekshirish
        if sum(x) == 5:
            winner = 1
            game_over = True
        if sum(x) == -5:
            winner = 2
            game_over = True
        # qatorni tekshirish
        if markerlar[0][x_pozitsiya] + markerlar[1][x_pozitsiya] + markerlar[2][x_pozitsiya] + markerlar[3][x_pozitsiya] + markerlar[4][x_pozitsiya] == 5:
            winner = 1
            game_over = True
        if markerlar[0][x_pozitsiya] + markerlar[1][x_pozitsiya] + markerlar[2][x_pozitsiya] + markerlar[3][
            x_pozitsiya] + markerlar[4][x_pozitsiya] == -5:
            winner = 2
            game_over = True
        x_pozitsiya += 1
    # diaganal ko'rinishda tekshirish
    if markerlar[0][0] + markerlar[1][1] + markerlar[2][2] + markerlar[3][3] + markerlar[4][4] == 5 or markerlar[4][0] + markerlar[3][1] + markerlar[2][2] + markerlar[1][3] +markerlar[0][4] == 5:
        winner = 1
        game_over = True
    if markerlar[0][0] + markerlar[1][1] + markerlar[2][2] + markerlar[3][3] + markerlar[4][4] == 5 or markerlar[4][0] + markerlar[3][1] + markerlar[2][2] + markerlar[1][3] + markerlar[0][4] == -5:
        winner = 2
        game_over = True

    if game_over == False:
        tie = True
        for qator in markerlar:
            for i in qator:
                if i == 0:
                    tie = False
        if tie == True:
            game_over = True
            winner = 0


def natija(winner):
    if winner != 0:
        end_text =  str(winner) + '-chi o`yinchi yutdi!'
    elif winner == 0:
        end_text = "O'yin durang bilan yakunlandi"

    rasm = font.render(end_text, True, (255, 0, 0))
    ekran.blit(rasm, (ekran_eni // 2 - 100, ekran_uzunligi // 2 - 50))

    replay = " Yana bir marta o'ynashni hohlaysanmi?"
    restart_rasmi = font.render(replay, True, (0, 255, 0))
    ekran.blit(restart_rasmi, (ekran_eni // 2 - 80, ekran_uzunligi // 2 + 21))


run = True
while run:
    ekranni_buyash()
    chizish()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pozitsiya = pygame.mouse.get_pos()
                kletka_x = pozitsiya[0] // 100
                kletka_y = pozitsiya[1] // 100
                if markerlar[kletka_x][kletka_y] == 0:
                    markerlar[kletka_x][kletka_y] = uyunchi
                    uyunchi *= -1
                    uyin_logikasi()

    if game_over == True:
    # O'yin ni kimdir haqqat yutgan bulsa
        natija(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pozitsiya = pygame.mouse.get_pos()


    pygame.display.update()
pygame.quit()
