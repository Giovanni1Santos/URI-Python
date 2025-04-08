def calcSimples():
    
    x = input().split(" ")
    y = input().split(" ")

    a,b,c = x
    a1,b1,c1 = y

    z = (int(b)*float(c))+(int(b1)*float(c1))

    print("VALOR A PAGAR: R$ %0.2f" %z)

calcSimples();