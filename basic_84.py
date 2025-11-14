a, b, c, s = input().split()

a = int(a)
b = int(b)
c = int(c)
s = int(s)

mb = float(a*b*c*s/(8*1024*1024))

print(format(mb,".1f"),"MB")
