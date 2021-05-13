import numpy as np
from function_value import get_function_value
from aproximation import czebyszew_aproximation


def calculate_integral(function_number, nodes_number, polynomial_degree):
    result, currentWeight, currentNode = 0.0, None, None
    for i in range(1, nodes_number + 1):
        currentWeight = np.pi / nodes_number
        currentNode = -np.cos(((2 * i - 1) * np.pi) / (2 * nodes_number))
        result += currentWeight * get_function_value(currentNode, function_number) * \
                  czebyszew_aproximation(polynomial_degree, currentNode, function_number)
    return result
