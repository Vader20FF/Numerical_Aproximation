from sys import exit as exit_program
from graph import generate_graph
from function_value import get_function_value
from gauss_integration import calculate_integral
import numpy as np


def menu():
    while True:
        print("""
        
-------------------------------------------------------------------------        
Metoda aproksymacji oparta o wielomiany Czebyszewa
Lukasz Janiszewski, Maciej Kubis""")
        print("""
Wybierz opcję:
1. Rozpocznij program
2. Zakończ program""")
        user_choice = int(input("""
Wybór: """))
        if user_choice == 1:
            data_load()
        elif user_choice == 2:
            exit_program()
        else:
            print("""Wybrano nieprawidlowa opcje!""")


def data_load():

    # Numer funkcji
    print("""
Wybierz numer funkcji ktorej chcesz uzyc w programie:
    1. FUNKCJA LINIOWA: x - 3
    2. FUNKCJA: |x|
    3. FUNKCJA WIELOMIANOWA:  2 * x^3 + 1 * x^2 - 3 * x + 7
    4. FUNKCJA TRYGONOMETRYCZNA:  4 * cos(x) + 6 * sin(x)
    5. FUNKCJA ZŁOŻONA:  |sin(x + 2) - 1.6|""")
    function_number = int(input("""
Wybór: """))
    while function_number not in [1, 2, 3, 4, 5]:
        valid_number = False
        while not valid_number:
            function_number = int(input("""
                Wybierz jeszcze raz numer funkcji: """))
            if function_number in [1, 2, 3, 4, 5]:
                valid_number = True

    # Przedział aproksymacji
    left_border = float(input("""
Podaj lewa granice przedziału aproksymacji: """))
    right_border = float(input("""Podaj prawa granice przedziału aproksymacji: """))

    # Stopień wielomianu aproksymujacego
    polynomial_degree = int(input("""
Podaj stopien wielomianu aproksymacji: """))
    while polynomial_degree < 1:
        print("Podaj stopień wielomianu większy od 0!")
        polynomial_degree = int(input("""
Podaj stopien wielomianu aproksymacji: """))

    # Liczba wezlow dla metody calkowania Gaussa-Czebyszewa
    nodes_number = int(input("""
Podaj liczbe wezlow dla metody calkowania (Gauss-Czebyszew): """))
    while nodes_number < 0:
        print("Podaj liczbe wezlow wieksza od 0!")
        nodes_number = int(input("""
Podaj liczbe wezlow dla metody calkowania (Gauss-Czebyszew): """))

    function_arguments = list(np.linspace(left_border, right_border, 1000))

    function_values = []
    for x in function_arguments:
        function_values.append(get_function_value(x, function_number))

    generate_graph(function_arguments, function_values, function_number, True, None, None)

    calculated_values = calculations(function_number, left_border, right_border, polynomial_degree, nodes_number)

    print()
    print("Blad aproksymacji wynosi:", calculated_values[0])

    generate_graph(function_arguments, function_values, function_number, calculated_values[1], calculated_values[2])


def calculations(function_number, left_border, right_border, polynomial_degree, nodes_number):
    segment = 100
    epsilon = 0.0
    current_x = 0
    current_y = 0
    approximated_arguments = []
    approximated_values = []

    for i in range(segment):
        current_x = left_border + 1.0 * i / segment * (right_border - left_border)
        current_y = calculate_integral(current_x, function_number, nodes_number, polynomial_degree)
        approximated_arguments.append(current_x)
        approximated_values.append(current_y)
        epsilon = epsilon + abs(get_function_value(current_x, function_number) - current_y)
    epsilon /= 100

    return [epsilon, approximated_arguments, approximated_values]


##########################################################################
# START
##########################################################################
menu()
