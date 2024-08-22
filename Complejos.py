import math

def Suma(n1, n2):
    """
    Arg n1: Primera coordenada cartesiana
    Arg n2: Segunda coordenada cartesiana
    Return: Coordenada cartesiana resultante de la suma
    """
    pr = round(n1[0] + n2[0], 2)
    pi = round(n1[1] + n2[1], 2)
    return pr, pi

def Producto(n1, n2):
    """
    Arg n1: Primera coordenada cartesiana
    Arg n2: Segunda coordenada cartesiana
    Return: Coordenada cartesiana resultante del producto
    """
    pr = round(n1[0]*n2[0] - n1[1]*n2[1], 2)
    pi = round(n1[0]*n2[1] + n2[0]*n1[1], 2)
    return pr, pi

def Resta(n1, n2):
    """
    Arg n1: Primera coordenada cartesiana
    Arg n2: Segunda coordenada cartesiana
    Return: Coordenada cartesiana resultante de la resta
    """
    pr = round(n1[0] - n2[0], 2)
    pi = round(n1[1] - n2[1], 2)
    return pr, pi

def Division(n1, n2):
    """
    Arg n1: Numerador en coordenadas cartesianas
    Arg n2: Denominador en coordenadas cartesianas
    Return: Coordenada cartesiana resultante de la división
    """
    denominator = n2[0]**2 + n2[1]**2
    if denominator == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    pr = round((n1[0]*n2[0] + n1[1]*n2[1]) / denominator, 2)
    pi = round((n2[0]*n1[1] - n1[0]*n2[1]) / denominator, 2)
    return pr, pi

def Modulo(n):
    """
    Arg n: Coordenada cartesiana
    Return: Módulo de la coordenada cartesiana
    """
    num = round((n[0]**2 + n[1]**2)**0.5, 2)
    return num

def Conjugado(n):
    """
    Arg n: Coordenada cartesiana
    Return: Conjugado de la coordenada cartesiana
    """
    return round(n[0], 2), round(n[1] * -1, 2)

def Fase(n):
    """
    Arg n: Coordenada cartesiana
    Return: Fase de la coordenada cartesiana
    """
    if n[1] == 0:
        if n[0] > 0:
            angle = 0
        elif n[0] < 0:
            angle = math.pi
        else:
            raise ZeroDivisionError("Division by zero is not allowed")
    elif n[0] == 0:
        angle = math.pi/2 if n[1] > 0 else -math.pi/2
    else:
        angle = round(math.atan(n[1]/n[0]), 2)
    return angle

def Polar_Car(coord):
    """
    Arg coord: Coordenada cartesiana
    Return: Coordenada polar
    """
    pr = round(Modulo(coord), 2)
    pi = round(Fase(coord), 2)
    return pr, pi

def Car_Polar(coord):
    """
    Arg coord: Coordenada polar
    Return: Coordenada cartesiana
    """
    pr = round(coord[0] * math.cos(coord[1]), 2)
    pi = round(coord[0] * math.sin(coord[1]), 2)
    return pr, pi

