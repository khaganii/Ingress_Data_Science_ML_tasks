a,b,c,x,y = map(int, input().split())
if (x>=a and (y>=b or y>=c)) or (x>=b and (y>=a or y>=c)) or (x>=c and (y>=a or y>=b)):
    print("YES")
else:
    print("NO")