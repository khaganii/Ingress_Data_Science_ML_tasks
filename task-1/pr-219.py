import math

h, w, l, k = map(int, input().split())
v= h*w*l
n = math.ceil(v/k)
print(n)