def main():
    try:
        with open('a.jpg','rb')as fs1:
            data=fs1.read()
            print(type(data)) #<class 'bytes'>
        with open('b.jpg','wb') as fs2:
            fs2.write(data)

    except FileNotFoundError as e:
        print('指定文件无法打开')
    except  IOError as e:
        print('读写文件出错')
    
    print('执行结束')

if __name__=='__main__':
    main()