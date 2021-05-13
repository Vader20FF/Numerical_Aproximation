import matplotlib.pyplot as plt
from function_formula import get_function_formula


def generate_graph(function_arguments, function_values, function_number, before_calculation, aproximation_arguments,
                   aproximation_values):
    """
    Function generating a graph with given data
    :param function_arguments: arguments for the whole graph
    :param function_values: values for the function graph
    :param function_number: a number of the given function
    :param before_calculation:
    :param aproximation_arguments:
    :param aproximation_values:
    :return: None
    """
    plt.plot(function_arguments, function_values, label='wykres funkcji f(x)')
    plt.title('f(x)=' + str(get_function_formula(function_number)))
    # if not before_calculation:
    #     plt.scatter(aproximation_arguments, interpolation_values, label='węzły interpolacji')
    #     plt.plot(function_arguments, aproximation_values, linestyle=":", label='wielomian interpolacji')
    plt.legend(loc='best')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()
