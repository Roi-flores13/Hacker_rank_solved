import numpy as np

number = input("")

array = np.array([int(i) for i in number.split(" ")]).reshape(3,3)
print(array)