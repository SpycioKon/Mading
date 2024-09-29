a = np.array((1,-2,3,4,5,-7,8,6,-2)).reshape((3,3))
b = np.transpose(a)
print(b)
np.max(np.sum(b,axis=1))
