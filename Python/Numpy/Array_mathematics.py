import numpy as np

two_numb = input("")
array_one = input("")
array_two = input("")

final_array_one = np.array([int(i) for i in array_one.split(" ")])
final_array_two = np.array([int(i) for i in array_two.split(" ")])

print(f"[{np.add(final_array_one, final_array_two)}]")
print(f"[{np.subtract(final_array_one, final_array_two)}]")
print(f"[{np.multiply(final_array_one, final_array_two)}]")
print(f"[{np.floor_divide(final_array_one, final_array_two)}]")
print(f"[{np.mod(final_array_one, final_array_two)}]")
print(f"[{np.power(final_array_one, final_array_two)}]")