import numpy as np
import math

# Các điểm x và y
x = np.array([-1, 0, 1])
y = np.array([1/3, 1, 3])

# Điểm cần tính giá trị của đa thức nội suy
x_sel = math.sqrt(3)

# Khởi tạo giá trị của Pn
Pn = 0

# Hàm tính đa thức cơ sở Lagrange L_i(x)
def l(x_sel, cap):
    multi = 1
    for i in range(len(x)):
        if i == cap:
            continue
        multi *= (x_sel - x[i]) / (x[cap] - x[i])
    return multi

# Tính giá trị của Pn tại x_sel
for cap, j in enumerate(y):
    print(f"cap {cap}:")
    Pn += j * l(x_sel, cap)
    print(f"{Pn}")

print(f"Giá trị của Pn tại x_sel = {x_sel} là: {Pn}")
