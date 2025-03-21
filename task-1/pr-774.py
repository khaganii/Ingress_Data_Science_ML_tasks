import math
r,w,l = map(int, input().split())
d = math.sqrt(math.pow(w,2)+math.pow(l,2))
if 2*r >= d:
    print("YES")
else:
    print("NO")