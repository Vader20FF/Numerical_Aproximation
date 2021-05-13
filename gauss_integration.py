import numpy as np
from function_value import get_function_value


def calculate_integral(function_number, nodes_number):
    result, currentWeight, currentNode = 0, 0, 0
    for i in range(1, nodes_number + 1):
        currentWeight = np.pi / nodes_number
        currentNode = -np.cos(((2 * i - 1) * np.pi) / (2 * nodes_number))
        result += currentWeight * get_function_value(currentNode, function_number)
    return result
