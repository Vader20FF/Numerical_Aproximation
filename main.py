from sys import exit as exitProgram
from graph import generate_graph
from function_value import get_function_value
from horner import get_polynomial_value
from gauss_integration import calculate_integral
import numpy as np
import sympy as sp


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
            exitProgram()
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
    nodes_number = float(input("""
        Podaj liczbe wezlow dla metody calkowania (Gauss-Czebyszew): """))
    while nodes_number < 0:
        print("Podaj liczbe wezlow wieksza od 0!")
        nodes_number = float(input("""
        Podaj liczbe wezlow dla metody calkowania (Gauss-Czebyszew): """))

    # NA 5: Oczekiwany błąd aproksymacji
    aproximation_error = float(input("""
        Podaj oczekiwany blad aproksymacji: """))
    while aproximation_error < 0:
        print("Podaj oczekiwany blad aproksymacji wiekszy od 0!")
        aproximation_error = float(input("""
        Podaj oczekiwany blad aproksymacji: """))

    calculations(function_number, nodes_number)


def calculations(function_number, nodes_number):
    print()
    print("Wartosc dla metody Gaussa-Czebyszewa:", round(calculate_integral(function_number, nodes_number), 6))
    print()


##########################################################################
# START
##########################################################################
menu()
