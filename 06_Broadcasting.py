"""
NumPy Broadcasting - Operating on arrays of different shapes
"""

import numpy as np

# ============================================================================
# 1. Broadcasting Rule - Scalar with Array
# ============================================================================
print("=" * 70)
print("1. Broadcasting - Scalar with Array")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
scalar = 10

print(f"Array: {arr}")
print(f"Scalar: {scalar}\n")

print(f"Array + Scalar: {arr + scalar}")
print(f"Array * Scalar: {arr * scalar}")
print(f"Scalar / Array: {scalar / arr}")

# ============================================================================
# 2. Broadcasting - 1D and 2D Arrays
# ============================================================================
print("\n" + "=" * 70)
print("2. Broadcasting - 1D and 2D Arrays")
print("=" * 70)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_1d = np.array([10, 20, 30])

print(f"2D Array:\n{arr_2d}")
print(f"\n1D Array (row): {arr_1d}\n")

# 1D array is broadcast to match 2D array shape
result = arr_2d + arr_1d
print(f"2D + 1D (broadcast row-wise):\n{result}\n")

result = arr_2d * arr_1d
print(f"2D * 1D (broadcast row-wise):\n{result}")

# ============================================================================
# 3. Broadcasting - Column vector with Row vector
# ============================================================================
print("\n" + "=" * 70)
print("3. Broadcasting - Column Vector with Row Vector")
print("=" * 70)

arr_row = np.array([[1, 2, 3]])  # Shape: (1, 3)
arr_col = np.array([[10], [20], [30]])  # Shape: (3, 1)

print(f"Row array shape: {arr_row.shape}")
print(f"Row array:\n{arr_row}\n")

print(f"Column array shape: {arr_col.shape}")
print(f"Column array:\n{arr_col}\n")

# Broadcasting: (1, 3) and (3, 1) -> (3, 3)
result = arr_row + arr_col
print(f"Row + Column (broadcast to (3, 3)):\n{result}\n")

result = arr_row * arr_col
print(f"Row * Column (broadcast to (3, 3)):\n{result}")

# ============================================================================
# 4. Broadcasting - Different dimensions
# ============================================================================
print("\n" + "=" * 70)
print("4. Broadcasting - Different Dimensions")
print("=" * 70)

arr_1d = np.array([1, 2, 3])  # Shape: (3,)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)

print(f"1D array shape: {arr_1d.shape}")
print(f"1D array: {arr_1d}\n")

print(f"2D array shape: {arr_2d.shape}")
print(f"2D array:\n{arr_2d}\n")

# Broadcasting: (3,) -> (2, 3)
result = arr_2d + arr_1d
print(f"2D + 1D (broadcast to (2, 3)):\n{result}")

# ============================================================================
# 5. Broadcasting - Adding 3D and 1D
# ============================================================================
print("\n" + "=" * 70)
print("5. Broadcasting - 3D and 1D Arrays")
print("=" * 70)

arr_3d = np.arange(1, 13).reshape(2, 2, 3)  # Shape: (2, 2, 3)
arr_1d = np.array([10, 20, 30])  # Shape: (3,)

print(f"3D array shape: {arr_3d.shape}")
print(f"3D array:\n{arr_3d}\n")

print(f"1D array shape: {arr_1d.shape}")
print(f"1D array: {arr_1d}\n")

# Broadcasting: (3,) -> (2, 2, 3)
result = arr_3d + arr_1d
print(f"3D + 1D (broadcast to (2, 2, 3)):\n{result}")

# ============================================================================
# 6. Broadcasting - Using newaxis for explicit dimension control
# ============================================================================
print("\n" + "=" * 70)
print("6. Broadcasting - Using np.newaxis")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Original array shape: {arr.shape}")
print(f"Array: {arr}\n")

# Add new axis at different positions
row_vector = arr[np.newaxis, :]  # Shape: (1, 5)
col_vector = arr[:, np.newaxis]  # Shape: (5, 1)

print(f"Row vector shape: {row_vector.shape}")
print(f"Row vector: {row_vector}\n")

print(f"Column vector shape: {col_vector.shape}")
print(f"Column vector:\n{col_vector}\n")

# Broadcasting with these
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
result = arr_2d + row_vector
print(f"2D array + row_vector:\n{result}\n")

result = arr_2d + col_vector
print(f"2D array + col_vector:\n{result}")

# ============================================================================
# 7. Broadcasting - Outer product
# ============================================================================
print("\n" + "=" * 70)
print("7. Broadcasting - Outer Product")
print("=" * 70)

arr1 = np.array([1, 2, 3])  # Shape: (3,)
arr2 = np.array([10, 20, 30, 40])  # Shape: (4,)

# Create outer product using broadcasting
col = arr1[:, np.newaxis]  # Shape: (3, 1)
row = arr2[np.newaxis, :]  # Shape: (1, 4)

print(f"arr1 shape: {arr1.shape} -> {col.shape}")
print(f"arr2 shape: {arr2.shape} -> {row.shape}\n")

outer_product = col * row
print(f"Outer product (arr1[:, np.newaxis] * arr2[np.newaxis, :]):\n{outer_product}")

# Using np.outer
print(f"\nUsing np.outer:\n{np.outer(arr1, arr2)}")

# ============================================================================
# 8. Broadcasting - Common operations
# ============================================================================
print("\n" + "=" * 70)
print("8. Broadcasting - Common Operations")
print("=" * 70)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mean = np.array([4, 5, 6])

print(f"Data:\n{data}\n")
print(f"Mean: {mean}\n")

# Center data by subtracting mean
centered = data - mean
print(f"Data - Mean (centered):\n{centered}")

# ============================================================================
# 9. Broadcasting - Row and column standardization
# ============================================================================
print("\n" + "=" * 70)
print("9. Broadcasting - Standardization")
print("=" * 70)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
print(f"Data:\n{data}\n")

# Normalize by rows
row_min = np.min(data, axis=1, keepdims=True)
row_max = np.max(data, axis=1, keepdims=True)
normalized_rows = (data - row_min) / (row_max - row_min)

print(f"Row min: {row_min.T}")
print(f"Row max: {row_max.T}\n")
print(f"Normalized by rows:\n{normalized_rows}\n")

# Normalize by columns
col_min = np.min(data, axis=0)
col_max = np.max(data, axis=0)
normalized_cols = (data - col_min) / (col_max - col_min)

print(f"Column min: {col_min}")
print(f"Column max: {col_max}\n")
print(f"Normalized by columns:\n{normalized_cols}")

# ============================================================================
# 10. Broadcasting rules and shapes
# ============================================================================
print("\n" + "=" * 70)
print("10. Broadcasting Rules Summary")
print("=" * 70)

print("""
Broadcasting Rule:
1. If arrays have different number of dimensions, pad the smaller one 
   with 1s on the left.
2. Arrays are compatible for broadcasting if their dimensions match 
   or one of them is 1.
3. If one dimension is 1, it's stretched to match the other array.

Examples:
(3,) and (3,) -> (3,)                   ✓
(3, 1) and (3, 4) -> (3, 4)             ✓
(3,) and (1,) -> (3,)                   ✓
(2, 3, 4) and (3, 4) -> (2, 3, 4)       ✓
(2, 3, 4) and (2, 3, 1) -> (2, 3, 4)    ✓
(3,) and (4,) -> ERROR                  ✗
(2, 3) and (3, 2) -> ERROR              ✗
""")

# ============================================================================
# 11. Invalid broadcasting
# ============================================================================
print("=" * 70)
print("11. Invalid Broadcasting (Examples)")
print("=" * 70)

arr1 = np.array([1, 2, 3])  # Shape: (3,)
arr2 = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)

print(f"arr1 shape: {arr1.shape}")
print(f"arr2 shape: {arr2.shape}")

try:
    result = arr1 + arr2
except ValueError as e:
    print(f"Error: {e}")

# ============================================================================
# 12. Broadcasting with keepdims
# ============================================================================
print("\n" + "=" * 70)
print("12. Broadcasting with keepdims")
print("=" * 70)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array:\n{arr}\n")

# Without keepdims
mean_no_dims = np.mean(arr, axis=0)
print(f"Mean without keepdims shape: {mean_no_dims.shape}")
print(f"Mean: {mean_no_dims}")

# With keepdims
mean_with_dims = np.mean(arr, axis=0, keepdims=True)
print(f"\nMean with keepdims shape: {mean_with_dims.shape}")
print(f"Mean: {mean_with_dims}\n")

# Broadcasting difference
print(f"Broadcasting arr - mean_no_dims can fail!")
print(f"Broadcasting arr - mean_with_dims works:\n{arr - mean_with_dims}")

# ============================================================================
# 13. Broadcasting in matrix operations
# ============================================================================
print("\n" + "=" * 70)
print("13. Broadcasting in Matrix Operations")
print("=" * 70)

A = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
b = np.array([10, 20, 30])  # Shape: (3,)

print(f"Matrix A:\n{A}")
print(f"Vector b: {b}\n")

# Broadcast b to match A
result = A + b
print(f"A + b (broadcast b to (2, 3)):\n{result}\n")

# Multiply each row by elements of b
result = A * b
print(f"A * b (element-wise):\n{result}")

# ============================================================================
# 14. Broadcasting efficiency
# ============================================================================
print("\n" + "=" * 70)
print("14. Broadcasting is Memory Efficient")
print("=" * 70)

# Large array
large_arr = np.arange(1000000).reshape(1000, 1000)
scalar_arr = np.array([1, 2, 3, 4, 5, 1000, 999, 998, 997, 996])

print(f"Large array shape: {large_arr.shape}")
print(f"Small array shape: {scalar_arr.shape}\n")

# Broadcasting doesn't create copies - it's computed on the fly
result = large_arr + scalar_arr[0]
print(f"Broadcasting is efficient - no unnecessary copies created!")
print(f"Result shape: {result.shape}")

# ============================================================================
# 15. Broadcasting with reshape
# ============================================================================
print("\n" + "=" * 70)
print("15. Broadcasting with Reshape")
print("=" * 70)

arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = np.arange(1, 19).reshape(3, 6)

print(f"1D array shape: {arr1d.shape}")
print(f"1D array: {arr1d}\n")

print(f"2D array shape: {arr2d.shape}")
print(f"2D array:\n{arr2d}\n")

# Reshape 1D to broadcast as column
arr_col = arr1d[:, np.newaxis]
print(f"Reshaped 1D as column: {arr_col.shape}\n")

# This allows column-wise operations
arr_reshaped = np.arange(1, 13).reshape(2, 6)
result = arr_reshaped + arr1d
print(f"2D + 1D (row broadcast):\n{result}")
