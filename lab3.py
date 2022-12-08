import numpy as np
from tabulate import tabulate

x_values = np.array([1.383, 1.357, 1.39, 1.394, 1.396, 1.4, 1.404])
y_values = np.array([9.05421, 8.76431, 7.11326, 6.87628, 7.36734, 8.10234, 9.21361])
INT_POINT = 1.38
EXT_POINT = 1.45


def create_basic_polynomial(x_values, i):
    def basic_polynomial(x):
        divider = 1
        result = 1
        for j, _ in enumerate(x_values):
            if j != i:
                result *= (x-x_values[j])
                divider *= (x_values[i]-x_values[j])
        return result/divider
    return basic_polynomial


def create_lagrange_polynomial(x_values, y_values):
    basic_polynomials = []
    for i in range(len(x_values)):
        basic_polynomials.append(create_basic_polynomial(x_values, i))
        

    def lagrange_polynomial(x):
        result = 0
        for i, y_val in enumerate(y_values):
            result += y_val * basic_polynomials[i](x)
        return result
    return lagrange_polynomial

lag_pol = create_lagrange_polynomial(x_values, y_values)
results = [lag_pol(x) for x in x_values]
delta = [y_values[i] - results[i] for i in range(len(x_values))]

print(tabulate({"X(i)": x_values,
                "Y(i)": [y for y in y_values],
                "L(i))": [res for res in results],
                "delta = Y(i) - L(i)": [f'{d:.6f}' for d in delta]},
                headers="keys", tablefmt="pretty"))

print(f"The value of Lagrange Polynomial in {INT_POINT} = ")
tmp = lag_pol(INT_POINT)
print(tmp)
print()

print(f"The value of Lagrange Polynomial in {EXT_POINT} = ")
tmp = lag_pol(EXT_POINT)
print(tmp)
print()
