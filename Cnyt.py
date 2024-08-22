from math import pi as pi

from math import atan2 as arctan

global e

e = 2.718281828459045

def Suma(n1, n2):
    """
    Arg n1: Primer número complejo
    Arg n2: Segundo número complejo
    Return: Número complejo resultante
    """
    real1, imaginario1 = n1[0], n1[1]
    real2, imaginario2 = n2[0], n2[1]
    real3 = real1 + real2
    imaginario3 = imaginario1 + imaginario2
    return [real3, imaginario3]

def Producto(n1, n2):
    """
    Arg n1: Primer número complejo
    Arg n2: Segundo número complejo
    Return: Número complejo resultante
    """
    real1, imaginario1 = n1[0], n1[1]
    real2, imaginario2 = n2[0], n2[1]
    real3 = (real1 * real2) - (imaginario1 * imaginario2)
    imaginario3 = (real1 * imaginario2) + (real2 * imaginario1)
    return [real3, imaginario3]

def Resta(n1, n2):
    """
    Arg n1: Primer número complejo
    Arg n2: Segundo número complejo
    Return: Número complejo resultante
    """
    real1, imaginario1 = n1[0], n1[1]
    real2, imaginario2 = n2[0], n2[1]
    real3 = real1 - real2
    imaginario3 = imaginario1 - imaginario2
    return [real3, imaginario3]

def Division(n1, n2):
    """
    Arg n1: Primer número complejo
    Arg n2: Segundo número complejo
    Return: Número complejo resultante
    """
    real1, imaginario1 = n1[0], n1[1]
    real2, imaginario2 = n2[0], n2[1]
    piv = (real2**2) + (imaginario2**2)
    real3, imaginario3 = 0, 0
    try:
        real3 = ((real1 * real2) + (imaginario1 * imaginario2)) / piv
        imaginario3 = ((real2 * imaginario1) - (real1 * imaginario2)) / piv
        return [real3, imaginario3]
    except ZeroDivisionError as error:
        print("Error:", error)

def Modulo(n):
    """
    Arg n: Número complejo
    Return c: Valor del módulo del número
    """
    real, imaginario = n[0], n[1]
    real = real**2
    imaginario = imaginario**2
    c = (real + imaginario)**(1/2)
    
    return c

def Conjugado(n):
    """
    Arg n: Número complejo
    Return: Conjugado
    """
    return [n[0], -n[1]]

def Sen(x):
    """
    Arg x: En radianes, el número del que se desea hallar el seno
    Return s: Seno de x
    """
    global e
    s = (e**(x*1j)).imag
    return s

def Cos(x):
    """
    Arg x: En radianes, el número del que se desea hallar el coseno
    Return c: Coseno de x
    """
    global e
    c = (e**(x*1j)).real
    return c

def Polar_Car(coord):
    """
    Arg coord: Coordenadas polares
    Return: Coordenada cartesiana
    """
    r, t = coord[0], coord[1]
    x = r * (Cos(t))
    y = r * (Sen(t))
    return [x, y]

def Car_Polar(coord):
    """
    Arg coord: Coordenada cartesiana
    Return: Coordenada polar
    """
    x, y = coord[0], coord[1]
    r = ((x**2) + (y**2))**(1/2)
    t = Fase([x, y])
    return [r, t]

def Fase(n):
    """
    Arg n: Número complejo
    Return f: Fase del número
    """
    real, imaginario = n[0], n[1]
    f = arctan(imaginario, real)
    if real < 0:
        f += pi
    elif real >= 0 and imaginario < 0:
        f += 2 * pi
    return f
