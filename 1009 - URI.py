def calcBonus():
    nome = input()
    a = float(input())
    b = float(input())

    x = (b*0.15)+a;
    print("TOTAL = R$","{0:.2F}".format(x));

calcBonus();