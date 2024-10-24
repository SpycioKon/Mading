import numpy as np

# Ma trận hệ số A và vector hằng số b
A = np.array([[2, 5, 6.5, 4],
              [4, 10, 5, 4],
              [8, 4, 2, 0],
              [0, 4, 4, 9]], dtype=float)

b = np.array([26, 32, 24, 21], dtype=float)

n = len(b) 

# Quá trình khử Gauss
for k in range(n):
    
    max_row = np.argmax(np.abs(A[k:, k])) + k  
    if A[max_row, k] == 0:
        raise ValueError("Ma trận không khả nghịch, phần tử trụ bằng 0.")
    
    if max_row != k:
        A[[k, max_row]] = A[[max_row, k]]
        b[k], b[max_row] = b[max_row], b[k]
    
    # Khử các phần tử bên dưới hàng trục
    for i in range(k+1, n):
        if A[i, k] == 0:
            continue  
        lambda_factor = A[i, k] / A[k, k]  
        A[i, k:] -= lambda_factor * A[k, k:] 
        b[i] -= lambda_factor * b[k]  

# Quá trình thế ngược để tìm nghiệm
x = np.zeros(n)  
for i in range(n-1, -1, -1): 
    sum_ax = np.dot(A[i, i+1:], x[i+1:])  
    x[i] = (b[i] - sum_ax) / A[i, i]  

# In kết quả
print("Nghiệm đúng của hệ là:")
for i in range(n):
    print(f"x_{i+1} = {x[i]:.2f}")
