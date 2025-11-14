h, w = input().split()
n = int(input())

li = []
for i in range(int(h)):
    li.append([])
    for j in range(int(w)):
        li[i].append(0)
for i in range(n):
    l,d,x,y = input().split()
    for j in range (int(l)):
        if(int(d) == 0):
            li[int(x)-1][j+int(y)-1] = 1
        if(int(d) == 1):
            li[j+int(x)-1][int(y)-1] = 1
            
for i in range (int(h)):
    # print(li[i])
    for j in range (int(w)):
        print(li[i][j],end = ' ')
    print()
