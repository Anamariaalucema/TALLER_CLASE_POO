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

class Carta: 
    def __init__(self, valor, pinta): 
        self.valor = valor
        self.pinta = pinta 

    pinta1 = "pica"
    pinta2 = "corazon"
    pinta3 = "trebol"
    pinta4 = "diamante"

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance, plata): 
        self.numero_cuenta = 30
        self.propietarios = 2
        self.balance = 50 
        self.plata = 0

    def depositar(self): 
        cuenta = int(input("a que numero de cuenta desea depositar la plata"))
        plata = float(input(f"cuanto desea depositar en la cuenta {cuenta}"))
        if cuenta == self.numero_cuenta: 
            self.plata = self.plata + plata 
            print(f"la plata se deposito en la cuenta: {cuenta} y ahora hay {self.plata} pesos en la cuenta")
        else: 
            print(f"la cuenta {cuenta} no exite o no fue encontrada")

    def retirar(self):
        cuenta =int(input("cual es el numero de la cuenta de la cual desea retirar")) 
        retirar = float(input("cuanta desea retirar de la cuenta"))
        if cuenta == self.numero_cuenta: 
            if self.plata >= plata: 
                self.plata = self.plata - retirar 
                print(f"la plata se retiro exitosamente, la plata restante es: {self.plata}pesos")
            else: 
                print("no hay suficiente plata en la cuenta para retirar en esa cuenta")
        else: 
            print(f"la cuenta {cuenta} no existe o no fue encontrada") 

    def cuota_manejo(self): 
        cuenta = int(input("cual es numero de la cuenta que va a pagar "))
        if cuenta == self.numero_cuenta: 
            pagar = self.plata + 2/100 
            print(f"tiene que pagar {pagar}")
        else: 
            print("esa cuenta no existe")

    def mostrar_detalles(self): 
        cuenta = int(input("cual es el numero de la cuenta"))
        if cuenta == self.numero_cuenta: 
            print(f"esta es la informacio de la cuenta: numero= {self.numero_cuenta}, propietarios= {self.propietarios}, cantidad de plata = {self.plata}, balance = {self.balance}")
