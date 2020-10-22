hrs = int(input("Enter hrs"))
rate = float(input("Enter hrs"))

if hrs>40:
    hrs-=40
    pay=(40*rate)+(hrs*(rate*1.5))
    print(pay)
else:
    pay=rate*hrs
    print(pay)


