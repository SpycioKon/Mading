# cho khoảng (a,b) = (-1,2)
"""
Điều kiện dừng, lặp với số lần tối đa, hoặc |x-x*|< Epsilon cho trước
"""
from sympy import Symbol, diff

a = 1 # khoảng trái
b = 2 # khoảng phải
n = 6 # số lần lặp

x = Symbol('x')
f_x = x**2-2 
count = 0
x_0 = (a+b)/2

while n!=0:
    if f_x.subs(x,x_0) == 0:
        print(x_0)
        break
    else:
        if f_x.subs(x,a) * f_x.subs(x,x_0) > 0:
            a = x_0
        else:
            b = x_0
        print(f"{a} :{b}: {f_x.subs(x,x_0)}")
    x_0 = (a+b)/2
    n-=1
print(x_0)
