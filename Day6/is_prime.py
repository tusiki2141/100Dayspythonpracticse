def is_prime(num):
    for factor in range(2,int(num**0.5)+1):
        if num%factor==0:
            return False
    return True if num!=1 else False

