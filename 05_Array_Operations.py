"""
NumPy Array Operations - Element-wise operations, arithmetic, and more
"""

import numpy as np

# ============================================================================
# 1. Basic Arithmetic Operations
# ============================================================================
print("=" * 70)
print("1. Basic Arithmetic Operations")
print("=" * 70)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}\n")

print(f"Addition (arr1 + arr2): {arr1 + arr2}")
print(f"Subtraction (arr1 - arr2): {arr1 - arr2}")
print(f"Multiplication (arr1 * arr2): {arr1 * arr2}")
print(f"Division (arr2 / arr1): {arr2 / arr1}")
print(f"Floor division (arr2 // arr1): {arr2 // arr1}")
print(f"Modulo (arr2 % arr1): {arr2 % arr1}")
print(f"Power (arr1 ** 2): {arr1 ** 2}")

# ============================================================================
# 2. Arithmetic with Scalars
# ============================================================================
print("\n" + "=" * 70)
print("2. Arithmetic with Scalars")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}\n")

print(f"arr + 5: {arr + 5}")
print(f"arr - 2: {arr - 2}")
print(f"arr * 3: {arr * 3}")
print(f"arr / 2: {arr / 2}")
print(f"arr ** 2: {arr ** 2}")

# ============================================================================
# 3. Unary Operations
# ============================================================================
print("\n" + "=" * 70)
print("3. Unary Operations")
print("=" * 70)

arr = np.array([1, -2, 3, -4, 5])
print(f"Array: {arr}\n")

print(f"Negative (-arr): {-arr}")
print(f"Absolute (np.abs(arr)): {np.abs(arr)}")
print(f"Square root (np.sqrt([1, 4, 9, 16])): {np.sqrt(np.array([1, 4, 9, 16]))}")

# ============================================================================
# 4. Comparison Operations
# ============================================================================
print("\n" + "=" * 70)
print("4. Comparison Operations")
print("=" * 70)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}\n")

print(f"arr1 == arr2: {arr1 == arr2}")
print(f"arr1 != arr2: {arr1 != arr2}")
print(f"arr1 < arr2: {arr1 < arr2}")
print(f"arr1 > arr2: {arr1 > arr2}")
print(f"arr1 <= arr2: {arr1 <= arr2}")
print(f"arr1 >= arr2: {arr1 >= arr2}")

# ============================================================================
# 5. Logical Operations
# ============================================================================
print("\n" + "=" * 70)
print("5. Logical Operations")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {arr}\n")

mask1 = arr > 5
mask2 = arr < 8

print(f"arr > 5: {mask1}")
print(f"arr < 8: {mask2}")
print(f"AND (arr > 5) & (arr < 8): {mask1 & mask2}")
print(f"OR (arr > 5) | (arr < 8): {mask1 | mask2}")
print(f"NOT not(arr > 5): {~mask1}")

# ============================================================================
# 6. Sum, Mean, Median, Std
# ============================================================================
print("\n" + "=" * 70)
print("6. Statistical Functions")
print("=" * 70)

arr = np.array([10, 20, 30, 40, 50])
print(f"Array: {arr}\n")

print(f"Sum (np.sum): {np.sum(arr)}")
print(f"Mean (np.mean): {np.mean(arr)}")
print(f"Median (np.median): {np.median(arr)}")
print(f"Std Dev (np.std): {np.std(arr)}")
print(f"Variance (np.var): {np.var(arr)}")
print(f"Min (np.min): {np.min(arr)}")
print(f"Max (np.max): {np.max(arr)}")

# ============================================================================
# 7. Operations along axes (2D)
# ============================================================================
print("\n" + "=" * 70)
print("7. Operations Along Axes (2D)")
print("=" * 70)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n{arr2d}\n")

print(f"Sum all: {np.sum(arr2d)}")
print(f"Sum along axis 0 (columns): {np.sum(arr2d, axis=0)}")
print(f"Sum along axis 1 (rows): {np.sum(arr2d, axis=1)}")

print(f"\nMean along axis 0: {np.mean(arr2d, axis=0)}")
print(f"Mean along axis 1: {np.mean(arr2d, axis=1)}")

print(f"\nMax along axis 0: {np.max(arr2d, axis=0)}")
print(f"Max along axis 1: {np.max(arr2d, axis=1)}")

# ============================================================================
# 8. Cumulative Operations
# ============================================================================
print("\n" + "=" * 70)
print("8. Cumulative Operations")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}\n")

print(f"Cumulative sum (np.cumsum): {np.cumsum(arr)}")
print(f"Cumulative product (np.cumprod): {np.cumprod(arr)}")

# ============================================================================
# 9. Sorting
# ============================================================================
print("\n" + "=" * 70)
print("9. Sorting")
print("=" * 70)

arr = np.array([5, 2, 8, 1, 9, 3])
print(f"Original array: {arr}\n")

print(f"Sorted (np.sort): {np.sort(arr)}")
print(f"Reverse sorted (np.sort with [::-1]): {np.sort(arr)[::-1]}")

# Get indices that would sort array
indices = np.argsort(arr)
print(f"Indices that sort array: {indices}")

# Sort along axis
arr2d = np.array([[3, 1, 2], [6, 4, 5]])
print(f"\n2D Array:\n{arr2d}")
print(f"Sorted along axis 0:\n{np.sort(arr2d, axis=0)}")
print(f"Sorted along axis 1:\n{np.sort(arr2d, axis=1)}")

# ============================================================================
# 10. Unique elements
# ============================================================================
print("\n" + "=" * 70)
print("10. Unique Elements")
print("=" * 70)

arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(f"Array with duplicates: {arr}\n")

unique = np.unique(arr)
print(f"Unique elements: {unique}")
print(f"Number of unique elements: {len(unique)}")

# Get counts of each unique element
unique, counts = np.unique(arr, return_counts=True)
print(f"\nUnique elements: {unique}")
print(f"Counts: {counts}")

# ============================================================================
# 11. Clip - Limit values
# ============================================================================
print("\n" + "=" * 70)
print("11. Clip - Limit Values")
print("=" * 70)

arr = np.array([1, 5, 3, 8, 2, 9, 4])
print(f"Original array: {arr}")
print(f"Clip between 3 and 7: {np.clip(arr, 3, 7)}")

# ============================================================================
# 12. Round, Floor, Ceil
# ============================================================================
print("\n" + "=" * 70)
print("12. Rounding Operations")
print("=" * 70)

arr = np.array([1.23, 2.56, 3.89, 4.12, 5.67])
print(f"Array: {arr}\n")

print(f"Round (np.round): {np.round(arr)}")
print(f"Floor (np.floor): {np.floor(arr)}")
print(f"Ceil (np.ceil): {np.ceil(arr)}")
print(f"Truncate (np.trunc): {np.trunc(arr)}")

# ============================================================================
# 13. Trigonometric functions
# ============================================================================
print("\n" + "=" * 70)
print("13. Trigonometric Functions")
print("=" * 70)

arr = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(f"Array (in radians): {arr}\n")

print(f"sin: {np.sin(arr)}")
print(f"cos: {np.cos(arr)}")
print(f"tan: {np.tan(arr)}")
print(f"arcsin([0, 0.5, 1]): {np.arcsin(np.array([0, 0.5, 1]))}")

# ============================================================================
# 14. Exponential and Logarithm
# ============================================================================
print("\n" + "=" * 70)
print("14. Exponential and Logarithm")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}\n")

print(f"exp (e^x): {np.exp(arr)}")
print(f"log (natural log): {np.log(arr)}")
print(f"log10: {np.log10(arr)}")
print(f"log2: {np.log2(arr)}")

# ============================================================================
# 15. Sign function
# ============================================================================
print("\n" + "=" * 70)
print("15. Sign Function")
print("=" * 70)

arr = np.array([-5, -2, 0, 3, 7])
print(f"Array: {arr}")
print(f"Sign (np.sign): {np.sign(arr)}")

# ============================================================================
# 16. Dot product
# ============================================================================
print("\n" + "=" * 70)
print("16. Dot Product")
print("=" * 70)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Dot product (1*4 + 2*5 + 3*6): {np.dot(arr1, arr2)}")

# ============================================================================
# 17. Element-wise operations (ufuncs)
# ============================================================================
print("\n" + "=" * 70)
print("17. Element-wise Operations (Universal Functions)")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}\n")

# Add using np.add
result_add = np.add(arr, 10)
print(f"np.add(arr, 10): {result_add}")

# Multiply using np.multiply
result_mul = np.multiply(arr, 2)
print(f"np.multiply(arr, 2): {result_mul}")

# Divide using np.divide
result_div = np.divide(arr, 2)
print(f"np.divide(arr, 2): {result_div}")

# ============================================================================
# 18. where() - Conditional selection
# ============================================================================
print("\n" + "=" * 70)
print("18. Where - Conditional Selection")
print("=" * 70)

arr = np.array([1, 5, 3, 8, 2, 9])
print(f"Array: {arr}")

# Replace values based on condition
result = np.where(arr > 5, 'high', 'low')
print(f"np.where(arr > 5, 'high', 'low'): {result}")

# Replace with different array
result = np.where(arr > 5, arr * 10, arr)
print(f"np.where(arr > 5, arr * 10, arr): {result}")

# ============================================================================
# 19. any() and all()
# ============================================================================
print("\n" + "=" * 70)
print("19. any() and all()")
print("=" * 70)

arr = np.array([True, False, True, False])
print(f"Array: {arr}")
print(f"any(): {np.any(arr)}")
print(f"all(): {np.all(arr)}")

arr2 = np.array([1, 2, 3, 0, 5])
print(f"\nArray: {arr2}")
print(f"any() - any non-zero: {np.any(arr2)}")
print(f"all() - all non-zero: {np.all(arr2)}")

# ============================================================================
# 20. In-place operations
# ============================================================================
print("\n" + "=" * 70)
print("20. In-place Operations")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Original: {arr}")

arr += 10
print(f"After arr += 10: {arr}")

arr *= 2
print(f"After arr *= 2: {arr}")

arr = np.array([1, 2, 3, 4, 5])
np.add(arr, 5, out=arr)
print(f"After np.add(arr, 5, out=arr): {arr}")
