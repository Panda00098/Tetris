# import random
import pgzrun

sirka = 15
vyska = 21
pocet_pixelu = 25


kostka = []
for a in range(4):
    kostka.append([0] * 4)
vyska0 = 0
vyska1 = 1
vyska2 = 2
vyska3 = 3
sirka0 = 0
sirka1 = 1
sirka2 = 2
sirka3 = 3
kostka[0][1] = 1
kostka[0][2] = 1
kostka[1][1] = 1
kostka[1][2] = 1


print(kostka)

pole = []
for y in range(vyska):
    radek = []
    for x in range(sirka):
        radek.append(0)
    pole.append(radek)
pole[2][3] = 1


def draw():
    global barva_kostky
    screen.clear()
    for y, radek in enumerate(pole):
        for x, barva in enumerate(radek):
            r = Rect((x * pocet_pixelu, y * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
            if barva == 0:
                barva_kostky = (255, 255, 255)
            screen.draw.filled_rect(r, barva_kostky)
    if kostka[0][1] == 1:
        test = Rect((sirka1 * pocet_pixelu, vyska0 * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
        screen.draw.filled_rect(test, (255, 0, 255))
    if kostka[0][2] == 1:
        test = Rect((sirka2 * pocet_pixelu, vyska0 * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
        screen.draw.filled_rect(test, (255, 0, 255))
    if kostka[1][1] == 1:
        test = Rect((sirka1 * pocet_pixelu, vyska1 * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
        screen.draw.filled_rect(test, (255, 0, 255))
    if kostka [1][2] == 1:
        test = Rect((sirka2 * pocet_pixelu, vyska1 * pocet_pixelu), (pocet_pixelu, pocet_pixelu))
        screen.draw.filled_rect(test, (255, 0, 255))
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

pgzrun.go()
