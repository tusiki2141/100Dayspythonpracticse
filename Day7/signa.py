s1='\'hello, world!\''
s2='\n\\hello,world!\\\n'
print(s1,s2,end='')

s3 = '\141\142\143\x61\x62\x63'
s4= '\u9a86\u660a'
print(s3, s4)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))