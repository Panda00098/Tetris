import random
import pgzrun
import copy
import keyboard

sirka = 15
vyska = 21  # 21
pocet_pixelu = 25

WIDTH = (sirka + 7) * pocet_pixelu
HEIGHT = (vyska + 7) * pocet_pixelu

kostka = []
for a in range(4):
    kostka.append([0] * 4)
for a in range(4):
    kostka[1][a] = 1

vyska0 = 0
sirka0 = 5

#prazny_radek = [0] * sirka

pole = []
for y in range(vyska):
    radek = []
    for x in range(sirka):
        radek.append(0)
    pole.append(radek)

pady = 0
scitani_kostek = 0

def padani():
    global vyska0, sirka0, rychlostpadu, pady, scitani_kostek, neomezenarychlost
    if not can_move(vyska0 + 1, sirka0):
        for ukladanix in range(4):
            for ukladaniy in range(4):
                if kostka[ukladanix][ukladaniy] != 0:
                    pole[vyska0 + ukladanix][sirka0 + ukladaniy] = kostka[ukladanix][ukladaniy]
        konec()
        niceni()
        vyska0 = 0
        sirka0 = 5
        scitani_kostek += 1
        if pady == 100:
            pady = 0
            rychlostpadu = 25
            rychlost_padu()
        else:
            if pady == 19:
                if rychlostpadu > 40:
                    rychlostpadu -= 5
                    pady = 0
                    rychlost_padu()
            else:
                pady += 1
        print(pady)
    else:
        vyska0 = vyska0 + 1


koncici_obrazovka = False

def konec():
    global koncici_obrazovka, pole, hlidani, zrychli_pohyb, pamatovak, zasoba_kostek, kostka_stranou, rychlostpadu
    vyber_kostky(0, 0)
    if not can_move(1, 5):
        koncici_obrazovka = True
        draw()
        pole = []
        for y in range(vyska):
            radek = []
            for x in range(sirka):
                radek.append(0)
            pole.append(radek)
        zasoba_kostek = []
        rychlostpadu = 100
        for x in range(5):
            zasoba_kostek.append(random.randint(0, 6))
        kostka_stranou = []
        for a in range(4):
            kostka_stranou.append([0] * 4)
        hlidani = 0
        zrychli_pohyb = False
        pamatovak = 0
        keyboard.wait("esc")


scitani_rad = 0

def niceni():
    global pole, scitani_rad
    nicici_pole = copy.deepcopy(pole)
    for niceniy in range(vyska):
        scitani = 0
        for nicenix in range(sirka):
            if nicici_pole[vyska - niceniy - 1][nicenix] != 0:
                scitani += 1
        if scitani == sirka:
            scitani_rad += 1
            for a in range(vyska-1-niceniy, 0, -1):
                nicici_pole[a] = nicici_pole[a-1]
            nicici_pole[0] = [0] * sirka
            pole = nicici_pole
            niceni()
            break


zasoba_kostek = []
for x in range(5):
    zasoba_kostek.append(random.randint(0, 6))
kostka_stranou = []
for a in range(4):
    kostka_stranou.append([0] * 4)

def vyber_kostky(kde, kolikata):
    global kostka, zasobarna, vybrana_kostka, kostka_stranou
    if kde == 0:
        vybrana_kostka = zasoba_kostek.pop(0)
        zasoba_kostek.append(random.randint(0, 6))
    if kde == 1:
        vybrana_kostka = zasoba_kostek[kolikata]
#    vybrana_kostka = 0
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
    if kde == 0:
        kostka = nova_kostka
    if kde == 1:
        kostka_stranou = nova_kostka




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



rychlostpadu = 100

def rychlost_padu():
    clock.unschedule(padani)
    clock.schedule_interval(padani, rychlostpadu / 100)


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

hlidani = 0
zrychli_pohyb = False
pamatovak = 0
def on_key_down(key):
    global sirka0, kostka, vyska0, hlidani, rychlostpadu, pamatovak
    if key == keys.A or key == keys.LEFT:
        clock.schedule_interval(pohyb_do_stran, 0.1)
    if key == keys.D or key == keys.RIGHT:
        clock.schedule_interval(pohyb_do_stran, 0.1)
    if key == keys.E:
        otocka = otoc_kostku(1)
        if can_move(vyska0, sirka0, otocka):
            kostka = otocka
    if key == keys.Q:
        otocka = otoc_kostku(-1)
        if can_move(vyska0, sirka0, otocka):
            kostka = otocka
    if key == keys.W:
        pad = 0
        koncime = 0
        while koncime != 1:
            if can_move(vyska0 + pad, sirka0):
                pad += 1
            else:
                pad -= 1
                koncime = 1
                vyska0 = vyska0 + pad
    if key == keys.SPACE:
        if hlidani == 0:
            clock.schedule_interval(padani, rychlostpadu / 100)
            hlidani = 1
    if key == keys.S:
        pamatovak = rychlostpadu
        rychlostpadu = 5
        rychlost_padu()



def on_key_up(key):
    global rychlostpadu
    if key == keys.S:
        rychlostpadu = pamatovak
        rychlost_padu()
    if key == keys.A or key == keys.LEFT:
        clock.unschedule(pohyb_do_stran)
    if key == keys.D or key == keys.RIGHT:
        clock.unschedule(pohyb_do_stran)

def pohyb_do_stran():
    global sirka0
    if keyboard.is_pressed("a") or keyboard.is_pressed("left"):
        if can_move(vyska0, sirka0 - 1):
            sirka0 = sirka0 - 1
    if keyboard.is_pressed("d") or keyboard.is_pressed("right"):
        if can_move(vyska0, sirka0 + 1):
            sirka0 = sirka0 + 1






barvy = (0xffffff, 0x00ffff, 0xffff00, 0xff0000, 0x00ff00, 0x0000ff, 0xffa500, 0xa020f0)


def jaka_barva():
    global rgb_kostky
    pocitani_barvy = 0
    for kostkax in range(4):
        for kostkay in range(4):
            if kostka[kostkax][kostkay] > 0:
                rgb_kostky = kostka[kostkax][kostkay]
                pocitani_barvy = 1
            if pocitani_barvy == 1:
                break
        if pocitani_barvy == 1:
            break



def jaka_barva_strana():
    global rgb_kostky_strany
    pocitani_barvy = 0
    for kostkax in range(4):
        for kostkay in range(4):
            if kostka_stranou[kostkax][kostkay] > 0:
                rgb_kostky_strany = kostka_stranou[kostkax][kostkay]
                pocitani_barvy = 1
            if pocitani_barvy == 1:
                break
        if pocitani_barvy == 1:
            break



def nakresli_kostku(x, y, rgb):
    for kostkax in range(4):
        for kostkay in range(4):
            test = Rect(((x + kostkay) * pocet_pixelu, (y + kostkax) * pocet_pixelu),
                        (pocet_pixelu, pocet_pixelu))
            if kostka[kostkax][kostkay] > 0:
                screen.draw.filled_rect(test, (rgb >> 16, (rgb >> 8) & 0xff, rgb & 0xff))



def nakresli_kostku_strana(x, y, rgb):
    for kostkax in range(4):
        for kostkay in range(4):
            test = Rect(((x + kostkay) * pocet_pixelu, (y + kostkax) * pocet_pixelu),
                        (pocet_pixelu, pocet_pixelu))
            if kostka_stranou[kostkax][kostkay] > 0:
                screen.draw.filled_rect(test, (rgb >> 16, (rgb >> 8) & 0xff, rgb & 0xff))




def draw():
    if not koncici_obrazovka:
        global vyska0
        screen.clear()
        for y, radek in enumerate(pole):
            for x, barva in enumerate(radek):
                r = Rect((x * pocet_pixelu, y * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
                rgb = barvy[barva]
                screen.draw.filled_rect(r, (rgb >> 16, (rgb >> 8) & 0xff, rgb & 0xff))
        zkvyska = vyska0
        while can_move(zkvyska, sirka0):
            zkvyska += 1
        zkvyska -= 1
        nakresli_kostku(sirka0, zkvyska, 0xD3D3D3)
        jaka_barva()
        nakresli_kostku(sirka0, vyska0, barvy[rgb_kostky])
        for c in range(5):
            vyber_kostky(1, c)
            jaka_barva_strana()
            nakresli_kostku_strana(17, 1 + c * 4, barvy[rgb_kostky_strany])
        screen.draw.text(("destroyed layers: " + str(scitani_rad)), (1 * pocet_pixelu, (vyska + 1) * pocet_pixelu), color="gray")
        screen.draw.text(("block placed: " + str(scitani_kostek)), (1 * pocet_pixelu, (vyska + 3) * pocet_pixelu), color="gray")
        screen.draw.text(("speed: " + str(rychlostpadu / 10)), (1 * pocet_pixelu, (vyska + 5) * pocet_pixelu), color="gray")
    if koncici_obrazovka:
        screen.clear()
        screen.draw.text("GAME OVER", (2.5 * pocet_pixelu, 2 * pocet_pixelu), color="red", fontsize=100)
        screen.draw.text("score:", (2.5 * pocet_pixelu, (vyska - 1) * pocet_pixelu), color="green", fontsize=40)
        screen.draw.text(("destroyed layers: " + str(scitani_rad)), (2.5 * pocet_pixelu, (vyska + 1) * pocet_pixelu), color="green", fontsize=25)
        screen.draw.text(("block placed: " + str(scitani_kostek)), (2.5 * pocet_pixelu, (vyska + 3) * pocet_pixelu), color="green", fontsize=25)
        screen.draw.text(("speed: " + str(rychlostpadu / 10)), (2.5 * pocet_pixelu, (vyska + 5) * pocet_pixelu), color="green", fontsize=25)



pgzrun.go()