#Raíz positiva de polinomio

def f(t):
    return 10+18*t-4.9*t**2

a=0
b=10
c=(a+b)/2
cant=b

while abs((cant-c)/cant)>1e-4:
    if f(c)*f(a)<0:
        b=c
    else:
        a=c
    print(c,f(c))
    cant=c
    c=(a+b)/2

