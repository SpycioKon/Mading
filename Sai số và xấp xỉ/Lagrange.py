
import numpy as np
import math

x = np.array([-1, 0, 1])
y = np.array([1/3, 1, 3])

x_sel = math.sqrt(3)

Pn = 0

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
