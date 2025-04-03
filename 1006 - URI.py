
def calcularMedia (a, b, c):
    return (a*0.2)+(b*0.3)+(c*0.5);

a = float(input());
b = float(input());
c = float(input());

x = calcularMedia(a,b,c);

print("MEDIA =", "{0:.1f}".format(x));