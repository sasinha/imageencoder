import numpy as np


#  copy-pasted from old cipher and needs cleanup
def inverse_matrix(inputMatrix, modulo):
    a = inputMatrix
    m = modulo
    p = np.round(np.linalg.det(a) * np.linalg.inv(a))
    a = np.round(np.linalg.det(a))
    num = np.arange(1, m + 1)  # creates a modulo dictionary
    res = np.mod(a * num, m)
    b = np.where(res == 1)
    err = np.size(b)
    if err == 0:
        print("The matrix has no modular inverse")
        return 0
    b = b[0].item(0) + 1
    return np.mod(b * p, m).astype(int)


def random_mod_matrix(min, max, dimension):
    random_matrix = np.random.randint(min, max, dimension)
    if random_matrix.all == 0:
        random_matrix = random_mod_matrix(min,max,dimension)
    else:
        inverse_mod = inverse_matrix(random_matrix, max)
        if np.size(inverse_mod) == 1:
            return random_mod_matrix(min,max,dimension)
    return random_matrix






if __name__ == "__main__":
    mTest=np.array(([6,24,1],[13,16,10],[20,17,15]))
    mResult = np.array(([8,5,10],[21,8,21],[21,12,8]))
    mInverse=inverse_matrix(mTest,26)
    print("Inverse: \n", mInverse)
    print("check: \n", mResult)


    test = random_mod_matrix(0,28,(3,3))
    testb = inverse_matrix(test, 28)
    testCheck = inverse_matrix(testb, 28)

    print(test)
    print(testb)
    print(testCheck)
