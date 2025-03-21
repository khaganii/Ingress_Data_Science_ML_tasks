# pr-219.py
import math
h, w, l, k = map(int, input().split())
v = h * w * l
n = math.ceil(v / k)
print(n)

# pr-248.py
n = int(input())
s=1
for i in range(1, n+1):
    s += i*2
print(s)

# pr-774.py
import math
r,w,l = map(int, input().split())
d = math.sqrt(math.pow(w,2)+math.pow(l,2))
if 2*r >= d:
    print("YES")
else:
    print("NO")

# pr-902.py
g = int(input())
if 1 <= g <= 3:
    print("Initial")
elif 4 <= g <= 6:
    print("Average")
elif 7 <= g <= 9:
    print("Sufficient")
elif 10 <= g <= 12:
    print("High")

# pr-905.py
a,b,c = map(int, input().split())
if a==b==c:
    print(1)
elif (a==b!=c) or (a==c!=b) or (b==c!=a):
    print(2)
else:
    print(3)

# pr-906.py
n = int(input())
p = 1
while n > 0:
    d = n%10
    n //= 10
    p *= d
print(p)

# pr-923.py
m = int(input())
if 3 <= m <= 5:
    print("Spring")
elif 6 <= m <= 8:
    print("Summer")
elif 9 <= m <= 11:
    print("Autumn")
elif m:
    print("Winter")

# pr-959.py
n = int(input())
s = n%10 + n//1000
print(s)

# pr-959.py
n = int(input())
s = n % 10 + n // 1000
print(s)

# pr-1312.py
a,b,c,x,y = map(int, input().split())
if (x>=a and (y>=b or y>=c)) or (x>=b and (y>=a or y>=c)) or (x>=c and (y>=a or y>=b)):
    print("YES")
else:
    print("NO")

# pr-2606.py
n,m = map(int, input().split())
print(min(n,m), max(n,m))

# pr-2860.py
n,m = map(int, input().split())
s = (m+n)*(m-n + 1) // 2
print(s)

# pr-4717.py
n = int(input())
k = int(input())
print(k%n)

# pr-7812.py
a, b, c, d = map(int, input().split())
print(max(a, b, c, d))

# pr-8254.py
n,m = map(int, input().split())
s = (n-1)*(m*3)
print(s)

# pr-8737.py
n,m = map(int, input().split())
print(n//m, n%m)

# pr-8813.py
a,b,c = map(int, input().split())
s = 2*(a*b + a*c + b*c)
v = a*b*c
print(s, v)

# pr-8815.py
a = int(input())
s = 6*(a*a)
v = a*a*a
print(s, v)