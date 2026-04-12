import numpy as np 
import matplotlib.pyplot as plt
def Biseccion (f, xl, xu, es, N):
    
    """
    f: funcion
    xl: valor de intervalo inferior
    xu: valor superior
    es: tolerancia porcentual (aun no incluida)
    N: numero maximo de iteraciones
    """
    if f(xl)*f(xu) > 0:
        print ('La función debe cambiar de signo en [xl, xu]')
        return None, 0, True
    
    xr = 0
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.format('Valor inicial', 'Valor final', 'Raiz anterior', 'Raiz actual', 'Error'))

    for i in range (1, N + 1):
        xran = xr
        xr = (xl + xu)/2

        if f(xl)*f(xr) < 0:
            xu = xr

        if f(xl)*f(xr) > 0:
            xl = xr

        if f(xl)*f(xr) == 0:
            print ('Solucion encontrada en ', i, ' iteraciones')
            print ('Solucion: ', xr)
            return xr, N
        
        if f(xl)*f(xr)<0 and f(xl)*f(xr)>0 and f(xl)*f(xr) ==0 : 
            print('Solucion no encontrada en ', N, ' iteraciones')
        

        ea = abs((((xr- xran)/xr))*100)
        #print('Error \n--', ea)
        print('{:10.5f} {:12f} {:12f} {:12f} {:11f}'.format(xl, xu, xr, xran, ea))
        if ea < es:
                print ('Se alcanzo la tolerancia: ', es, ' %')
                print ('Solucion hasta la tolerancia: ', xr)
                break
        
        
    return xr, N, False


def f(x):
    return -25 + 82*x - 90*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5
xl = 0.5
xu = 1.0
#-25 + 82*x - 92*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5
N = 400
es = 10 #cantidad en porcentaje
solucion, iteraciones, convergencia = Biseccion(f, xl, xu, es, N)
print (convergencia)
if convergencia == False:
    x = np.linspace (xl-xu, xu+1, 500)
    plt.plot (x, f(x))
    plt.scatter(solucion, 0, color='red', s=20, label='Raiz')
    plt.legend(['Funcion', 'Raiz '])
    plt.title('Aproximación por Biseccion')
    plt.grid("black",linewidth=0.3)
    plt.show()