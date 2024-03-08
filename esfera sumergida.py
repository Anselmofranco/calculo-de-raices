# Hallar la porción d de una esfera de radio 
# r=10cm y densidad ρ=0,638g/cm 3 que
# queda sumergida en agua de manera estable.
# El modelo matemático es
# π.(d 3 -3d 2 .r+4.r 3 .ρ )/3 = 0

import math as m 
def f(d):
    
    return m.pi*((d**3)-3*(d**2)*r+4*r**3*rho)/3
 
r=10
rho=0.638
a=0
b=20
c=(a+b)/2

while abs(f(c))>1e-4:
    if f(c)*f(a)<0:
        b=c
    else:
        a=c
    print(c,f(c))
    c=(a+b)/2