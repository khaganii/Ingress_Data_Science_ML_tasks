n = int(input())
p = 1
while n > 0:
    d = n%10
    n //= 10
    p *= d
print(p)