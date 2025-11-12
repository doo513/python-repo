d = []
for i in range(10):
    d.append(list(map(int, input().split())))

x,y = 1,1
while (1):
        if(d[x][y] == 2):
            d[x][y] = 9
            break
        if(d[x][y] == 0):
            d[x][y] = 9
            if(d[x][y+1] != 1):
                y += 1
            else:
                x += 1
        if(d[x+1][y] == 1 and d[x][y+1] == 1):
            d[x][y] = 9
            break
for i in range(10):
    for j in range(10):
        print(d[i][j],end = ' ')
    print()
