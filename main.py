import random
import pgzrun

sirka = 10
vyska = 20
pocet_pixelu = 50

pole = []
for y in range(vyska):
    radek = []
    for x in range(sirka):
        radek.append(0)
    pole.append(radek)

def draw():
    screen.clear()
    for y, radek in enumerate(pole):
        for x, barva in enumerate(radek):
            screen.draw.line(y * pocet_pixelu, x * pocet_pixelu, (255, 255, 255))
    for x, radek in enumerate(pole):
        for y, barva in enumerate(radek):
            screen.draw.line(x * pocet_pixelu, y * pocet_pixelu, (255, 255, 255))


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

