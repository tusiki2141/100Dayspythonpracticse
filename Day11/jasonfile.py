import json

def main():
    mydict={
        'name':'luohao',
        'age':38,
        'qq':1234567,
        'friends':['wang','chen'],
        'cars':[
            {'brand':'benz','speed':'180'},
            {'brand':'bmw','speed':'190'},
            {'brand':'BYD','speed':'280'}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8')as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完毕！')

if __name__ =='__main__':
    main()