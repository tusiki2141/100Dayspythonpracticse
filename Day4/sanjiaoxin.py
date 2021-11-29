"""
打印
*
**
***
****
*****
"""
#自己想的答案
x="*"
row1=int(input('请输入行数'))
for i in range(row1+1):
    print(x*i)

#jack答案
row2 = int(input('请输入行数: '))
for i in range(row2):
    for _ in range(i + 1):
        print('*', end='')
    print()

row3=int(input('请输入行数'))
for i in range(row3+1):
    print(" "*(row3-i),x*i)

row4=int(input('请输入行数'))
j=1
for i in range(row4+1):
    print(" "*(row4-i),x*j)
    j+=2