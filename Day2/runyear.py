"""判断是否闰年"""
year=int(input('请输入年份：'))
print(year%4)
if year % 4==0:
    print('%d是闰年'%year)
else:
    print('%d不是闰年'%year)