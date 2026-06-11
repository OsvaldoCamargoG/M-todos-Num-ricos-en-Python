import numpy as np 
import matplotlib.pyplot as plt
import math
def Biseccion (f, xl, xu, es):
    
    """
    f: funcion
    xl: valor de intervalo inferior
    xu: valor superior
    es: tolerancia porcentual
   
    """
    if f(xl)*f(xu) > 0:
        print ('La función debe cambiar de signo en [xl, xu]')
        return None, 0, True
    
    xr = 0
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.format('Valor inicial', 'Valor final', 'Raiz anterior', 'Raiz actual', 'Error'))
    ea = 100
    while ea > es:
        xran = xr
        xr = (xl + xu)/2

        if f(xl)*f(xr) < 0:
            xu = xr

        if f(xl)*f(xr) > 0:
            xl = xr

        if f(xl)*f(xr) == 0:
            
            break
            return xr, False
        ea = abs((((xr- xran)/xr))*100)
        print('{:10.5f} {:12f} {:12f} {:12f} {:11f}'.format(xl, xu, xran, xr, ea))
        if ea < es:
            print ('Se alcanzo la tolerancia: ', es, ' %')
            print ('Solucion hasta la tolerancia: ', xr)
            break
        if math.isclose (0, ea, abs_tol=0.00000010):
            #print ('Solucion encontrada en ', i, ' iteraciones')
            print ('Solucion encontrada: ', xr)
            break
      
        
    return xr, False


def f(x):
    return  -0.5*x**2 + 2.5*x + 4.5
xl = 5
xu = 10
#-25 + 82*x - 92*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5
es = 10 #cantidad en porcentaje
solucion, convergencia = Biseccion(f, xl, xu, es)
print (convergencia)
if convergencia == False:
    x = np.linspace (xl-xu, xu+1, 500)
    plt.plot (x, f(x))
    plt.scatter(solucion, 0, color='green', s=20, label='Raiz')
    plt.legend(['Funcion', 'Raiz '])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.text(solucion, 0, solucion, color='green' )
    plt.title('Aproximación por Biseccion')
    plt.grid("black",linewidth=0.3)
    plt.show()
