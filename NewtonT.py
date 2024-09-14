import numpy as np

x = np.array([0, 2, 3, 5, 6])
y = np.array([1, 3, 2, 5, 6])

diff_table = np.zeros((len(y), len(y)))

diff_table[:, 0] = y

def TSP():
    n = len(y)
    for cap in range(1, n):  
        for i in range(n - cap):  
            diff_table[i, cap] = (diff_table[i+1, cap-1] - diff_table[i, cap-1]) / (x[i+cap] - x[i])
TSP()
## lập bảng tỉ sai phân, công thức tự viết
