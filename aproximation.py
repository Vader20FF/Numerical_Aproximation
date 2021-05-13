from gauss_integration import calculate_integral
import numpy


def czebyszew_aproximation(polynomial_degree, argument, function_number):
    if polynomial_degree == 0:
        return 1
    elif polynomial_degree == 1:
        return argument
    return (2 * argument * czebyszew_aproximation(polynomial_degree - 1, argument, function_number) -
            czebyszew_aproximation(polynomial_degree - 2, argument, function_number))


def calculate_aproximation(argument, function_number, polynomial_degree, nodes_number):
    result = 1.0 / 2.0 * 2.0 / numpy.pi * calculate_integral(argument, function_number, nodes_number, polynomial_degree)
    for i in range(1, polynomial_degree + 1):
        result = result + 2.0 / numpy.pi * calculate_integral(argument, function_number, nodes_number,
                                                              polynomial_degree)
    return result
