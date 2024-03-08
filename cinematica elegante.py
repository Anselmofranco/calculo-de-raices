import math as m

def f(t):
    return y_0+(c*v+c**2*9.8)*(1-m.e**(-t/c))-9.8*c*t

c=2
y_0=10
v=18
a=0
b=20
d=(a+b)/2

while abs(f(d))>1e-7:
    if f(d)*f(a)<0:
        b=d
    else:
        a=d
    print(d,f(d))
    d=(a+b)/2
