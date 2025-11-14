a = int(input())

sum = 0

for i in range(a):
    if (1 >= a or a == 0):
        print(sum + a)
        break
    
    if(sum >= a):
        print(sum)
        break
    else:
        sum += i
