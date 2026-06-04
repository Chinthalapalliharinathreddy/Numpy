"""
NumPy fromiter()
fromiter() creates an array from an iterable (generator, range, list comprehension)
Memory efficient for creating arrays from iterables
"""

import numpy as np

# Example 1: Create array from range
arr1 = np.fromiter(range(5), dtype=int)
print("Array from range(5):")
print(arr1)

# Example 2: Create array from generator
def gen_squares(n):
    for i in range(n):
        yield i ** 2

arr2 = np.fromiter(gen_squares(5), dtype=int)
print("\nArray from generator (squares):")
print(arr2)

# Example 3: Create array from list comprehension
arr3 = np.fromiter([x * 2 for x in range(6)], dtype=int)
print("\nArray from list comprehension (doubles):")
print(arr3)

# Example 4: Use count parameter to limit elements
iterator = iter(range(100))
arr4 = np.fromiter(iterator, dtype=int, count=5)
print("\nArray from iterator with count=5:")
print(arr4)

# Example 5: Create float array from iterable
arr5 = np.fromiter((float(x) for x in range(4)), dtype=float)
print("\nFloat array from generator:")
print(arr5, arr5.dtype)

# Example 6: Custom generator with calculations
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

arr6 = np.fromiter(fib_gen(8), dtype=int)
print("\nFibonacci sequence:")
print(arr6)

# Example 7: Using filter with fromiter
arr7 = np.fromiter(filter(lambda x: x % 2 == 0, range(10)), dtype=int)
print("\nEven numbers from 0 to 9:")
print(arr7)

# Example 8: Complex numbers from iterable
arr8 = np.fromiter((complex(x, x+1) for x in range(4)), dtype=complex)
print("\nComplex array from generator:")
print(arr8)

# Example 9: fromiter() with callable
def counter_gen():
    count = 0
    while count < 5:
        yield count
        count += 1

arr9 = np.fromiter(counter_gen(), dtype=int)
print("\nArray from callable generator:")
print(arr9)
