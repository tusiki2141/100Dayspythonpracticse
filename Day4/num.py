"""输入一个正整数判断是不是素数。"""
from math import fabs, sqrt
num=int(input("请输入一个正整数："))
end=int(sqrt(num))                #平方根

is_prime=True
for x in range(2,end+1):
    if num%x==0:
        is_prime=False
        break
if is_prime and num!=1:
    print('%d 是素数'%num)
else:
    print('%d 不是是素数'%num)
    