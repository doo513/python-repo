min, max, target = map(int,input().split())

sum = min

#n = int(input())

block = min + max

win = []

for i in range(min):
    win.append(int((target - i+1) % block))

for i in range(1,int(target / (min+max))+1):
    sum = min + i*(min+max) + 1
    if(min <= (target - i+1) % block or (target - i+1) % block <= max):
        if(sum <= target):
            print(sum)
    else:
        print(-1)