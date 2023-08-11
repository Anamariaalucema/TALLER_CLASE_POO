import math 
class Vehiculo: 
    def __init__(self, velocidad_maxima, kilimetraje): 
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje 

class Punto: 
    def __init__(self, punto_eje_x, punto_eje_y): 
        self.punto_eje1_x = punto_eje_x
        self.punto_eje1_y = punto_eje_y 
        self.punto_eje2_x = punto_eje_x
        self.punto_eje2_y = punto_eje_y 

    def mostrar(self): 
        self.punto_eje_x= float(input("escriba el punto del eje x en el plano: "))
        self.punto_eje_y= float(input("escriba el punto del eje y en el plano: "))
        print(f"las coordenadas del punto son ({self.punto_eje1_x},{self.punto_eje1_y})")

    def mover(self): 
        mover= int(input("desea cambiar las coordenadas del punto: 1. para si 2. para no"))
        if mover == 1: 
            self.punto_eje1_x= float(input("defina el nuevo punto para el eje x en el plano: "))
            self.punto_eje1_y= float(input("defina el nuevo punto para el eje y en el plano: "))
            print(f"las coordenadas del punto son ({self.punto_eje1_x},{self.punto_eje1_y})")
        else: 
            print("las coordenadas van a quedar como estaban")

    def clacular_distancia(self): 
        self.punto_eje2_x = punto_eje_x= float(input("escriba las coordenadas para el segundo punto del eje x en el plano: "))
        self.punto_eje2_y = punto_eje_y = float(input("escriba las coordenadas para el segundo punto del eje y en el plano: "))
        calcular = (self.punto_eje2_x - self.punto_eje1_x)**2 * (self.punto_eje2_y - self.punto_eje1_y)**2 
        calcular_raiz = math.sqrt(calcular)
        print (f"las distancia de los dos puntos son: {calcular_raiz}") 

class Rectangulo: 
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self): 
        self.lado1 = float(input("defina el largo del rectangulo")) 
        self.lado2 = float(input("defina el ancho del rectangulo")) 
        area = self.lado1 * self.lado2
        print(f"el area del rectangulo es: {area}")

    def calcular_perimetro(self):
        perimetro = 2*self.lado1 + 2*self.lado2 
        print(f"el perimetro del rectangulo es: {perimetro}")

    def rectangulo_cuadrado(self): 
        if self.lado1 == self.lado2: 
            print("el rectangulo es una cuadrado ya que sus lados son iguales") 
        else: 
            print("el rectangulo si lo es ya que su largo y ancho son diferentes") 

class Circulo: 
    def __init__(self, centro, radio): 
        self.centro = centro
        self.radio = radio 

    def area_circulo(self): 
        self.radio = float(input("defina el radio del circulo"))
        pi = 3.14
        area = pi * (self.radio)**2 
        print(f"el area del circulo es: {area}") 

    def perimetro_circulo(self): 
        pi = 3.14
        perimetro = pi * self.radio *2 
        print(f"el area del circulo es: {perimetro}") 

    def punto_circulo(self): 
        punto = float(input("que distancia hay de un punto al centro"))
        if punto != self.radio: 
            print("el punto no pertenece al circulo")
        else: 
            print("el punto si pertenece al circulo")