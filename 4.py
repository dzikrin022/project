def fibo(kolom,baris):
    a, b , c= 0,1,0
    for i in range(baris):
        for j in range(kolom) :
            print(a, end=',')
            c=a+b
            a=b
            b=c
        print()

