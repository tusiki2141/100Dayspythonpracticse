"""
实现判断一个数是不是回文数的函数
设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，
则称n为一回文数。
例如，若n=1234321，则称n为一回文数；
但若n=1234567，则n不是回文数。
"""


def is_pal(num):
    temp=num
    total=0
    while temp>0:
        total=total*10+temp%10
        temp //=10
    return total==num


