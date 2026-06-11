import numpy as np
import matplotlib.pyplot as plt
import math

def secante(f, x0, x1, tol):
    ea = 100
    n = 0
    print('{:^10s}{:^10s}{:^10s}{:^10s}{:^10s}'.format('n', 'x_n', 'x_n-1', 'x_n+1','Error'))
    while ea > tol:
        n = n + 1
        xran = x0
        xr = x1 - (((x1 - x0)*(f(x1)))/(f(x1) - f(x0)))
        ea = abs((((xr- xran)/xr))*100)
        print('{:^10}{:^10f}{:^10f}{:^10f}{:^10f}'.format(n, x0, x1, xr,ea))
        x0 = x1
        x1 = xr
        if ea < tol:
            print ('Se alcanzo la tolerancia: ', tol, '%', ' en ', n, ' iteraciones')
            print ('Solucion hasta la tolerancia: ', xr)
            break
        if math.isclose (0, ea, abs_tol= 0.0000001):
            #print ('Solucion encontrada en ', i, ' iteraciones')
            print ('Solucion encontrada: ', xr, 'en ', n, ' iteraciones')
            break
    return xr, n
tol = 0
x0 = 0.4
x1 = 0.5
def f(x):
    return 8*np.sin(x)*np.exp(-x) - 1
g = f
solucion, iteraciones = secante(f, x0, x1, tol)

x = np.linspace(x0-6, x1+6, 400)
y = f(x)
plt.plot(x, y)
plt.scatter(solucion, 0, color='green', s=40)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Metodo de la Secante')
plt.legend(['Funcion $f(x)$$=$$0$', 
 f'Raiz aproximada en {iteraciones} iteraciones: %.6f' %solucion])
plt.grid(True)
plt.show()
