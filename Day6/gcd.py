"""
实现计算求最大公约数和最小公倍数的函数
"""
def gcd(x,y):                           #求最大公约数
    (x,y)=(y,x) if x>y else(x,y)
    for facotr in range (x,0,-1):
        if x%facotr==0 and y%facotr==0:
            return facotr

def lcm(x,y):                            #求最小公倍数
    return x*y//gcd(x,y)

print(gcd(15,20))
print(lcm(15,20))

