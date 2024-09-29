a = np.array((5,-2,1,3,-6,0,-7,2,9)).reshape((3,3))
print(a)
def checkCTH(b):
    flag_1 = True
    flag_2 = True
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[j][j] < np.sum(b[j]) - b[j][j]:
                print(np.sum(b[j]) - b[j][j])
                print(b[j][j])
                flag_1 = False
        if flag_1 == False:
            print("Không chéo trội hàng")
            return False
    return True
def checkCTC(b):
    flag_1 = True
    flag_2 = True
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[j][j] < np.sum(b[j]) - b[j][j]:
                print(np.sum(b[j]) - b[j][j])
                print(b[j][j])
                flag_1 = False
        if flag_1 == False:
            print("Không chéo trội cột")
            return False
    return True
if checkCTH(np.abs(a)):
    print("Chéo trội hàng")
if checkCTC(np.abs(np.transpose(a))):
    print("Chéo trội cột")
