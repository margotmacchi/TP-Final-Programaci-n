
"""
Crear un programa que cuando se ingresen datos por teclado se pueda 
seleccionar en un menú, opciones como: 
- Clasificar triángulos según lados o ángulos
- Calcular áreas o perímetros de algunas figuras geométricas como: triángulos, 
rectángulos, rombos y paralelogramos 
- Calcular ángulos interiores de un triángulo.
"""
import math
import numpy as np

#Clasificación de triángulos según la longitud de sus lados
def clasificar_triangulo_lados(a, b, c):
    """
    La función clasifica triangulos sabiendo la longitud de los lados a, 
    b y c
    """
    if a <= 0 or b <= 0 or c <= 0:
        print ("No es un dato válido para la longitud del lado de un \
triángulo (los lados deben ser mayores que cero).")
        return
    if not a + b > c and a + c > b and b + c > a:
        print ("No son datos válidos para un triángulo (la suma del primer \
y segundo lado debe ser mayor que el tercer lado ingresado).")
        return
    if a == b == c:
        print ("El triángulo es EQUILÁTERO")
    elif a == b or b == c or a == c:
        print ("El triángulo es ISÓSCELES")
    else:
        print ("El triángulo es ESCALENO")
#Clasificación de triángulos según la amplitud de sus ángulos
def clasificar_triangulo_angulos(d, e, f):
    """
    La función clasifica triangulos sabiendo la amplitud de sus ángulos
    d,e y f
    """
    if d <= 0 or e <= 0 or f <= 0:
        print ("No es un dato válido para la amplitud del ángulo de un \
triángulo (los ángulos deben ser mayores que cero).")
        return
    if d + e + f != 180:
        print ("No son datos válidos para un triángulo (la suma de los \
ángulos interiores del triángulo debe ser 180°).")
        return
    if d < 90 and e < 90 and f < 90:
        print ("El triángulo es ACUTÁNGULO")
    elif d == 90 or e == 90 or f == 90:
        print ("El triángulo es RECTÁNGULO")
    else:
        print ("El triángulo es OBTUSÁNGULO")
# Cálculo de ángulos en triángulos usando teorema del coseno
def calculo_angulos_del_triangulo(a, b, c):
    """
    La función calcula los ángulos interiores a, b y c del triángulo 
    usando teorema del coseno
    """
    angulo_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
    angulo_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
    angulo_c = math.degrees(math.acos((b**2 + a**2 - c**2) / (2*a*b)))
    return angulo_a, angulo_b, angulo_c
# Cálculo de perímetros
def perimetrorectangulo(a, b):
    """
    La función calcula el perímetro del rectángulo sabiendo la longitud 
    de la base a y la altura b
    """
    return round(np.add(np.multiply(2, a), np.multiply(2, b)))
def perimetrotriangulo(a, b, c):
    """
    La función calcula el perímetro del triángulo sabiendo la longitud 
    de sus lados
    """
    return round(np.add(np.add(a, b), c))
def perimetroparalelogramo(a, b):
    """
    La función calcula el perímetro del paralelogramo sabiendo la longitud 
    de la base a y el lado lateral
    """
    return round(np.add(np.multiply(2, a), np.multiply(2, b)))
def perimetrorombo(a):
    """
    La función calcula el perímetro del rombo sabiendo la longitud del lado
    a del rombo
    """
    return round(np.multiply(4, a))
# Cálculo de áreas
def area_rectangulo(a, b):
    """La función calcula el área del rectángulo sabiendo la longitud 
    de la base a y la altura b
    """
    return round(np.multiply(a, b), 2)
def area_triangulo(a, b):
    """
    La función calcula el área del triángulo sabiendo la longitud de la base a 
    y la altura b
    """
    return round(np.multiply(a, b) / 2, 2)
def area_paralelogramo(a, b):
    """
    La función calcula el área del paralelogramo sabiendo la longitud de la 
    base a y la altura b
    """
    return round(np.multiply(a, b), 2)
def area_rombo(a, b):
    """
    La función calcula el área del rombo sabiendo la longitud de la diagonal1 
    a y la diagonal2 b
    """
    return round(np.multiply(a, b) / 2, 2)
# Menú principal
while True:
    print("\n======================")
    print("\n   MENÚ PRINCIPAL")
    print("\n======================")
    print("1.- Clasificar triángulo según la longitud de sus lados")
    print("2.- Clasificar triángulo según la amplitud de sus ángulos")
    print("3.- Calcular área de figuras geométricas")
    print("4.- Calcular perímetro de figuras geométricas")
    print("5.- Calcular la amplitud de los ángulos interiores de un triángulo")
    print("0.- Salir")
    try:
        opcion = int(input("Elija una opción: "))
# CLASIFICACIÓN DE TRIÁNGULOS SEGÚN LADOS
        if opcion == 1:
            print("\nClasificación de Triángulos según longitud de sus lados")
            lado1 = float(input("Ingrese el lado 1 en cm: "))
            lado2 = float(input("Ingrese el lado 2 en cm: "))
            lado3 = float(input("Ingrese el lado 3 en cm: "))
            clasificar_triangulo_lados(lado1, lado2, lado3)
# CLASIFICACIÓN DE TRIÁNGULOS SEGÚN ÁNGULOS
        elif opcion == 2:
            print("\nClasificación de Triángulos según amplitud de sus ángulos")
            lado1 = float(input("Ingrese el ángulo 1 en grados: "))
            lado2 = float(input("Ingrese el ángulo 2 en grados: "))
            lado3 = float(input("Ingrese el ángulo 3 en grados: "))
            clasificar_triangulo_angulos(lado1, lado2, lado3)
# CÁLCULO DE ÁREAS
        elif opcion == 3:
            print("\n======================")
            print("\n    CALCULAR ÁREAS")
            print("\n======================")
            print("1.- Área del rectángulo")
            print("2.- Área del triángulo")
            print("3.- Área del paralelogramo")
            print("4.- Área del rombo")
            print("0.- Volver al menú principal")
            figura = int(input("Elija el cálculo que desea realizar: "))
# ÁREA RECTÁNGULO
            if figura == 1:
                base = float(input("Ingrese la longitud de la base del \
rectángulo en cm: "))
                altura = float(input("Ingrese la la longitud de la altura del \
rectángulo en cm: "))
                if base <= 0 or altura <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de la base y altura deben ser mayores que cero.")
                else:
                    resultado = area_rectangulo(base, altura)
                    print(f"El área del rectángulo de base {base}cm y altura \
{altura}cm, es: {resultado}cm²")
# ÁREA TRIÁNGULO
            elif figura == 2:
                base = float(input("Ingrese la base del triángulo en cm: "))
                altura = float(input("Ingrese la altura del triángulo en cm: "))
                if base <= 0 or altura <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de la base y altura deben ser mayores que cero.")
                else:
                    resultado = area_triangulo(base, altura)
                    print(f"El área del triángulo de base {base}cm y altura \
{altura}cm, es: {resultado}cm²")
# ÁREA PARALELOGRAMO
            elif figura == 3:
                base = float(input("Ingrese la base del paralelogramo en cm: "))
                altura = float(input("Ingrese la altura del paralelogramo en \
cm: "))
                if base <= 0 or altura <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de la base y altura deben ser mayores que cero.")
                else:
                    resultado = area_paralelogramo(base, altura)
                    print(f"El área del paralelogramo de base {base}cm y \
altura {altura}cm, es: {resultado}cm²")
# ÁREA ROMBO
            elif figura == 4:
                diagonal_1 = float(input("Ingrese la diagonal 1 en cm: "))
                diagonal_2 = float(input("Ingrese la diagonal 2 en cm: "))
                if diagonal_1 <= 0 or diagonal_2 <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de las diagonales deben ser mayores que cero.")
                else:
                    resultado = area_rombo(diagonal_1, diagonal_2)
                    print(f"El área del rombo de diagonales {diagonal_1}cm y \
{diagonal_2}cm, es: {resultado}cm²")
            elif figura == 0:
                continue  # Vuelve al menú principal
# CÁLCULO DE PERÍMETROS
        elif opcion == 4:
            print("\n============================")
            print("\n    CALCULAR PERÍMETROS")
            print("\n============================")
            print("1.- Perímetro del rectángulo")
            print("2.- Perímetro del triángulo")
            print("3.- Perímetro del paralelogramo")
            print("4.- Perímetro del rombo")
            print("0.- Volver al menú principal")
            dibujo = int(input("Elija el cálculo que desea realizar: "))
# PERÍMETRO RECTÁNGULO
            if dibujo == 1:
                base = float(input("Ingrese la base del rectángulo en cm: "))
                altura = float(input("Ingrese la altura del rectángulo en \
cm: "))
                if base <= 0 or altura <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de la base y altura deben ser mayores que cero.")
                else:
                    perimetro = perimetrorectangulo(base, altura)
                    print(f"El perímetro del rectángulo de base {base}cm y \
altura {altura}cm es: {perimetro}cm")
# PERÍMETRO TRIÁNGULO
            elif dibujo == 2:
                lado1 = float(input("Ingrese el lado 1 en cm: "))
                lado2 = float(input("Ingrese el lado 2 en cm: "))
                lado3 = float(input("Ingrese el lado 3 en cm: "))
                if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de los lados deben ser mayores que cero.")
                elif not (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 \
 and lado2 + lado3 > lado1):
                    print("No son datos válidos para un triángulo (la suma \
del primer y segundo lado debe ser mayor que el tercer lado ingresado")
                else:
                    perimetro = perimetrotriangulo(lado1, lado2, lado3)
                    print(f"El perímetro del triángulo de lados {lado1}cm, \
{lado2}cm y {lado3}cm; es: {perimetro}cm")
# PERÍMETRO PARALELOGRAMO
            elif dibujo == 3:
                lado_base = float(input("Ingrese la base del paralelogramo en \
cm: "))
                lado_lateral = float(input("Ingrese el lado lateral del \
paralelogramo en cm: "))
                if lado_base <= 0 or lado_lateral <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de los lados deben ser mayores que cero.")
                else:
                    perimetro = perimetroparalelogramo(lado_base, lado_lateral)
                    print(f"El perímetro del paralelogramo de lados \
{lado_base}cm y {lado_lateral}cm es: {perimetro}cm")
# PERÍMETRO ROMBO
            elif dibujo == 4:
                lado = float(input("Ingrese el lado del rombo en cm: "))
                if lado <= 0:
                    print("Los datos no son correctos, los valores de las \
longitudes de los lados deben ser mayores que cero.")
                else:
                    perimetro = perimetrorombo(lado)
                    print(f"El perímetro del rombo de lado {lado}cm es:\
{perimetro}cm")
            elif dibujo == 0:
                continue  # Vuelve al menú principal
# CÁLCULO DE ÁNGULOS INTERIORES DEL TRIÁNGULO
        elif opcion == 5:
            print("\nCálculo de ángulos interiores de triángulos")
            lado1 = float(input("Ingrese el lado 1 en cm: "))
            lado2 = float(input("Ingrese el lado 2 en cm: "))
            lado3 = float(input("Ingrese el lado 3 en cm: "))
            if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                print("No es un dato válido para la longitud del lado de un \
triángulo (los lados deben ser mayores que cero).")
            elif not (lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or \
            lado2 + lado3 > lado1):
                print("No son datos válidos para un triángulo (la suma del \
primer y segundo lado debe ser mayor que el tercer lado ingresado.")
            else:
                AnguloA, AnguloB, AnguloC= calculo_angulos_del_triangulo\
(lado1, lado2, lado3)
                print(f"La amplitud del ángulo 'A' es: {round(AnguloA, 0)}°")
                print(f"La amplitud del ángulo 'B' es: {round(AnguloB, 0)}°")
                print(f"La amplitud del ángulo 'C' es: {round(AnguloC, 0)}°")
        elif opcion == 0:
            print("Fin del programa, esperamos te haya sido útil. ¡Hasta \
luego!.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("CUIDADO: Entrada NO VALIDA.. Revisá las medidas e ingresá solo \
números.")
# PREGUNTAR SI DESEA CONTINUAR
    repetir = input("\n¿Querés realizar otro cálculo? (S/N): ").lower()
    if repetir != "s":
        print("¡Hasta luego!")
        break
