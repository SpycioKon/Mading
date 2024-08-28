import math
"""
Nội suy Lagrange dùng để làm gì: Nội suy Lagrange dùng để tính số gần đúng'
Công thức
P = sum 0->n (y_i*l_i(x))
với l_i = (x-x0)(x-x1)...(x-x[n-1])/(xi-x0)(xi-x1)..(xi-x[n-1]) trong đó không có x-xi trên tử và xi-xi dưới mẫu
"""

"""
sample lấy các tọa độ x,y
x   0   2    3
y   7   11   28
"""
def l_cap(index,x):
    sum1 = 1
    sum2 = 1
    for i in range(len(X)):
        if i == index:
            continue
        else:
            sum1 *= (x-X[i])
            sum2 *= (X[index] - X[i])
    return sum1/sum2

X = [15,17,31,35]
Y = [65.4,62.5,47.8,39]
x = 16
Pn = 0
for i in range(len(X)):
    print(f"Tính l_cap{i}")
    Pn += Y[i]*l_cap(i,x)
    print(Pn)
