a = 1
b = 2
n = 2
# (a,b) là khoảng phân ly
x = Symbol('x')
f_x = x**2-2
save_point = 0

while n!=0:
    if f_x.subs(x,a) > 0:
        x_0 = b # điểm fourier là a
        save_point = x_0 - (f_x.subs(x,x_0) / (f_x.subs(x,x_0) - f_x.subs(x,a)) * (x_0 - a))
        b = save_point
    else:
        x_0 = a # điểm fourier là b
        save_point = x_0 - ((f_x.subs(x,x_0)) / (f_x.subs(x,x_0) - f_x.subs(x,b))) * (x_0 - b)
        a = save_point
    n-=1
print(save_point)
