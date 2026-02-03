import numpy as np

x = np.array([1,2,4])
y = np.array([2,4,1.5])

str = "x is {}"
print(str.format(x))
print(str.format(type(x)))

str = "x+y is {}"
print(str.format(x+y))

str = "x*y is {}"
print(str.format(x*y))

str = "x*2 is {}"
print(str.format(x*2))

A = np.array([[1,2], [3,4]])
B = np.array([10,20])

str = "A*B is {}" #广播
print(str.format(A*B))

for row in A:
    print(row)

print(A>2)

A = A.flatten() #转化为一维数组

str = "flatten A is {}"
print(str.format(A))

str = "A[1] is {}"
print(str.format(A[np.array([1])]))