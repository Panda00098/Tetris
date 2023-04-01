import math
import random
import sys
import os
import pgzrun
import copy
import time

sirka = 8
vyska = 10  # 21
pocet_pixelu = 25



kostka = []

vyska0 = 0
sirka0 = round(sirka / 2) - 2
pole = []
zasoba_kostek = []


try:
    vzpominani = open(f"{os.path.dirname(__file__)}\\saved_tetris.txt", "r")
    if vzpominani.readline() != "":
        saved = 1
        vzpominani.seek(0)
        vyska = int(vzpominani.readline().strip())
        sirka = int(vzpominani.readline().strip())
        for y in range(vyska):
            pole.append(list(map(int, vzpominani.readline().strip().split())))
        vyska0 = int(vzpominani.readline().strip())
        sirka0 = int(vzpominani.readline().strip())
        for y in range(4):
            kostka.append(list(map(int, vzpominani.readline().strip().split())))
        zasoba_kostek = list(map(int, vzpominani.readline().strip().split()))
        rychlostpadu = int(vzpominani.readline().strip())
        vypisovaci_rychlost = int(vzpominani.readline().strip())
        konecny_cas = vzpominani.readline().strip()
        aktualnicas = float(vzpominani.readline().strip())
        scitani_rad = int(vzpominani.readline().strip())
        scitani_kostek = int(vzpominani.readline().strip())
        pady = int(vzpominani.readline().strip())
    else:
        saved = 0
        pole = []
        for y in range(vyska):
            radek = []
            for x in range(sirka):
                radek.append(0)
            pole.append(radek)
except FileNotFoundError:
    saved = 0
    pole = []
    for y in range(vyska):
        radek = []
        for x in range(sirka):
            radek.append(0)
        pole.append(radek)


WIDTH = (sirka + 7) * pocet_pixelu
HEIGHT = (vyska + 8) * pocet_pixelu


if saved == 0:
    for a in range(4):
        kostka.append([0] * 4)




if saved == 0:
    pady = 0
    scitani_kostek = 0
    vypisovaci_rychlost = 100

def padani():
    global vyska0, sirka0, rychlostpadu, pady, scitani_kostek, neomezenarychlost, vypisovaci_rychlost
    if not can_move(vyska0 + 1, sirka0):
        for ukladanix in range(4):
            for ukladaniy in range(4):
                if kostka[ukladanix][ukladaniy] != 0:
                    pole[vyska0 + ukladanix][sirka0 + ukladaniy] = kostka[ukladanix][ukladaniy]
        vyska0 = 0
        sirka0 = 5
        konec()
        niceni()
        scitani_kostek += 1
        if pady == 100:
            pady = 0
            rychlostpadu = 25
            vypisovaci_rychlost = 25
            rychlost_padu()
        else:
            if pady == 10:
                if rychlostpadu > 40:
                    rychlostpadu -= 5
                    vypisovaci_rychlost -= 5
                    pady = 0
                    rychlost_padu()
        pady += 1
    else:
        vyska0 = vyska0 + 1






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


def konec():
    global koncici_obrazovka, pole, zrychli_pohyb, pamatovak, zasoba_kostek, kostka_stranou, vypnout
    vyber_kostky(0, 0)
    if not can_move(1, 5):
        vypnout = False
        clock.unschedule(padani)
        draw()
        pole = []
        for y in range(vyska):
            radek = []
            for x in range(sirka):
                radek.append(0)
            pole.append(radek)
        zasoba_kostek = []
        for x in range(5):
            zasoba_kostek.append(random.randint(0, 6))
        kostka_stranou = []
        for a in range(4):
            kostka_stranou.append([0] * 4)
        zrychli_pohyb = False
        pamatovak = 0
        vypis = open(f"{os.path.dirname(__file__)}\\saved_tetris.txt", "w")
        vypis.close()





if saved == 0:
    for x in range(round(vyska / 4)):
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
    #vybrana_kostka = 6
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

if saved == 0:
    vyber_kostky(0, 0)


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
vypnout = True
cas_po_pauze = 0





def on_key_down(key):
    global sirka0, kostka, vyska0, hlidani, rychlostpadu, pamatovak, casovac
    if vypnout:
        if key == keys.K_0:
            ukladani_do_souboru()
        if key == keys.SPACE:
            if hlidani == 0:
                casovac = time.time()
                if saved == 1:
                    casovac -= aktualnicas
                rychlost_padu()
                draw()
                hlidani = 1
        if hlidani == 1:
            if key == keys.A or key == keys.LEFT:
                pohyb_do_stran_vlevo()
                clock.schedule_interval(pohyb_do_stran_vlevo, 0.15)
            if key == keys.D or key == keys.RIGHT:
                pohyb_do_stran_vpravo()
                clock.schedule_interval(pohyb_do_stran_vpravo, 0.15)
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
                        vyska0 += pad
            if key == keys.S:
                pamatovak = rychlostpadu
                rychlostpadu = 5
                rychlost_padu()
            if key == keys.ESCAPE:
                clock.unschedule(padani)
                hlidani = 0






def on_key_up(key):
    global rychlostpadu
    if vypnout:
        if hlidani == 1:
            if key == keys.S:
                rychlostpadu = pamatovak
                rychlost_padu()
            if key == keys.A or key == keys.LEFT:
                clock.unschedule(pohyb_do_stran_vlevo)
            if key == keys.D or key == keys.RIGHT:
                clock.unschedule(pohyb_do_stran_vpravo)




def on_mouse_down(pos):
    global vypnout, pady, scitani_kostek, scitani_rad, rychlostpadu, vypisovaci_rychlost,casovac
    if not vypnout:
        if 5 * pocet_pixelu < pos[0] < 8 * pocet_pixelu < pos[1] < 11 * pocet_pixelu:
            sys.exit("ukoncil/a jsi program")
        if 5 * pocet_pixelu < pos[0] < 8 * pocet_pixelu and 14 * pocet_pixelu < pos[1] < 17 * pocet_pixelu:
            pady = 0
            scitani_kostek = 0
            scitani_rad = 0
            rychlostpadu = 100
            vypisovaci_rychlost = 100
            vypnout = True
            casovac = time.time()
            clock.schedule_interval(padani, rychlostpadu / 100)





def ukladani_do_souboru():
    vypis = open(f"{os.path.dirname(__file__)}\\saved_tetris.txt", "w")
    vypis.write(str(vyska) + "\n" + str(sirka) + "\n")
    for vypis_y in range(vyska):
        ukladani = " ".join(map(str, pole[vypis_y])) + "\n"
        vypis.write(ukladani)
    vypis.write(str(vyska0) + "\n" + str(sirka0) + "\n")
    for vypis_y in range(4):
        ukladani = " ".join(map(str, kostka[vypis_y])) + "\n"
        vypis.write(ukladani)
    vypis.write(" ".join(map(str, zasoba_kostek)) + "\n")
    vypis.write(
        str(rychlostpadu) + "\n" + str(vypisovaci_rychlost) + "\n" + konecny_cas + "\n" + str(aktualnicas) + "\n" + str(
            scitani_rad) + "\n" + str(scitani_kostek) + "\n" + str(pady) + "\n")
    vypis.close()
    sys.exit("saved")



def pohyb_do_stran_vlevo():
    global sirka0
    if can_move(vyska0, sirka0 - 1):
        sirka0 = sirka0 - 1

def pohyb_do_stran_vpravo():
    global sirka0
    if can_move(vyska0, sirka0 + 1):
        sirka0 = sirka0 + 1




barva_kompletni = (0xffffff, 0x00ffff, 0xffff00, 0xff0000, 0x00ff00, 0x0000ff, 0xffa500, 0xa020f0)
barva_mensiho_jasu = (0xffffff, 0xe0ffff, 0xffffe0, 0xffcccb, 0x90ee90, 0xadd8e6, 0xffd580, 0xcbc3e3)
barvy = barva_kompletni


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



def update():
    draw()



def draw():
    global vyska0, barvy, konecny_cas, aktualnicas
    if vypnout:
        screen.clear()
        if hlidani == 1:
            barvy = barva_kompletni
        else:
            barvy = barva_mensiho_jasu
        for y, radek in enumerate(pole):
            for x, barva in enumerate(radek):
                r = Rect((x * pocet_pixelu, y * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
                rgb = barvy[barva]
                screen.draw.filled_rect(r, (rgb >> 16, (rgb >> 8) & 0xff, rgb & 0xff))
        zkvyska = vyska0
        while can_move(zkvyska, sirka0):
            zkvyska += 1
        zkvyska -= 1
        nakresli_kostku(sirka0, zkvyska, 0xdcdcdc)
        jaka_barva()
        nakresli_kostku(sirka0, vyska0, barvy[rgb_kostky])
        for c in range(round(vyska / 4)):
            vyber_kostky(1, c)
            jaka_barva_strana()
            nakresli_kostku_strana(sirka + 1, vyska - 4 - c * 4, barvy[rgb_kostky_strany])
        screen.draw.text(("destroyed layers: " + str(scitani_rad)), (1 * pocet_pixelu, (vyska + 2.5) * pocet_pixelu),
                         color="green", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text(("block placed: " + str(scitani_kostek)), (1 * pocet_pixelu, (vyska + 4) * pocet_pixelu),
                         color="green", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text(("speed: " + str(vypisovaci_rychlost / 10)), (1 * pocet_pixelu, (vyska + 5.5) * pocet_pixelu),
                         color="green", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text("SETTINGS: ", ((sirka - 1) * pocet_pixelu, (vyska + 1) * pocet_pixelu),
                         color="dimgray", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text("left, right: a, d", (sirka * pocet_pixelu, (vyska + 2) * pocet_pixelu),
                         color="dimgray", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text("turning: q, e", (sirka * pocet_pixelu, (vyska + 3) * pocet_pixelu),
                         color="dimgray", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text("faster falling: s", (sirka * pocet_pixelu, (vyska + 4) * pocet_pixelu),
                         color="dimgray", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text("port down: w", (sirka * pocet_pixelu, (vyska + 5) * pocet_pixelu),
                         color="dimgray", fontsize=pocet_pixelu * (24 / 25))
        screen.draw.text("pause: esc", (sirka * pocet_pixelu, (vyska + 6) * pocet_pixelu),
                         color="dimgray", fontsize=pocet_pixelu * (24 / 25))
        if hlidani == 1:
            aktualnicas = time.time() - casovac
            cashms = time.strftime("%H:%M:%S", time.gmtime(aktualnicas))
            milisec = (aktualnicas - math.floor(aktualnicas)) * 1000
            milisec = math.floor(milisec)
            screen.draw.text(("time: " + cashms + ":" + str(milisec)), (1 * pocet_pixelu, (vyska + 1) * pocet_pixelu),
                             color="green", fontsize=pocet_pixelu * (24 / 25))
            konecny_cas = "time: " + cashms + ":" + str(milisec)
        else:
            if saved == 0:
                screen.draw.text("time: 00:00:00:000", (1 * pocet_pixelu, (vyska + 1) * pocet_pixelu),
                                 color="green", fontsize=pocet_pixelu * (24 / 25))
            else:
                screen.draw.text(konecny_cas, (1 * pocet_pixelu, (vyska + 1) * pocet_pixelu),
                                 color="green", fontsize=pocet_pixelu * (24 / 25))
            screen.draw.text("Press SPACE", ((sirka / 10) * pocet_pixelu, (vyska / 2 - 1) * pocet_pixelu), color="black",
                             fontsize=pocet_pixelu * (sirka * (70 / 15)) / 25)
    if not vypnout:
        screen.clear()
        screen.draw.text("GAME OVER", (2.5 * pocet_pixelu, 2 * pocet_pixelu), color="red", fontsize=pocet_pixelu * 4)
        screen.draw.text("score:", (2.5 * pocet_pixelu, (vyska - 1) * pocet_pixelu), color="green", fontsize=pocet_pixelu * (40 / 25))
        screen.draw.text(("destroyed layers: " + str(scitani_rad)),
                         (2.5 * pocet_pixelu, (vyska + 2.75) * pocet_pixelu), color="green", fontsize=pocet_pixelu)
        screen.draw.text(("block placed: " + str(scitani_kostek)),
                         (2.5 * pocet_pixelu, (vyska + 4.5) * pocet_pixelu), color="green", fontsize=pocet_pixelu)
        screen.draw.text(("speed: " + str(vypisovaci_rychlost / 10)),
                         (2.5 * pocet_pixelu, (vyska + 6.25) * pocet_pixelu), color="green", fontsize=pocet_pixelu)
        for x in range(2):
            r = Rect((5 * pocet_pixelu, (8 + x * 6) * pocet_pixelu), (3 * pocet_pixelu, 3 * pocet_pixelu))
            barviska = (0xff, 0x00, 0x00)
            screen.draw.filled_rect(r, barviska)
        barviska = (0x00, 0x00, 0x00)
        screen.draw.filled_circle((6.5 * pocet_pixelu, 9.5 * pocet_pixelu), pocet_pixelu, barviska)
        barviska = (0xff, 0x00, 0x00)
        screen.draw.filled_circle((6.5 * pocet_pixelu, 9.5 * pocet_pixelu), 0.8 * pocet_pixelu, barviska)
        r = Rect((6.125 * pocet_pixelu, 8.2 * pocet_pixelu), (0.75 * pocet_pixelu, pocet_pixelu))
        screen.draw.filled_rect(r, barviska)
        barviska = (0x00, 0x00, 0x00)
        r = Rect((6.4 * pocet_pixelu, 8.375 * pocet_pixelu), (0.2 * pocet_pixelu, 0.75 * pocet_pixelu))
        screen.draw.filled_rect(r, barviska)
        screen.draw.filled_circle((6.5 * pocet_pixelu, 15.5 * pocet_pixelu), pocet_pixelu, barviska)
        barviska = (0xff, 0x00, 0x00)
        screen.draw.filled_circle((6.5 * pocet_pixelu, 15.5 * pocet_pixelu), 0.8 * pocet_pixelu, barviska)
        r = Rect((5 * pocet_pixelu, 14 * pocet_pixelu), (1.5 * pocet_pixelu, 1.5 * pocet_pixelu))
        screen.draw.filled_rect(r, barviska)
        barviska = (0x00, 0x00, 0x00)
        for x in range(16):
            x /= 50
            screen.draw.line(((6.5 - x) * pocet_pixelu, (14.9 - x) * pocet_pixelu),
                             ((6.5 - x) * pocet_pixelu, (14.3 + x) * pocet_pixelu), barviska)
        screen.draw.text("quit", (10 * pocet_pixelu, 8.75 * pocet_pixelu), color="red", fontsize=pocet_pixelu * (45 / 25))
        screen.draw.text("restart", (10 * pocet_pixelu, 14.75 * pocet_pixelu), color="red", fontsize=pocet_pixelu * (40 / 25))
        screen.draw.text(konecny_cas, (1 * pocet_pixelu, (vyska + 1) * pocet_pixelu), color="green", fontsize=pocet_pixelu * (24 / 25))
pgzrun.go()


#save, upload
#pygame (pygame zero nee)