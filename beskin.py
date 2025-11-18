min, max, target = map(int,input().split())

sum = min

#n = int(input())

block = min + max

win = []

for i in range(min):
    win.append(int((target - i+1) % block))

for i in range(int(target / (min+max))+1):
    sum += i*(min+max)
    if(sum < target): 
        print(sum)