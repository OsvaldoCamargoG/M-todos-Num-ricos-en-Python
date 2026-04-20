import numpy as np
import matplotlib.pyplot as plt
import math
def aproximacion(xi, tol, f, df, N):
    """
    xi: valor inicial
    ea: error absoluto porcentual
    tol: tolerancia porcentual
    f: funcion
    df: derivada de la funcion
    N: numero maximo de iteraciones
    """
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.format('N', 'xi', 'f(xi)', '(df/dx)', '(xi+1)','Error'))
    if df == 0:
        print ('La derivada debe de ser distinta de 0')
        return None, 0, False

    for n in range (1, N+1):
        x = xi -(f(xi)/ df(xi))
        ea = abs(((x - xi)/x)*100)
        print('{:10f} {:10f} {:10f} {:10f} {:10f} {:10f}'.format(n, xi, f(xi), df(xi), x, ea))
        xi = x
        
        if ea < tol:
            return xi, N, True
            break 
    
    return 
xi = 0.55
N = 200
tol = 0.0010
def f(x):
    return (8*np.sin(x)*np.exp(-x)) - 1
def df(x):
    return 8*((np.exp(-x)*np.cos(x)) - (np.exp(-x)*np.sin(x)))
solucion, iteraciones, convergencia = aproximacion(xi, tol, f, df, N)
if convergencia == True:
    x = np.linspace (-15, 15, 200)
    y = f(x)
    plt.plot (x, y)
    plt.scatter(solucion, 0, color='green', s = 20, label='Raiz aproximada')
    plt.legend (['Funcion', 'Raiz aproximada'])
    plt.title('Aproximacion')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.text(solucion, 0, solucion, color='green' )
    plt.grid('black', linewidth=0.3)
    plt.show()
