import numpy as np
import matplotlib.pyplot as plt
import math
def aproximacion(xi, tol, f, df):
    """
    xi: valor inicial
    ea: error absoluto porcentual
    tol: tolerancia porcentual
    f: funcion
    df: derivada de la funcion
    N: numero maximo de iteraciones
    """

    ea = 100
    n = 0
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.format('N', 'xi', 'x_i+1', 'f´(xi)', 'f(xi)','Error'))
    if df == 0:
        print ('La derivada debe de ser distinta de 0')
        return None, 0, False
    while ea > tol: 
        n = n+1
        x = xi -(f(xi)/ df(xi))
        ea = abs(((x - xi)/x)*100)
        print('{:^10} {:10f} {:10f} {:10f} {:10f} {:10f}'.format(n, xi, x, df(xi), f(xi), ea))
        xi = x

        if ea < tol:
            return xi, N+n, True
            break 
        if math.isclose(0, ea, abs_tol=0.00000001):
            return xi, n, True
            break
    
    return 
xi = 1.5
tol = 0
def f(x):
    return x*np.exp(0.5*x) + 1.2*x - 5
def df(x):
    return np.exp(0.5*x) + 0.5*x*np.exp(0.5*x) + 1.2
solucion, iteraciones, convergencia = aproximacion(xi, tol, f, df)
if convergencia == True:
    x = np.linspace (-15, 15, 200)
    y = f(x)
    plt.plot (x, y)
    plt.scatter(solucion, 0, color='green', marker='*',s = 80)
    plt.legend (['Funcion $f(x)=0$', 'Raiz aproximada: %.6f' %solucion])
    plt.title('Metodo Newton-Rapshon')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.grid('black', linewidth=0.3)
    plt.show()
