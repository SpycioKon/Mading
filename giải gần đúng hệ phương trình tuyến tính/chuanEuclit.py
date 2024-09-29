"""
|| A ||_2 hoặc ||.||

"""
import numpy as np
import math
sum_ = 0
a = np.array((1,-2,3,4,5,-7,8,6,-2)).reshape((3,3))
for row in a:
    for i in row:
        sum_ += i**2
sum = math.sqrt(sum_)
print(sum)
