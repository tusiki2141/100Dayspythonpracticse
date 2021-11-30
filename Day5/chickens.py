x,y,z=0,0,0
for x in range(0,21):
    for y in range(0,34):
        for z in range(0,301,3):    #题主提供答案为z=100-x-y
            if x+y+z==100 and 5*x+3*y+z/3==100:
                print('%d 只公鸡，%d 只母鸡，%d 只小鸡'%(x,y,z))