import math

f1_half_div_method = lambda x: math.exp(x) + 3 * x
f2_half_div_method = lambda x: x**3 - 23 * x - 42
f1_sim_iter_method = lambda x: x - ((math.exp(x) + 3 * x) / 3.3690)
f2_sim_iter_method = lambda x: x - ((x**3 - 23 * x - 42) / 85)
f1_first_deriv_newton_method = lambda x: math.exp(x) + 3
f1_second_deriv_newton_method = lambda x: math.exp(x)
f2_first_deriv_newton_method = lambda x: 3 * x ** 2 - 23
f2_second_deriv_newton_method = lambda x: 6 * x

def pr_6int(num : float): 
    formatted_string = "{:.6f}". format(num)
    float_value = float(formatted_string)
    return float_value

def half_division_method(a, b, eps, func, count = 1):
    
    fa = func(a)
    fb = func(b)
    
    if (fa * fb > 0):
        print(f"Incorect interval! [{a}, {b}]")
    else:
        c = a + ((b - a) / 2)
        print (f"{count}: {c}")
        fc = func(c)
        
        if ((fc == 0) or ((b - a) < eps)):
            print (f'Result is {pr_6int(c)}')
            print(f'Number of Iterations is {count}')
            return c
        
        if (fa * fc < 0):
            half_division_method(a, c, eps, func, count + 1) 
        else:
            half_division_method(c, b, eps, func, count + 1)
        
def simple_iterations_method(x1, x0, eps, func, q, count = 1, tmp = []) :
    
    x0 = func(x0)
    tmp.append(x0)
    print (f"{count}: {x0}")
    
    if (len(tmp) >= 2) and ((q/(1 - q) * abs(tmp[len(tmp) - 1] - tmp[len(tmp) - 2])) <= eps):
        print(f'Result is {pr_6int(x0)}')
        print(f'Number of Iterations is {count}')
    else: 
        simple_iterations_method(x1, x0, eps, func, q, count + 1, tmp)
        
def newton_method(x, a, b, eps, func, func1, c, count = 1, tmp = []):
        
    x = x - func(x) / func1(x)
    tmp.append(x)
    print (f"{count}: {x}")

    
    if ((len(tmp) >= 2) and eps >= c * ((abs(tmp[len(tmp) - 1] - tmp[len(tmp) - 2]))**2)):
        print (f'Result is {pr_6int(x)}')
        print (f'Number of Iterations is {count}')
        return
    
    newton_method(x, a, b, eps, func, func1, c, count + 1, tmp)

def chord_method(a, b, eps, func, c, count = 1, tmp =[]):
    
    x = a - (func(a) / (func(b) - func(a)) * (b - a))
    print (f"{count}: {c}")
    tmp.append(x)
    
    if (len(tmp) >= 2 and (c * (abs(tmp[len(tmp) - 1] - tmp[len(tmp) - 2]) <= eps))):
            print (f'Result is {pr_6int(x)}')
            print (f'Number of Iterations is {count}')
            return
    
    if (func(a) > 0 and func(b) < 0):
        chord_method(a, x, eps, func, c, count + 1, tmp)
    else:
        chord_method(x, b, eps, func, c, count + 1, tmp)

def main():
    print("First function:")
    
    print("")
    print("")
    print("Half Division Method: ")
    half_division_method(-1, 0, 0.000001, f1_half_div_method)
    
    print("")
    print('Simple Iterations Method:')
    simple_iterations_method(0, -1, 0.000001, f1_sim_iter_method, 0.15775)

    print("")
    print('Newton Method:')
    newton_method(0, -1, 0, 0.000001, f1_half_div_method, f1_first_deriv_newton_method, 0.125)

    print("")
    print('Chord Method:')
    chord_method(-1, 0, 0.000001, f1_half_div_method, 0.1778563)
    print("")

    print("")
    print("Second function:")
    print("")

    
    print("")
    print("Half Division Method: ")
    half_division_method(5, 6, 0.000001, f2_half_div_method)        

    print("")
    print('Simple Iterations Method:')
    simple_iterations_method(5, 5.5, 0.000001, f2_sim_iter_method, 0.3882)

    print("")
    print('Newton Method:')
    newton_method(6, 5, 6, 0.000001, f2_half_div_method, f2_first_deriv_newton_method, 0.34615385)
    
    print("")
    print('Chord Method:')
    chord_method(5, 6, 0.000001, f2_half_div_method, 0.63461)
            
if __name__ == '__main__':
    main()