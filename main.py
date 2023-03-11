import random
import pgzrun
import copy

sirka = 15
vyska = 21  # 21
pocet_pixelu = 25

WIDTH = sirka * pocet_pixelu
HEIGHT = vyska * pocet_pixelu

kostka = []
for a in range(4):
    kostka.append([0] * 4)
for a in range(4):
    kostka[1][a] = 1

vyska0 = 0
sirka0 = 5



pole = []
for y in range(vyska):
    radek = []
    for x in range(sirka):
        radek.append(0)
    pole.append(radek)

pady = 0

def padani():
    global vyska0, sirka0, rychlostpadu, pady
    if not can_move(vyska0 + 1, sirka0):
        for ukladanix in range(4):
            for ukladaniy in range(4):
                if kostka[ukladanix][ukladaniy] != 0:
                    pole[vyska0 + ukladanix][sirka0 + ukladaniy] = kostka[ukladanix][ukladaniy]
        print(pole)
        vyber_kostky()
        niceni()
        vyska0 = 0
        sirka0 = 5
        if pady == 20:
            pady = 0
            if rychlostpadu != 0.1:
                rychlostpadu -= 0.1
        else:
            pady += 1
    else:
        vyska0 = vyska0 + 1

    print("provedení počtů", vyska0)


def niceni():
    global pole
    nicici_pole = copy.deepcopy(pole)
    for niceniy in range(vyska):
        scitani = 0
        for nicenix in range(sirka):
            if nicici_pole[vyska - niceniy - 1][nicenix] != 0:
                scitani += 1
            if scitani == sirka:
                for a in range(vyska - 1):
                    radek_niceni = []
                    for b in range(sirka):
                        radek_niceni.append(pole[a][b])
                    nicici_pole[a + 1] = radek_niceni
                pole = nicici_pole
                niceni()




def vyber_kostky():
    global kostka
    vybrana_kostka = random.randint(0, 6)
    print(vybrana_kostka, "tady")
    nova_kostka = []
    for a in range(4):
        nova_kostka.append([0] * 4)
    if vybrana_kostka == 0:
        for u in range(4):
            nova_kostka[1][u] = 1
    if vybrana_kostka == 1:
        for u in range(2):
            for h in range(2):
                nova_kostka[u + 1][h + 1] = 2
    if vybrana_kostka == 2:
        for u in range(2):
            nova_kostka[1][u] = 3
        for u in range(2):
            nova_kostka[2][u + 1] = 3
    if vybrana_kostka == 3:
        for u in range(2):
            nova_kostka[2][u] = 4
        for u in range(2):
            nova_kostka[1][u + 1] = 4
    if vybrana_kostka == 4:
        for u in range(3):
            nova_kostka[1][u] = 5
        nova_kostka[2][0] = 5
    if vybrana_kostka == 5:
        for u in range(3):
            nova_kostka[2][u] = 6
        nova_kostka[1][0] = 6
    if vybrana_kostka == 6:
        for u in range(3):
            nova_kostka[2][u] = 7
        nova_kostka[1][1] = 7
    kostka = nova_kostka



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
rychlostpadu = 0.5

def on_mouse_down():
    global neomezenarychlost
    global rychlostpadu
    if neomezenarychlost == 0:
        clock.schedule_interval(padani, rychlostpadu)
        neomezenarychlost = 1


def otoc_kostku(smer):
    kostka_otaceni = []
    for b in range(4):
        kostka_otaceni.append([0] * 4)
    if smer == 1:
        for otackyx in range(4):
            for otackyy in range(4):
                kostka_otaceni[otackyx][otackyy] = kostka[3 - otackyy][otackyx]
    if smer == -1:
        for otackyx in range(3, -1, -1):
            for otackyy in range(3, -1, -1):
                kostka_otaceni[otackyx][otackyy] = kostka[otackyy][3 - otackyx]
    return kostka_otaceni


def on_key_down(key):
    global sirka0, kostka, vyska0
    if key == keys.A or key == keys.LEFT:
        if can_move(vyska0, sirka0 - 1):
            sirka0 = sirka0 - 1
    if key == keys.D or key == keys.RIGHT:
        if can_move(vyska0, sirka0 + 1):
            sirka0 = sirka0 + 1
    print(sirka0)
    if key == keys.E:
        o = otoc_kostku(1)
        if can_move(vyska0, sirka0, o):
            kostka = o
            print(kostka)
    if key == keys.Q:
        o = otoc_kostku(-1)
        if can_move(vyska0, sirka0, o):
            kostka = o
            print(kostka)
    if key == keys.S:
        x = 0
        a = 0
        while a != 1:
            if can_move(vyska0 + x, sirka0):
                x += 1
                print("zkousim")
            else:
                x -= 1
                a = 1
                vyska0 = vyska0 + x

barvy = (0xffffff, 0x00ffff, 0xffff00, 0xff0000, 0x00ff00, 0x0000ff, 0xffa500, 0xa020f0)

def nakresli_kostku(x, y, rgb):
    for kostkax in range(4):
        for kostkay in range(4):
            test = Rect(((x + kostkay) * pocet_pixelu, (y + kostkax) * pocet_pixelu),
                        (pocet_pixelu, pocet_pixelu))
            if kostka[kostkax][kostkay] > 0:
                screen.draw.filled_rect(test, (rgb >> 16, (rgb >> 8) & 0xff, rgb & 0xff))

def draw():
    global vyska0, barva
    screen.clear()
    for y, radek in enumerate(pole):
        for x, barva in enumerate(radek):
            r = Rect((x * pocet_pixelu, y * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
            rgb = barvy[barva]
            screen.draw.filled_rect(r, (rgb >> 16, (rgb >> 8) & 0xff, rgb & 0xff))
    nakresli_kostku(sirka0, vyska0, barvy[barva])
    zkvyska = vyska0
    while can_move(zkvyska, sirka0):
        zkvyska += 1
    zkvyska -= 1
    nakresli_kostku(sirka0, zkvyska, barvy[barva])
    dopad = Rect((sirka0 * pocet_pixelu, zkvyska * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
    nakresli_kostku(sirka0, zkvyska, 0x808080)







    #screen.draw.filled_rect(dopad, (0x80, 0x80, 0x80))

    #for kostkax in range(4):
    #    for kostkay in range(4):
    #        test = Rect(((sirka0 + kostkay) * pocet_pixelu, (vyska0 + kostkax) * pocet_pixelu),
    #                    (pocet_pixelu, pocet_pixelu))
    #        if kostka[kostkax][kostkay] > 0:
    #            rgb = barvy[kostka[kostkax][kostkay]]
    #            screen.draw.filled_rect(test, (rgb >> 16, (rgb >> 8) & 0xff, rgb & 0xff))


pgzrun.go()
