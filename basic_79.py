a = input()
a = int(a)

i = 0
sum = 0

while(sum > a or sum != a):
    i += 1
    sum += i
    if(sum >= a): # 합이 입력값보다 클 경우 무한루프 탈출
        print(i)
        break
