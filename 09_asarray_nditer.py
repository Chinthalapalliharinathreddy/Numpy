"""
NumPy asarray() with nditer()
asarray() converts lists, tuples, and other iterables into NumPy arrays
nditer() iterates over array elements efficiently
"""

import numpy as np

# Example 1: Convert a list to array
list_data = [1, 2, 3, 4, 5]
arr1 = np.asarray(list_data)
print("List to array:")
print(arr1)

# Example 2: Convert nested list (2D) to array
nested_list = [[1, 2, 3], [4, 5, 6]]
arr2 = np.asarray(nested_list)
print("\nNested list to 2D array:")
print(arr2)

# Example 3: Convert tuple to array
tuple_data = (10, 20, 30, 40)
arr3 = np.asarray(tuple_data)
print("\nTuple to array:")
print(arr3)

# Example 4: Using nditer() to iterate over array
print("\nIterating with nditer():")
for value in np.nditer(arr1):
    print(value, end=" ")
print()

# Example 5: nditer() with multiple arrays (broadcasting)
arr_x = np.asarray([1, 2, 3])
arr_y = np.asarray([10, 20, 30])
print("\nIterating two arrays simultaneously:")
for x, y in np.nditer([arr_x, arr_y]):
    print(f"({x}, {y})", end=" ")
print()

# Example 6: asarray() with dtype specification
arr4 = np.asarray([1, 2, 3], dtype=float)
print("\nArray with float dtype:")
print(arr4, arr4.dtype)

# Example 7: nditer() with flags
arr_2d = np.asarray([[1, 2], [3, 4]])
print("\nForward iteration (C-order):")
for val in np.nditer(arr_2d, flags=['refs_ok'], op_flags=['readwrite']):
    print(val, end=" ")
print()

# Example 8: Generator to array using asarray
def gen_data():
    for i in range(5):
        yield i * 2

arr5 = np.asarray(list(gen_data()))
print("\nGenerator converted to array:")
print(arr5)
