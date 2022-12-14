'''
Решение задач коши методов Рунге-Кутта, Эйлера
вариант 3: y' = f(x, y)
y(x0) = y0
1) С выбранным шагом h=0.05 начиная с точки x0 вычислить решение данной задачи с заданным шагом h на отрезке [A, B]
2) Использовать метод Эйлера
3) Использовать метод Рунге-Кута (4 порядка)

для достижения нужной точности e = 10^-3 необходимо по данным методам применять двойной расчет по принципу Рунге:
- получили решение
- делим шаг пополам
- делаем перерасчет
- сравниваем через y c начальными ответами (находим разность)
'''
import pprint

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

# исходная функция
FUN = lambda x, y: x * np.log(y) - y * np.log(x)

# исходные значения
A = 1
B = 2
X0 = 1
Y0 = 1
STEP = 0.05
EPS = 0.001
#для вывода на экран
X = np.arange(start=A, stop=B + STEP, step=STEP)

def diff(first_result : dict, second_result : dict) -> float:
    
    
    
    # нужно привести 2 словарь к первому, чтобы можно было сравнить значение функции в узлах
    pprint.pprint(second_result)
    tmp = {}
    for x, y in second_result.items():
        if x.round(3) in X.round(3):
            tmp[x] = y
    print()
    print()
    print()
    pprint.pprint(tmp)
    
    x_values = np.arange(start=A, stop=B + STEP, step=STEP)
    diff = []
    for x in x_values:
        diff.append(first_result[x.round(3)] - second_result[x.round(3)])
    print(f'Difference is : {max(diff)}')
    return max(diff)
    
def calculate_euler(A, B, STEP, Y0):
    x_values = np.arange(start=A, stop=B + STEP, step=STEP)
    y_values = [Y0]
    for i in range(1, len(x_values)):
        y_values.append(y_values[i - 1] + STEP * FUN(x_values[i - 1], y_values[i - 1]))
    return {x.round(3): y for (x, y) in zip(x_values, y_values)}

def print_euler(result: dict):
    x_values = result.keys()
    y_values = result.values()
    print("Euler Method: ")
    print(tabulate({"STEP": [i for i in range(1, len(X) + 1)],
                    "X": [x for x in X],
                    "Y": [y for x, y in result.items() if x.round(4) in X.round(4)]},
                    headers="keys", tablefmt="grid"))
    plt.plot(x_values, y_values, color='r', label='Euler Method')
    
#Euler Method
def euler(A, B, STEP, Y0, EPS):
    first_dict = calculate_euler(A, B, STEP, Y0)
    second_dict = calculate_euler(A, B, STEP/2, Y0)
    error = diff(first_dict, second_dict)
    if error < EPS:
        print(f'Error is {error}')
        print_euler(first_dict)
    else:
        euler(A, B, STEP/2, Y0, EPS)
    
def calculate_rk(A, B, STEP, Y0):
    x_values = np.arange(start=A, stop=B + STEP, step=STEP)
    y_values = [Y0]
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    k = []
    for x in X:
        k1.append(STEP * FUN(x, y_values[-1]))
        k2.append(STEP * FUN((x + STEP/2), (y_values[-1] + k1[-1]/2)))
        k3.append(STEP * FUN((x + STEP/2), (y_values[-1] + k2[-1]/2)))
        k4.append(STEP * FUN((x + STEP), (y_values[-1] + k3[-1])))
        k.append((k1[-1] + 2*k2[-1] + 2*k3[-1] + k4[-1]) / 6)
        y_values.append(y_values[-1] + k[-1])
    return {x.round(3): y for (x, y) in zip(x_values, y_values)}
    
    
    
# def print_rk(result: dict):
#     print("RK4 Method: ")
#     print(tabulate({"STEP": [i for i in range(1, len(X) + 1)],
#                     "X": x_values,
#                     "Y": y_values[:-1:],
#                     "k1": k1,
#                     "k2": k2,
#                     "k3": k3,
#                     "k4": k4,
#                     "k": k,
#                     "Y(i + 1)": [y_values[i] for i in range (1, len(y_values))]},
#                     headers="keys", tablefmt="grid"))
#     plt.plot(x_values, y_values[:-1:], color='g', label='RK4')
#     plt.title('Methods')
#     plt.show()
    
# (Runge Kutta) RK-4 method  
def rk4(A, B, STEP, Y0):
    first_dict = calculate_rk(A, B, STEP, Y0)
    second_dict = calculate_rk(A, B, STEP/2, Y0)
    error = diff(first_dict, second_dict)
    if error < EPS:
        print(f'Error is {error}')
        print_euler(first_dict)
    else:
        euler(A, B, STEP/2, Y0, EPS)
    
    
def main():
    # euler(A, B, STEP, Y0, EPS)  
    rk4(A, B, STEP, Y0)
    # euler(A, B, STEP/2, Y0)
    # euler(A, B, Y0, STEP/2)
    print()
    
if __name__ == "__main__":
    main()
