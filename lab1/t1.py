import pygame


def t1341(x, y):
    xt, yt = x + 3 * y, 4 * x + y

    return xt, yt


def t1231(x, y):
    xt, yt = x + 2 * y, 3 * x + y

    return xt, yt


def t121n3(list):
    l = list.copy()
    for i in range(len(list) // 2):
        l[2 * i] = list[2 * i] + 2 * list[2 * i + 1]
        l[2 * i + 1] = list[2 * i] - 3 * list[2 * i + 1]
    return l


def tt(list, t):
    l = list.copy()
    for i in range(len(list) // 2):
        l[2 * i] = t[0] * list[2 * i] + t[1] * list[2 * i + 1]
        l[2 * i + 1] = t[2] * list[2 * i] + t[3] * list[2 * i + 1]
    return l


def Move(list, x, y):
    l = list.copy()
    for i in range(len(l) // 2):
        l[2 * i] += x
        l[2 * i + 1] += y
    return l


def Scale(list, c):
    l = list.copy()
    for i in range(len(list)):
        l[i] *= c
    return l


def task1(screen):
    x = int(input())
    y = int(input())
    xt, yt = t1341(x, y)

    print(f'Начальные координаты: {x} {y}')
    print(f'Полученные координаты: {xt} {yt}')
    rect1 = pygame.rect.Rect(0, 0, 5, 5)
    rect1.center = (x, y)
    rect2 = pygame.rect.Rect(0, 0, 5, 5)
    rect2.center = xt, yt
    pygame.draw.rect(screen, (0, 255, 0), rect1)
    pygame.draw.rect(screen, (0, 0, 255), rect2)


def task2(screen):
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 75, 2)
    pygame.draw.line(screen, (0, 255, 0), (200, 25), (200, 175), 2)

    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Синий текст', False, (0, 0, 255))
    screen.blit(text_surface, (300, 100))


def task3(screen):
    t = [1, 3, 4, 1]
    l = [10, 10, 100, 200]
    lt = tt(l, t)
    pygame.draw.line(screen, (0, 255, 0), (l[0], l[1]), (l[2], l[3]), 2)
    pygame.draw.line(screen, (255, 0, 0), (lt[0], lt[1]), (lt[2], lt[3]), 2)


def task4(screen):
    x1, y1, x2, y2 = 0, 100, 200, 300
    pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2))
    center = ((x1 + x2) / 2, (y1 + y2) / 2)
    pygame.draw.circle(screen, (0, 128, 0), center, 5)
    xt1, yt1 = t1231(x1, y1)
    xt2, yt2 = t1231(x2, y2)
    center_t = ((xt1 + xt2) / 2, (yt1 + yt2) / 2)
    pygame.draw.line(screen, (255, 0, 0), (xt1, yt1), (xt2, yt2))
    pygame.draw.circle(screen, (128, 0, 0), center_t, 5)
    pygame.draw.line(screen, (0, 0, 255), center, center_t)


def task5(screen):
    x1, y1, x2, y2 = 50, 100, 250, 200
    x3, y3, x4, y4 = 50, 200, 250, 300
    pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2))
    pygame.draw.line(screen, (0, 223, 0), (x3, y3), (x4, y4))
    xt1, yt1 = t1231(x1, y1)
    xt2, yt2 = t1231(x2, y2)
    xt3, yt3 = t1231(x3, y3)
    xt4, yt4 = t1231(x4, y4)
    pygame.draw.line(screen, (255, 0, 0), (xt1, yt1), (xt2, yt2))
    pygame.draw.line(screen, (223, 0, 0), (xt3, yt3), (xt4, yt4))


def task6(screen):
    l = [-1 / 2, 3 / 2, 3, -2, -1, -1, 3, 5 / 3]
    lt = t121n3(l)
    lp = Move(Scale(l, 100), 600, 400)
    ltp = Move(Scale(lt, 100), 600, 400)

    pygame.draw.line(screen, (0, 255, 0), (lp[0], lp[1]), (lp[2], lp[3]))
    pygame.draw.line(screen, (0, 127, 0), (lp[4], lp[5]), (lp[6], lp[7]))

    pygame.draw.line(screen, (255, 0, 0), (ltp[0], ltp[1]), (ltp[2], ltp[3]))
    pygame.draw.line(screen, (127, 0, 0), (ltp[4], ltp[5]), (ltp[6], ltp[7]))


def task7(screen):
    l = [3, -1, 4, 1, 2, 1]
    t = [0, 1, -1, 0]
    lt = tt(l, t)
    sl = Scale(l, 100)
    slt = Scale(lt, 100)
    lp = Move(sl, 600, 400)
    ltp = Move(slt, 600, 400)

    pygame.draw.line(screen, (0, 255, 0), (lp[0], lp[1]), (lp[2], lp[3]))
    pygame.draw.line(screen, (0, 255, 0), (lp[2], lp[3]), (lp[4], lp[5]))
    pygame.draw.line(screen, (0, 255, 0), (lp[4], lp[5]), (lp[0], lp[1]))

    pygame.draw.line(screen, (255, 0, 0), (ltp[0], ltp[1]), (ltp[2], ltp[3]))
    pygame.draw.line(screen, (255, 0, 0), (ltp[0], ltp[1]), (ltp[4], ltp[5]))
    pygame.draw.line(screen, (255, 0, 0), (ltp[4], ltp[5]), (ltp[2], ltp[3]))


def task8(screen):
    l = [8, 1, 7, 3, 6, 2]
    t = [0, 1, 1, 0]
    lt = tt(l, t)
    sl = Scale(l, 100)
    slt = Scale(lt, 100)
    lp = Move(sl, 0, -50)
    ltp = Move(slt, 0, -50)

    pygame.draw.line(screen, (0, 255, 0), (lp[0], lp[1]), (lp[2], lp[3]))
    pygame.draw.line(screen, (0, 255, 0), (lp[2], lp[3]), (lp[4], lp[5]))
    pygame.draw.line(screen, (0, 255, 0), (lp[4], lp[5]), (lp[0], lp[1]))

    pygame.draw.line(screen, (255, 0, 0), (ltp[0], ltp[1]), (ltp[2], ltp[3]))
    pygame.draw.line(screen, (255, 0, 0), (ltp[0], ltp[1]), (ltp[4], ltp[5]))
    pygame.draw.line(screen, (255, 0, 0), (ltp[4], ltp[5]), (ltp[2], ltp[3]))


def task9(screen):
    l = [5, 1, 5, 2, 3, 2]
    t = [2, 0, 0, 2]
    lt = tt(l, t)
    sl = Scale(l, 100)
    slt = Scale(lt, 100)
    lp = Move(sl, 100, 100)
    ltp = Move(slt, 100, 100)

    pygame.draw.line(screen, (0, 255, 0), (lp[0], lp[1]), (lp[2], lp[3]))
    pygame.draw.line(screen, (0, 255, 0), (lp[2], lp[3]), (lp[4], lp[5]))
    pygame.draw.line(screen, (0, 255, 0), (lp[4], lp[5]), (lp[0], lp[1]))

    pygame.draw.line(screen, (255, 0, 0), (ltp[0], ltp[1]), (ltp[2], ltp[3]))
    pygame.draw.line(screen, (255, 0, 0), (ltp[0], ltp[1]), (ltp[4], ltp[5]))
    pygame.draw.line(screen, (255, 0, 0), (ltp[4], ltp[5]), (ltp[2], ltp[3]))


def task10(screen):
    import math
    a = 100
    b = 100
    px = b + 2 * a
    py = 0
    for i in range(101):
        teta = i * math.pi / 50
        r = b + 2 * a * math.cos(teta)
        x = r * math.cos(teta)
        y = r * math.sin(teta)
        line = Move([px, py, x, y], 600, 400)
        pygame.draw.line(screen, (0, 255, 0), (line[0], line[1]), (line[2], line[3]))
        px = x
        py = y


def task11(screen):
    import math
    x = [2, -2, -2, -2, -2, 2, 2, 2]
    t = [math.cos(math.pi / 32),
         math.sin(math.pi / 32),
         -math.sin(math.pi / 32),
         math.cos(math.pi / 32)]
    x = Scale(x, 100)
    for i in range(20):
        line = Move(x, 600, 400)
        pygame.draw.line(screen, (0, 255, 0), (line[0], line[1]), (line[2], line[3]))
        pygame.draw.line(screen, (0, 255, 0), (line[0], line[1]), (line[6], line[7]))
        pygame.draw.line(screen, (0, 255, 0), (line[4], line[5]), (line[2], line[3]))
        pygame.draw.line(screen, (0, 255, 0), (line[4], line[5]), (line[6], line[7]))
        x = tt(x, t)
        x = Scale(x, 0.9)
