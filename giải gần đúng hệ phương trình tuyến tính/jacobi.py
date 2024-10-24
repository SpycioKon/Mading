import numpy as np

def jacobi(A, b, x0, num_iterations):
  n = len(A)
  x = x0.copy()
  for _ in range(num_iterations):
    x_new = np.zeros(n)
    for i in range(n):
      s = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
      x_new[i] = (b[i] - s) / A[i, i]
    x = x_new.copy()
  return x

A = np.array([[5, -1, 2],
              [1, 4, -1],
              [1, 1, 4]])
b = np.array([8,-4, 4])
x0 = [0,0,0] #Vector nghiệm ban đầu
num_iterations = 3
x = jacobi(A, b, x0, num_iterations)
print(x)
