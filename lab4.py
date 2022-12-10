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

# зададим нужный отрезок
X = np.arange(start=A, stop=B + STEP, step=STEP)
N = len(X)

#Euler Method
def euler(X0, Y0, STEP):
    N = len(X)
    Y = [Y0]
    
    for i in range(1, N):
        Y.append(Y[i - 1] + STEP * FUN(X[i - 1], Y[i - 1]))

    print("Euler Method: ")
    print(tabulate({"STEP": [i for i in range(1, N + 1)],
                    "X": [x for x in X],
                    "Y": [y for y in Y]},
                    headers="keys", tablefmt="grid"))
    
# (Runge Kutta) RK-4 method  
def rk4(X0, Y0, STEP):
    N = len(X)
    Y = [Y0]
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    k = []
    for i in range(N):
        k1.append(STEP * FUN(X[i - 1], Y[i - 1]))
        k2.append(STEP * FUN((X[i - 1] + STEP/2), (Y[i - 1] + k1[-1]/2)))
        k3.append(STEP * FUN((X[i - 1] + STEP/2), (Y[i - 1] + k2[-1]/2)))
        k4.append(STEP * FUN((X[i - 1] + STEP), (Y[i - 1] + k3[-1])))
        k.append((k1[-1] + 2*k2[-1] + 2*k3[-1] + k4[-1])/6)
        Y.append(Y[i - 1] + k[-1])

    print("RK4 Method: ")
    print(tabulate({"STEP": [i for i in range(1, N + 1)],
                    "X": X,
                    "Y": Y[:-1:],
                    "k1": k1,
                    "k2": k2,
                    "k3": k3,
                    "k4": k4,
                    "k": k,
                    "Y(i + 1)": [Y[i] for i in range (1, len(Y))]},
                    headers="keys", tablefmt="grid"))
    
def main():
    euler(X0, Y0, STEP)
    rk4(X0, Y0, STEP)
    
if __name__ == "__main__":
    main()