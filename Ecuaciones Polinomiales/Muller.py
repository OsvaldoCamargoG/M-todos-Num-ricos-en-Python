import numpy as np 
import matplotlib.pyplot as plt
import math
import cmath

def Muller(f, x0, x1, x2, tol):
    """
    x0, x1 y x2: valores iniciales de x
    f: funcion polinomica
    tol: tolerancia porcentual
    """
    k = 0
    ea = 100
    #s significa cadena
    print('{:^10s}{:^19s}{:^19s}{:^19s}{:^19s}{:^19s}'.format('N', 'x0', 'x1', 'x2','x_3', 'ea(%)'))
    while ea > tol:
        k = k + 1

        #variaciones y evaluacion de la funcion en los valores de x
        h0 = x1 - x0
        h1 = x2 - x1
        f0 = f(x0)
        f1 = f(x1)
        f2 = f(x2)
        d0 = (f1 - f0)/h0
        d1 = (f2 - f1)/h1

        #coeficientes de la parabola
        a = (d1 - d0)/(h1 + h0)
        b = a*h1 + d1
        c = f2
        n = b + cmath.sqrt(b**2 - (4*a*c))
        n1 = b - cmath.sqrt(b**2 - (4*a*c))
        n_n1 = np.array([n, n1])
        m = b**2 - (4*a*c)
        if n == 0 or n1 == 0:
            print(f'Error, se a presentado una division por cero en la obtencion de x3 en la iteracion {k}')
            print('b + sqrt(b^2 - (4*a*c)) = ', n)
            print('b - sqrt(b^2 - (4*a*c)) = ', n1)
            print('b^2 - (4*a*c) = ', m)
            print(f'Ultima solucion obtenida {x2}')
            return x2, k, None
            break

        #eleccion de la raiz
        criterio = np.iscomplex(n_n1)
        if criterio[0] == True:
            d = cmath.sqrt(b**2 - (4*a*c))
            D1 = b + d
            D2 = b - d
            if b.real > 0:
                x3 = x2 + (-2*c)/D1
            else:
                x3 = x2 + (-2*c)/D2
        if criterio[0] == False:
            d = math.sqrt(b**2 - (4*a*c))
            D1 = b + d
            D2 = b - d
            if b > 0:
                x3 = x2 + (-2*c)/D1
            else:
                x3 = x2 + (-2*c)/D2

        #error absoluto
        ea = abs((x3 - x2)/x3)*100
        print('{:^10}{:^19f}{:^19f}{:^19f}{:^19f}{:^19f}'.format(k, x0, x1, x2, x3, ea))

        #actualizacion de los valores
        x0 = x1
        x1 = x2
        x2 = x3

        if ea < tol:
            print(f'Tolerancia alcanzada ({tol}%)')
            print('Solucion:  ', x3)
            return x3, k, criterio[0]
            break
        if math.isclose(0, ea, abs_tol=0.000000001):
            print('Solucion encontrada: ', x3)
            return x3, k, criterio[0]
            break

    return
"""
prueba raices complejas
def f(x):
    return x**3 + 1 
x0 = -1
x1 = 2
x2 = 3
reales
f = (lambda x : x**3 + x**2 - 4*x - 4)
x0 = 1
x1 = 1.5
x2 = 1.8
"""
#declaracion de varible y parametros
#f = (lambda x : x**3 + 1)
def f(x):
    return x**3 + x**2 - 4*x - 4
x0 = 1
x1 = 1.5
x2 = 1.8
tol = 0
solucion, iteraciones, RoC = Muller(f, x0, x1, x2, tol)

if RoC == True:
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    F = np.abs(f(Z)) 
    plt.figure(figsize=(8, 8))
    cp = plt.contourf(X, Y, F, levels=50, cmap='viridis_r')
    plt.colorbar(cp, label='f(z)')
    angulo = np.linspace(0, 2*np.pi, 100)
    plt.plot(np.cos(angulo), np.sin(angulo), 'black', alpha=0.5, label='Círculo Unitario')
    plt.scatter(solucion.real, solucion.imag,  color='red', edgecolor='black', s=100, zorder=5, label='Soluciones (Raíces)')
    plt.axhline(y=0, ls='--', color='black', linewidth=0.9)
    plt.axvline(x=0, ls='--', color='black', linewidth=0.9)
    plt.title('Solucion Compleja')
    plt.xlabel('Parte Real (Re)')
    plt.ylabel('Parte Imaginaria (Im)')
    plt.legend()
    plt.gca().set_aspect('equal')
    plt.grid(linewidth=0.3, color='black')
    plt.show()

if RoC == False:
    x = np.linspace(solucion*-1.5, solucion*1.5, 200)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.scatter(solucion, 0, s = 100, marker='*', color='green')
    plt.axhline(y=0, ls='--', color='black', linewidth=0.9)
    plt.axvline(x=0, ls='--', color='black', linewidth=0.9)
    plt.legend(['Funcion f(x)', f'Aproximacion: {solucion}'])
    plt.title('Metodo de Muller')
    plt.grid(linewidth=0.3, color='black')
    plt.show()