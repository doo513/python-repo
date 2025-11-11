d = []
for i in range (20):
    d.append([])
    for j in range(20):
        d[i].append(0)
# 2차원 리스트 생성 0[],1[]...[19][19]
n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1
#원하는 행 x번, 열 y번에 1 저장
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end = ' ') # 전체 출력 [0][1] 부터 [0][19]를 거쳐 [19][19] 출력
    print() # 열 출력 후 줄 바꿈으로 다음 행이 있을 자리에 열 출력
