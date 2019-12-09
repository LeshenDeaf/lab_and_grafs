import numpy as np
import random


def graf1():
    n = randint(10, 20)
    colorR = [0] * n
    mtrR = [[0] * 3 for i in range(n)]

    for i in range(n):
        if i % 2 != 0:
            colorR[i] = 1
        else:
            colorR[i] = 2

    for i in range(0, n-1):
        mtrR[i][0] = i
        mtrR[i][1] = i + 1
        if i % 2 != 0:
            mtrR[i][2] = 1
        else:
            mtrR[i][2] = 2
    mtrR.pop(n-1)

    loops = randint(2, 4)
    edges = []

    for i in range(loops):
        x = randint(0, n-1)
        while x in edges:
            x = randint(0, n - 1)
        edges.append(x)
        mtrR.append([x, x, 3])

    loops = randint(2, 4)
    edges = []

    for i in range(loops):
        x = randint(0, n-2)
        while x in edges or x + 1 in edges:
            x = randint(0, n - 2)
        edges.append(x)
        mtrR.append([x, x+1, 4])

    loops = randint(2,4)

    for i in range(loops):
        v = randint(0, n-1)
        u = randint(0, n-1)
        while u == v or colorR[u] == colorR[v] or v in edges or u in edges or -1 <= u - v <= 1:
            v = randint(0, n - 1)
            u = randint(0, n - 1)
        edges.append(u)
        edges.append(v)
        mtrR.append([u, v, 5])

    f = open('out1.txt', 'w')
    f.write('{0}  {1}\n'.format(n, len(mtrR)))

    for i in range(len(mtrR)):
        f.write('{0} {1}, color of the edge is {2}\n'.format(mtrR[i][0], mtrR[i][1], mtrR[i][2]))

    for i in range(n):
        f.write('{0}, color is {1}\n'.format(i, colorR[i]))

    f.close()

    return mtrR


def graf2():
    n = randint(10, 20)
    difference = randint(5, 8)
    red = [None] * (n - difference)
    black = [None] * difference

    i = 0
    while i < (n - difference):
        x = randint(0, n-1)
        while x in red:
            x = randint(0, n - 1)
        red[i] = x
        i += 1

    i = 0
    while i < difference:
        x = randint(0, n - 1)
        while x in black or x in red:
            x = randint(0, n - 1)
        black[i] = x
        i += 1

    mtrR = [[None] * 3 for i in range(n)]
    edge = 0

    i = 0
    while i < len(red) and i < len(black):
        mtrR[i][0] = red[i]
        mtrR[i][1] = black[i]
        mtrR[i][2] = 1
        edge += 1
        i += 1

    edges = []

    if len(red) > len(black):
        rr = (len(red) - len(black))
        for i in range(rr):
            x = randint(0, n - 1)
            while x in red or x in edges:
                x = randint(0, n - 1)
            mtrR[edge + i][0] = red[edge + i]
            mtrR[edge + i][1] = x
            mtrR[edge + i][2] = 2

    elif len(red) < len(black):
        rr = (len(black) - len(red))
        for i in range(rr):
            x = randint(0, n - 1)
            while x in black or x in edges:
                x = randint(0, n - 1)
            mtrR[edge + i][0] = black[edge + i]
            mtrR[edge + i][1] = x
            mtrR[edge + i][2] = 2

    loops = 2 #  randint(2, 4)
    edges = []

    for i in range(loops):
        x = randint(0, n - 1)
        while x in edges:
            x = randint(0, n - 1)
        edges.append(x)
        mtrR.append([x, x, 3])

    loops = 2 #  randint(2, 4)
    edges = []

    for i in range(loops):
        x = random.choice(red)
        z = red.index(x)
        y = mtrR[z][1]
        while x in edges or y in edges:
            x = random.choice(red)
            z = red.index(x)
            y = mtrR[z][1]
        edges.append(x)
        edges.append(y)
        mtrR.append([x, y, 4])

    loops = 1 #  randint(2, 4)
    edges = []
    for i in range(loops):
        v = random.choice(red)
        u = random.choice(black)
        while v in edges or u in edges:
            v = random.choice(red)
            u = random.choice(black)
        edges.append(v)
        edges.append(u)
        mtrR.append([v, u, 5])

        z = red.index(v)
        y = black.index(u)
        zv = mtrR[z][1]
        yu = mtrR[y][0]
        edges.append(zv)
        edges.append(yu)
        mtrR.append([zv, yu, 5])

    f = open('out2.txt', 'w')
    f.write('{0}  {1}\n'.format(n, len(mtrR)))

    for i in range(len(mtrR)):
        if mtrR[i][0] != None or mtrR[i][1] != None or mtrR[i][2] != None:
            f.write('{0} {1}, color of the edge is {2}\n'.format(mtrR[i][0], mtrR[i][1], mtrR[i][2]))

    for i in red:
        f.write('{0}, color is red\n'.format(i))

    for i in black:
        f.write('{0}, color is black\n'.format(i))

    f.close()
    return mtrR


def graf3():
    def connect(v, color, cnt):
        if v + 1 != n:
            i = v + 1
            while flag[i]:
                i += 1
                if i == n:
                    return cnt
            mtrV[v][i] = color % 3 + 1
            colorR[i] = color % 3 + 1
            colorV[i] = color % 3 + 1
            flag[i] = True
            if i + 1 != n:
                mtrV[v][i+1] = (color + 1) % 3 + 1
                colorR[i+1] = (color + 1) % 3 + 1
                colorV[i+1] = (color + 1) % 3 + 1
                flag[i+1] = True
        return cnt

    n = randint(10, 20)
    m = 0
    mtrV = np.zeros((n, n), dtype=np.int8)
    flag = [False] * n
    colorR = [0] * n
    colorV = [0] * n
    cnt = 4

    for i in range(n):
        leaves = 2
        prob = randint(i, n)

        if prob == i:
            mtrV[i][0] = cnt #cycle
            mtrV[i][0] = cnt + 1 #pair edge
            cnt += 2
        else:
            connected = 0
            cnt = connect(i, colorR[i], cnt)

    for i in range(n):
        for j in range(n):
            prob = randint(0, n)
            if prob == j and not mtrV[i][i]:
                mtrV[i][i] = cnt
                cnt += 1
                m += 1
            if mtrV[i][j] and i != j:
                m += 1

    f = open('out3.txt', 'w')
    f.write('{0}  {1}\n'.format(n, m))

    for i in range(n):
        for j in range(n):
            if mtrV[i][j]:
                f.write('{0} {1}, color of the edge is {2}\n'.format(i, j, mtrV[i][j]))

    for i in range(n):
        f.write('{0}, color is {1}\n'.format(i, colorV[i]))

    f.close()

    return colorR


def graf4():

    def check(i, m):
        if mtrR[i][0] in dR:
            dR[mtrR[i][0]].append(color)
        else:
            dR[mtrR[i][0]] = [color]
        if m == 1:
            if mtrR[i][1] in dR:
                dR[mtrR[i][1]].append(color)
            else:
                dR[mtrR[i][1]] = [color]

    def loop(i, j, color):
        while mtrR[j][0] == mtrR[i][0]:
            colors.append(mtrR[j][2])
            while color in colors or color in dR[mtrR[i][0]] or color in dR[mtrR[i][1]]:
                color += 1
            j += 1
            if j == len(mtrR):
                break
        return color

    n = randint(10, 20)
    mtrV = np.zeros((n, n), dtype=bool)
    mtrColor = [0] * n
    mtrColor[0] = 1
    for i in range(1, n):
        vs = randint(1, 2)
        connected = []
        for j in range(vs):
            x = randint(0, n-1)
            col_x = 1
            while col_x == mtrColor[x] or col_x in connected:
                col_x += 1
            mtrV[i][x] = 1
            mtrV[x][i] = 1
            mtrColor[i] = col_x
            connected.append(mtrColor[x])

    mtrR = []
    for i in range(n):
        for j in range(i, n):
            if mtrV[i][j]:
                mtrR.append([i, j, 0])

    bf = mtrR[0][0]
    bi = 0
    colors = []
    dR = dict()
    m = len(mtrR)
    for i in range(m):
        b = i
        if mtrR[i][0] not in dR:
            dR[mtrR[i][0]] = []
        if mtrR[i][1] not in dR:
            dR[mtrR[i][1]] = []
        if bf != mtrR[b][0]:
            bf = mtrR[b][0]
            bi = b
            colors = []
        j = bi

        color = 1
        color = loop(i, j, color)

        j = mtrR[i][1]
        i = mtrR[j][0]

        check(i, 0)

        color = loop(i, j, color)
        mtrR[b][2] = color
        i = b

        check(i, 1)

        prob = randint(0, n // 2)
        j = bi + 1
        if prob == 1:
            color = loop(i, bi, color)
            mtrR.append([mtrR[i][0], mtrR[i][1], color])
            check(i, 1)

    f = open('Dashin_out4.txt', 'w')
    f.write('{0}  {1}\n'.format(n, len(mtrR)))

    for i in range(len(mtrR)):
        f.write('{0} {1}, color of the  edge is {2}\n'.format(mtrR[i][0], mtrR[i][1], mtrR[i][2]))

    for i in range(len(mtrColor)):
        f.write('{0} color is {1}\n'.format(i, mtrColor[i]))

    f.close()

    return mtrR


def graf5():
    def check(i, m):
        if mtrR[i][0] in dR:
            dR[mtrR[i][0]].append(color)
        else:
            dR[mtrR[i][0]] = [color]
        if m == 1:
            if mtrR[i][1] in dR:
                dR[mtrR[i][1]].append(color)
            else:
                dR[mtrR[i][1]] = [color]

    def loop(i, j, color):
        while mtrR[j][0] == mtrR[i][0]:
            colors.append(mtrR[j][2])
            while color in colors or color in dR[mtrR[i][0]] or color in dR[mtrR[i][1]]:
                color += 1
            j += 1
            if j == len(mtrR):
                break
        return color

    n = randint(10, 20)
    mtrV = np.zeros((n, n), dtype = bool)
    mtrColor = [0] * n
    mtrColor[0] = 1
    for i in range(1, n):
        vs = randint(1, i)
        connected = []
        for j in range(vs):
            x = randint(0, i-1)
            col_x = 1
            while col_x == mtrColor[x] or col_x in connected:
                col_x += 1
            mtrV[i][x] = 1
            mtrV[x][i] = 1
            mtrColor[i] = col_x
            connected.append(mtrColor[x])

    mtrR = []
    for i in range(n):
        for j in range(i, n):
            if mtrV[i][j] == 1:
                mtrR.append([i, j, 0])

    bf = mtrR[0][0]
    bi = 0
    colors = []
    dR = dict()
    m = len(mtrR)
    for i in range(m):
        b = i
        if mtrR[i][0] not in dR:
            dR[mtrR[i][0]] = []
        if mtrR[i][1] not in dR:
            dR[mtrR[i][1]] = []
        if bf != mtrR[b][0]:
            bf = mtrR[b][0]
            bi = b
            colors = []
        j = bi

        color = 1
        color = loop(i, j, color)

        j = mtrR[i][1]
        i = mtrR[j][0]

        if mtrR[i][0] not in dR:
            dR[mtrR[i][0]] = []

        color = loop(i, j, color)
        mtrR[b][2] = color
        i = b

        check(i, 1)

        prob = randint(0, n//2)
        if prob == 0:
            color = loop(i, i, color)
            mtrR.append([mtrR[i][0], mtrR[i][0], color])
            check(i, 0)
        j = bi + 1
        if prob == 1:
            color = loop(i, bi, color)
            mtrR.append([mtrR[i][0], mtrR[i][1], color])
            check(i, 1)
        i = b

    f = open('out5.txt','w')
    f.write('{0}  {1},\n'.format(n, len(mtrR)))

    for i in range(len(mtrR)):
        f.write('{0} {1}, color of the  edge is {2}\n'.format(mtrR[i][0], mtrR[i][1], mtrR[i][2]))

    for i in range(len(mtrColor)):
        f.write('{0} color is {1}\n'.format(i, mtrColor[i]))

    f.close()

    return mtrR


def main():
    graf1()
    graf2()
    graf3()
    graf4()
    graf5()
    print('_____G O T O V O_____')


if __name__ == '__main__':
    randint = random.randint
    main()
