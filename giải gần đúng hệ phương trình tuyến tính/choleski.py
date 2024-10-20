# Vũ Tiến Đạt
import numpy as np
import base64
import math
"""
giải phương trình bằng phân tích choleski
Phương pháp: Ly = B
L.T.x = y

"""
def tongDuongCheo(col,A,new_matrix):
    result = 0
    for i in range(col):
        result+=new_matrix[col][i]**2
    return result
def tongKhongCheo(row,col,A,new_matrix):
    result = 0
    for i in range(col):
        result+=new_matrix[row][i]*new_matrix[col][i]
    return result
if __name__ == "__main__":
    print(base64.b64decode(b"=QXYEBibllGVgUnV"[::-1]))
    A = np.array((4,-1,1,-1,4,-2,1,-2,4)).reshape((3,3))
    b = np.array((12,-1,5)).reshape(3,1)
    new_matrix = np.zeros((len(b),len(A)))
    for row in range(len(A)):
        for col in range(len(A[row])):
            if row<col:
                continue
            elif col == row:
                value =  math.sqrt(A[col][col] - tongDuongCheo(col,A,new_matrix)) 
                new_matrix[row][col] = value
            else:
                value = A[row][col] - tongKhongCheo(row,col,A,new_matrix)
                new_matrix[row][col] = value/(new_matrix[col][col])
        print("*"*8)
        print(new_matrix)

print(f"{'*'*8}\nL: \n{new_matrix}")
newMatrixT = new_matrix.T
y = np.linalg.solve(new_matrix,b)
x = np.linalg.solve(newMatrixT,y)
print(x)
