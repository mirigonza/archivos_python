import numpy as np

v1 = np.array([1, 2])
v2 = np.array([2,2])

suma = v1 + v2
print(suma)

where_v1 = np.where((v1 % 2) == 0, v1, 0)
print(where_v1)

def sumando():
    v1 = np.array([-9, 5, 8, 3])
    total = np.sum(v1)
    print(total)



if __name__ == '__main__':
    sumando()
    #numpy_where_diff()
    #numpy_mask()