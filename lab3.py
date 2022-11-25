import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from tabulate import tabulate

n = 7

x = np.array([1.383, 1.357, 1.39, 1.394, 1.396, 1.4, 1.404])
y = np.array([9.05421, 8.76431, 7.11326, 6.87628, 7.36734, 8.10234, 9.21361])

print(tabulate({"X": x,
                "Y": y}, headers="keys", tablefmt="pretty"))
print('\n')
f = lagrange(x, y)
print(f"Lagrange Polynomial: ")
print (f)

x_new = np.arange(1.3, 1.45, 0.01)
fig = plt.figure(figsize = (10,8))
plt.plot(x_new, f(x_new), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()