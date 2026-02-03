import numpy as np

A = np.array([1, 2, 3, 4])

str = "A={}"
print(str.format(A))
str = "A.ndim={}"
print(str.format(A.ndim))
str = "A.shape={}"
print(str.format(A.shape))
str = "A.shape[0]={}"
print(str.format(A.shape[0]))

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

str = "AB = {}"
print(str.format(np.dot(A, B)))