"""生成斐波那契数列的前20个数"""
f1=1
f2=1
x=2
print(f1,end=" ")
while x<=20:
    print(f2,end=" ")
    f1,f2=f2,f1+f2
    x+=1
