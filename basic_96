d = []
for i in range(19):
    d.append(list(map(int, input().split()))) # map 함수로 리스트를 받아오기

n = int(input())

for i in range(n):
    xy = input().split() # 좌표 입력받기
    
    for j in range(19):
        d[int(xy[0])-1][j] = 1 - d[int(xy[0])-1][j] # 입력된 좌표의 행 값과 1을 뺌. 1이면 0으로 0이면 1이 저장되게 됨
    for k in range(19):
        d[k][int(xy[1])-1] = 1 - d[k][int(xy[1])-1] # 입력된 좌표의 열 값과 1을 뺌. 1이면 0으로 0이면 1이 저장되게 됨
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()
