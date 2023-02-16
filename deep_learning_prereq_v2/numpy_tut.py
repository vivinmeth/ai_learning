import numpy as np

# Array creation
A = np.array([1,2,3])


# Append will not work
try:
    A.append(5)

except Exception as ex:
    print("cannot append to numpy arrayss, ex:", ex)


# Loop through array
for elem in A:
    print(elem)

# broadcasting
print(A + np.array([4]))

# vector addition
print(A + np.array([4, 5, 6]))

# cannot add vectors of different sizes
try:
    print(A + np.array([4, 5]))
except Exception as ex:
    print(ex)

# multiply on Array
print(2 * A)

# sqaure in array
print(A**2)

# sqrt in array
print(np.sqrt(A))

# log in array
print(np.log(A))

# exp in array
print(np.exp(A))

# tanh in array
print(np.tanh(A))

''' 
  Dot Product
'''
a = np.array([1, 2])
b = np.array([3, 4])
print(np.sum(a * b))  # method 1
print(np.dot(a, b))  # method 2
print(a @ b)  # method 3


# magnitude of a vector
amag = np.sqrt((a * a).sum())
print(amag)

# normalize a vector
norma = np.linalg.norm(a)
normb = np.linalg.norm(b)
print(norma, normb)

# cosangle
cosangle = a.dot(b) / (norma * normb)
print(cosangle)

# angle
angle = np.arccos(cosangle)
print(angle)

