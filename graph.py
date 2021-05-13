import matplotlib.pyplot as plt
from function_formula import get_function_formula


def generate_graph(function_arguments, function_values, function_number, aproximation_arguments,
                   aproximation_values):
    """
    Function generating a graph with given data
    :param function_arguments: arguments for the original function graph
    :param function_values: values for the original function graph
    :param function_number: a number of the given function
    :param aproximation_arguments: arguments for the aproximation polynomial
    :param aproximation_values: values for the aproximation polynomial
    :return: None
    """
    plt.plot(function_arguments, function_values, label='wykres funkcji f(x)')
    plt.title('f(x)=' + str(get_function_formula(function_number)))
    plt.plot(aproximation_arguments, aproximation_values, linestyle=":", label='wielomian aproksymujacy')
    plt.legend(loc='best')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
