"""
### Vũ Tiến Đạt

import numpy as np

x = np.array([-2, 1, 4, -1, 3, -4])
y = np.array([-1, 2, 59, 4, 24, -53])

diff_table = np.zeros((len(y), len(y)))

diff_table[:, 0] = y

Pn = 0

def TSP():
    n = len(y)
    for cap in range(1, n):  
        for i in range(n - cap):  
            diff_table[i, cap] = (diff_table[i+1, cap-1] - diff_table[i, cap-1]) / (x[i+cap] - x[i])
        print(f"Bảng {cap}:\n {diff_table}")
TSP()
## lập bảng tỉ sai phân, công thức tự viết
## sau khi có bảng sai phân thì h lấy ra nhân thôi @@
new_diff_table = diff_table[0,1:]
print(new_diff_table) -> lười quá ae tự code Pn nhé,

"""

### Nguyễn Hà Anh Đức
import numpy as np
def TSP(x, y):
    n = len(x)
    table = np.zeros([n, n])  
    table[:, 0] = y  

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])

    return table[0] 

def newton_tien(x, y, x_value):
    table = TSP(x, y) 
    n = len(x)
    approx_value = table[0]  
    bieu_thuc = 1 

    for i in range(1, n):
        bieu_thuc *= (x_value - x[i - 1])
        approx_value += table[i] * bieu_thuc

    print("Các hệ số của đa thức nội suy Newton (tỉ sai phân chia):")
    for i, c in enumerate(table):
        print(f"Hệ số bậc {i}: {c}")

    return approx_value


x = np.array([-2,1,4,-1,3,-4])
y = np.array([-1,2,59,4,24,-53])

x_value = 2
kq = newton_tien(x, y, x_value)

print(f"Giá trị gần đúng của f(1.25) là: {kq}")
