# import random
import pgzrun
from pgzero import clock, screen
from pygame import draw, keys, Rect

sirka = 15
vyska = 11  #21
pocet_pixelu = 25

kostka = []
for a in range(4):
    kostka.append([0] * 4)

vyska0 = 0
sirka0 = 5
kostka[0][1] = 1
kostka[0][2] = 1
kostka[1][1] = 1
kostka[1][2] = 1

def kostka_vyber():
    global vyska0
    global sirka0
    vyska0 = 0
    sirka0 = 5




pole = []
for y in range(vyska):
    radek = []
    for x in range(sirka):
        radek.append(0)
    pole.append(radek)




def padani():
    global vyska0
    vyska0 = vyska0 + 1
    print("provedení počtů", vyska0)


def ukladani():
    if not can_move(vyska0 + 1, sirka0):
        pole[vyska0][sirka0 + 1] = 1
        pole[vyska0][sirka0 + 2] = 1
        pole[vyska0 + 1][sirka0 + 1] = 1
        pole[vyska0 + 1][sirka0 + 2] = 1
        print(pole)
        clock.schedule_unique(kostka_vyber, 0)


def can_move(x, y, co=None):
    if co is None:
        co = kostka
    for pocitanix in range(4):
        for pocitaniy in range(4):
            if co[pocitanix][pocitaniy] == 0:
                continue
            try:
                if x + pocitanix < 0 or y + pocitaniy < 0:
                    return False
                if pole[x + pocitanix][y + pocitaniy] > 0:
                    return False
            except IndexError:
                return False
    return True




neomezenarychlost = 0
def on_mouse_down():
    global neomezenarychlost
    if neomezenarychlost == 0:
        clock.schedule_interval(ukladani, 0.5)
        clock.schedule_interval(padani, 0.5)
        clock.schedule_interval(draw, 0.5)
        clock.schedule_interval(can_move, 0.25)
        neomezenarychlost = 1


def otoc_kostku(smer):
    kostka_otaceni = []
    for b in range(4):
        kostka_otaceni.append([0] * 4)
    if smer == 1:
        for otackyx in range(4):
            for otackyy in range(4):
                kostka_otaceni[otackyx][otackyy] = kostka[otackyy][otackyx]
    if smer == -1:
        for otackyx in range(3, -1, -1):
            for otackyy in range(3, -1, -1):
                kostka_otaceni[otackyx][otackyy] = kostka[otackyy][otackyx]
    return kostka_otaceni

def on_key_down(key):
    global sirka0
    global kostka
    if key == keys.A or key == keys.LEFT:
        if can_move(vyska0, sirka0 - 1):
            if sirka0 >= 0:
                sirka0 = sirka0 - 1
    if key == keys.D or key == keys.RIGHT:
        if can_move(vyska0, sirka0 + 1):
            if sirka0 <= 11:
                sirka0 = sirka0 + 1
    print(sirka0)
    if key == keys.E:
        otoc_kostku(1)
        o = otoc_kostku(0)
        if can_move(vyska0, sirka0, o):
            kostka = o
            print(kostka)
    if key == keys.Q:
        otoc_kostku(-1)
        o = otoc_kostku(0)
        if can_move(vyska0, sirka0, o):
            kostka = o
            print(kostka)




def draw():
    global barva_kostky
    screen.clear()
    for y, radek in enumerate(pole):
        for x, barva in enumerate(radek):
            r = Rect((x * pocet_pixelu, y * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
            if barva == 0:
                barva_kostky = (255, 255, 255)
            if barva == 1:
                barva_kostky = (255, 0, 255)
            screen.draw.filled_rect(r, barva_kostky)
    for kostkax in range(4):
        for kostkay in range(4):
            if kostka[kostkax][kostkay] == 1:
                test = Rect(((sirka0 + kostkay) * pocet_pixelu, (vyska0 - 1) * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
                screen.draw.filled_rect(test, (255, 255, 255))
                test = Rect(((sirka0 + kostkay) * pocet_pixelu, (vyska0 + kostkax) * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
                screen.draw.filled_rect(test, (255, 0, 255))
#    if vyska0 == 19:
#        clock.unschedule(padani)



#    kostka_x = 6
#    kostka_y = 0
#    mal_kostka = Rect((kostka_x * pocet_pixelu, kostka_y * pocet_pixelu), (pocet_pixelu * 2, pocet_pixelu * 2))
#    screen.draw.filled_rect(mal_kostka, (255, 0, 255))


#    def vyber_kostky():
#        while u == 1:
#            v = 0
#            u = 9
#            while kostky[0] != " ":
#                kostky = []
#                 while kostky[3] != " ":
#                     v = v.random.randrange(7)
#                     kostky = kostky.append(v)
#             v = v.random.randrange(7)
#             kostky = kostky.append(v)
#             u = kostky.pop(0)


#    if pole[vyska0 + 2][sirka0 + 1] == 0:
#        if pole[vyska0 + 2][sirka0 + 2] == 0:
#            pohyb_dolu = True
#    if pole[vyska0][sirka0] == 0:
#        if pole[vyska0 + 1][sirka0] == 0:
#            pohyb_vlevo = True
#    if pole[vyska0][sirka0 + 3] == 0:
#        if pole[vyska0 + 1][sirka0 + 3] == 0:
#            pohyb_vpravo = True
pgzrun.go()
