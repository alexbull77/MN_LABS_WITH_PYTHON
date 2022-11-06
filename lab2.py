import numpy as np
import sys
import math
import pprint
import scipy
import scipy.linalg

f1 = lambda x1,x2,x3, x4: (7.2 + 0.9*x2 - 0.6*x3 - 0.8*x4) / 8.1
f2 = lambda x1,x2,x3, x4: (10.3 + 0.9*x1 - 0.3*x3 - 0.7*x4) / 14.3 
f3 = lambda x1,x2,x3, x4: (-11.9 - 0.6*x1 - 0.3*x2 + 0.4*x4) / 7.9
f4 = lambda x1,x2,x3, x4: (9.2 - 0.8*x1 - 0.7*x2 + 0.4*x3) / 10.6

# number of unknowns
n = 4
# tolerable error
eps = 0.00001
# max number of iterations
m = 100

a = np.zeros((n,n+1))
a = [
    [8.1, -0.9, 0.6, 0.8, 7.2],
    [-0.9, 14.3, 0.3, 0.7, 10.3],
    [0.6, 0.3, 7.9, -0.4, -11.9],
    [0.8, 0.7, -0.4, 10.6, 9.2]
]
a_mod = [
    [8.1, -0.9, 0.6, 0.8],
    [-0.9, 14.3, 0.3, 0.7],
    [0.6, 0.3, 7.9, -0.4],
    [0.8, 0.7, -0.4, 10.6]
]
v_res = [7.2, 10.3, -11.9, 9.2]

def Gauss():
    x = np.zeros(n)

    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    # Displaying solution
    print('\nGauss Method: ')
    for i in range(n):
        print (f'x{i + 1} = {x[i]}')

def GaussJordan():
    x = np.zeros(n)

    # Applying Gauss Jordan Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    # Obtaining Solution

    for i in range(n):
        x[i] = a[i][n]/a[i][i]

    print('\nGauss Jordan Method: ')
    for i in range(n):
        print (f'x{i + 1} = {x[i]}')
    print ('\n\n')

def cholesky():
    L = scipy.linalg.cholesky(a_mod, lower=True)
    pprint.pprint (L)
        
            
def JacobiMethod():
        # Initial setup
    x1_0 = 0
    x2_0 = 0
    x3_0 = 0
    x4_0 = 0
    count = 1

    # Reading tolerable error
    e = eps

    # Implementation of Jacobi Iteration
    print("Jacobi Method:")
    print('\nCount\tx1 \t x2 \t x3 \t x4\n')

    condition = True
    while condition:
        x1_1 = f1(x1_0, x2_0, x3_0, x4_0)
        x2_1 = f2(x1_0, x2_0, x3_0, x4_0)
        x3_1 = f3(x1_0, x2_0, x3_0, x4_0)
        x4_1 = f4(x1_0, x2_0, x3_0, x4_0)

        print('%d\t%0.3f\t%0.3f\t%0.3f\t%0.3f\n' %(count, x1_1, x2_1, x3_1, x4_1))
        e1 = abs(x1_0-x1_1)
        e2 = abs(x2_0-x2_1)
        e3 = abs(x3_0-x3_1)
        e4 = abs(x4_0-x4_1)
        
        count += 1
        x1_0 = x1_1
        x2_0 = x2_1
        x3_0 = x3_1
        x4_0 = x4_1
        
        condition = e1>e and e2>e and e3>e and e4>e

    print('\nSolution is:\n\nx1=%0.3f\nx2=%0.3f\nx3 = %0.3f\nx4 = %0.3f\n'% (x1_1, x2_1, x3_1, x4_1))
    
def Gauss_Seidel_Method():
    # Initial setup
    x1_0 = 0
    x2_0 = 0
    x3_0 = 0
    x4_0 = 0
    count = 1

    # Reading tolerable error
    e = eps

    # Implementation of Jacobi Iteration
    print("Gauss-Zeidel Method:")
    print('\nCount\tx1 \t x2 \t x3 \t x4\n')

    condition = True
    while condition:
        x1_1 = f1(x1_0, x2_0, x3_0, x4_0)
        x2_1 = f2(x1_1, x2_0, x3_0, x4_0)
        x3_1 = f3(x1_1, x2_1, x3_0, x4_0)
        x4_1 = f4(x1_1, x2_1, x3_1, x4_0)

        print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1_1, x2_1, x3_1, x4_1))
        e1 = abs(x1_0-x1_1)
        e2 = abs(x2_0-x2_1)
        e3 = abs(x3_0-x3_1)
        e4 = abs(x4_0-x4_1)
        
        count += 1
        x1_0 = x1_1
        x2_0 = x2_1
        x3_0 = x3_1
        x4_0 = x4_1
        
        condition = e1>e and e2>e and e3>e and e4>e

    print('\nSolution is:\n\nx1=%0.4f\nx2=%0.4f\nx3 = %0.4f\nx4 = %0.4f\n'% (x1_1, x2_1, x3_1, x4_1))

def main():
    Gauss()
    GaussJordan()
    JacobiMethod()
    Gauss_Seidel_Method()
    cholesky()

if __name__ == "__main__":
    main()
