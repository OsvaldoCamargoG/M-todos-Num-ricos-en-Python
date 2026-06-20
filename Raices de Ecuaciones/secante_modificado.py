import numpy as np 
import matplotlib.pyplot as plt
import math
def secante_m (xi, d, f, n, tol):
    """
    xi: valor inicial
    d(delta): cambio fraccionario
    f: funcion
    n: iteraciones a realizar, se inserta cuando busca un numero de iteraciones especifico, si no usara, entonces n = 0
    tol: tolerancia, se inserta si busca tolerancia 0 o un valor prefijado en porcentaje
    xr(x_i+1)
    """
    m = 0
    xr = 0
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^11s} {:^11s}'.format('N', 'xi', 'x_i+1', 'f(xi)', 'f(xi + d)', 'ea(%)'))
    if n != 0:
        for i in range(n):
            m = m+1
            xran = xr
            if ((f(xi + d*xi)) - f(xi)) == 0:
                print(f'Division por 0 en la iteracion {m}')
                return None, m, None
                break
            xr = xi - ((d*xi*f(xi))/((f(xi + d*xi)) - f(xi)))
            ea = abs((((xr - xi)/xr))*100)
            print('{:^10}{:10f}{:11f}{:12f}{:11f}{:13f}'.format(m, xi, xr, f(xi), f(xi+d), ea))
            xi = xr
        print('Aproximacion Realizada por Numero de Iteraciones')
        print (f'Aproximacion hasta {n} iteracion(es): ', xr)
        return xr, m, False
    ea = 100
    if n==0:
        while ea > tol:
            m = m+1
            xran = xr
            if ((f(xi + d*xi)) - f(xi)) == 0:
                print(f'Division por 0 en la iteracion {m}')
                return None, m, None
                break
            xr = xi - ((d*xi*f(xi))/((f(xi + d*xi)) - f(xi)))
            ea = abs((((xr - xi)/xr))*100)
            print('{:^10}{:10f}{:11f}{:12f}{:11f}{:13f}'.format(m, xi, xr, f(xi), f(xi+d), ea))
            xi = xr
            if ea < tol:
                print('Aproximacion Realizada con Tolerancia')
                print (f'Aproximacion hasta la tolerancia {tol}%: ', xr)
                print(f'{m} iteraciones realizadas')
                return xr, m, True
                break    
            if math.isclose(0, ea, abs_tol=0.000000010):
                print('Aproximacion Realizada con Tolerancia')
                print('Solucion encontrada: ', xr)
                print(f'{m} iteraciones realizadas')
                return xr, m, True
                break

    return 

xi = 0.3
d = 0.001
f = (lambda x : 8*np.sin(x)* np.exp(-x) - 1)
g = f
n = 3
tol = 0
solucion, iteraciones, metodo = secante_m(xi, d, f, n, tol)
x = np.linspace(-xi*1.2, xi*1.2, 300)
plt.plot(x, f(x))
plt.scatter(solucion, 0, marker='*', s=120, color='green')
plt.axhline(y=0, ls='--', color='black', linewidth=0.9)
plt.axvline(x=0, ls='--', color='black', linewidth=0.9)
plt.legend(['Funcion $f(x)=0$', f'Aproximacion en {iteraciones}' + ' iteraciones: %.6f' %solucion])
plt.ylabel('f(x)')
plt.xlabel('x')
if metodo == False:
    plt.title('Metodo de la Secante Modificado\n(Mediante No. Iteraciones)')
if metodo == True:
    plt.title('Metodo de la Secante Modificado\n(Mediante Tolerancia Prefijada)')
plt.grid(color='black', linewidth=0.3)
plt.show()