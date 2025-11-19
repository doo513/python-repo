min, max, target = map(int,input().split())

sum = min

#n = int(input())

block = min + max

for i in range(1,int(target / (min+max))+1):
    if min > (target - min) % block or (target - min) % block > max:
        print(-1)
        break
    else:
        sum = min + i*(min+max) + 1
        if(sum < target):
            print(sum, end = ' ')
    