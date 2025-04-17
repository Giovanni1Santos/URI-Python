A,B,C = list(map(float,input().split()))

print('TRIANGULO:',"{0:.3f}".format((A*C)/2));
print('CIRCULO:',"{0:.3f}".format((C*C) * 3.14159));
print('TRAPEZIO:',"{0:.3f}".format(((A+B)*C)/2));
print('QUADRADO:',"{0:.3f}".format(B*B));
print('RETANGULO:',"{0:.3f}".format(A*B));

