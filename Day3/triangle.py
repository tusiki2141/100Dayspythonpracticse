"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
a=float(input('请输入a：'))
b=float(input('请输入b：'))
c=float(input('请输入c：'))

if a+b>c and b+c>a and a+c>b:
    print('周长等于%f'%(a+b+c))
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print('面积等于%f'%area)
else:
    print('不能构成三角形')
#计算面积公式为海伦公式