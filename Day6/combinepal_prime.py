def is_pal(num):
    temp=num
    total=0
    while temp>0:
        total=total*10+temp%10
        temp //=10
    return total==num

def is_prime(num):
    for factor in range(2,int(num**0.5)+1):
        if num%factor==0:
            return False
    return True if num!=1 else False

if __name__=='__main__':
    num=int(input("请输入正整数"))
    if is_pal(num) and is_prime(num):
        print("%d是回文素数"%num)
    else:
        print("%d不是回文素数"%num)
    