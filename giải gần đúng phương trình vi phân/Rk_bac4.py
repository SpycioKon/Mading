from sympy import symbols
import numpy as np

"""
Giải phương trình vi phân bằng Runge-Kutta bậc 4
"""
x, y = symbols('x y')
a = int(input("Nhập khoảng trái a: "))
b = int(input("Nhập khoảng phải b: "))
n = int(input("Nhập số khoảng chia n: "))
h = (b - a) / n
print(f"h: {h}")

f_x = 3 * (x**2) * y
y_current = 1 

def k1(x_value, y_value):
    return h * f_x.subs({x: x_value, y: y_value})

def k2(x_value, y_value):
    return h * f_x.subs({x: x_value + (h / 2), y: y_value + k1(x_value, y_value) / 2})

def k3(x_value, y_value):
    return h * f_x.subs({x: x_value + (h / 2), y: y_value + k2(x_value, y_value) / 2})

def k4(x_value, y_value):
    return h * f_x.subs({x: x_value + h, y: y_value + k3(x_value, y_value)})
table = np.zeros((5,7))
print(table)
for i in range(n + 1):
    x_current = a + i * h
    k_1 = k1(x_current, y_current)
    k_2 = k2(x_current, y_current)
    k_3 = k3(x_current, y_current)
    k_4 = k4(x_current, y_current)

    print(f"x: {x_current:.1f} | y: {y_current:.6f} | f_(x,y): {(f_x.subs({x:x_current,y:y_current})).evalf(4)}|k1: {k_1:.6f} | k2: {k_2:.6f} | k3: {k_3:.6f} | k4: {k_4:.6f}")
    table[i] = [x_current,y_current,(f_x.subs({x:x_current,y:y_current})).evalf(4), k_1,k_2,k_3,k_4]
    y_current = y_current + (1 / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
