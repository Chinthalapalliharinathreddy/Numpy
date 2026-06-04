"""
NumPy Array Indexing - Accessing array elements
"""

import numpy as np

# ============================================================================
# 1. 1D Array Indexing
# ============================================================================
print("=" * 70)
print("1. 1D Array Indexing")
print("=" * 70)

arr = np.array([10, 20, 30, 40, 50])
print(f"Array: {arr}")
print(f"Index 0: {arr[0]}")
print(f"Index 2: {arr[2]}")
print(f"Index 4: {arr[4]}")
print(f"Last element (index -1): {arr[-1]}")
print(f"Second last (index -2): {arr[-2]}")

# ============================================================================
# 2. 2D Array Indexing - Access by row and column
# ============================================================================
print("\n" + "=" * 70)
print("2. 2D Array Indexing")
print("=" * 70)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n{arr2d}\n")
print(f"Element at [0, 0]: {arr2d[0, 0]}")
print(f"Element at [0, 2]: {arr2d[0, 2]}")
print(f"Element at [1, 1]: {arr2d[1, 1]}")
print(f"Element at [2, 2]: {arr2d[2, 2]}")
print(f"Element at [-1, -1]: {arr2d[-1, -1]}")

# Access entire row
print(f"\nFirst row [0, :]: {arr2d[0, :]}")
print(f"Second row [1, :]: {arr2d[1, :]}")

# Access entire column
print(f"\nFirst column [:, 0]: {arr2d[:, 0]}")
print(f"Second column [:, 1]: {arr2d[:, 1]}")

# ============================================================================
# 3. 3D Array Indexing
# ============================================================================
print("\n" + "=" * 70)
print("3. 3D Array Indexing")
print("=" * 70)

arr3d = np.arange(24).reshape(2, 3, 4)
print(f"3D Array shape: {arr3d.shape}\n")
print(f"arr3d:\n{arr3d}\n")
print(f"Element at [0, 0, 0]: {arr3d[0, 0, 0]}")
print(f"Element at [0, 1, 2]: {arr3d[0, 1, 2]}")
print(f"Element at [1, 2, 3]: {arr3d[1, 2, 3]}")
print(f"Element at [-1, -1, -1]: {arr3d[-1, -1, -1]}")

# Access 2D slice
print(f"\nFirst 2D slice [0]:\n{arr3d[0]}")
print(f"\nSecond 2D slice [1]:\n{arr3d[1]}")

# ============================================================================
# 4. Boolean Indexing - Conditional access
# ============================================================================
print("\n" + "=" * 70)
print("4. Boolean Indexing")
print("=" * 70)

arr = np.array([10, 20, 30, 40, 50, 60])
print(f"Array: {arr}")

# Get elements greater than 30
mask = arr > 30
print(f"\nElements > 30: {arr[mask]}")

# Get elements less than 50
mask = arr < 50
print(f"Elements < 50: {arr[mask]}")

# Get even numbers
mask = arr % 2 == 0
print(f"Even numbers: {arr[mask]}")

# Get odd numbers
mask = arr % 2 != 0
print(f"Odd numbers: {arr[mask]}")

# ============================================================================
# 5. Boolean Indexing with 2D Arrays
# ============================================================================
print("\n" + "=" * 70)
print("5. Boolean Indexing with 2D Arrays")
print("=" * 70)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n{arr2d}\n")

# Get elements greater than 5
mask = arr2d > 5
print(f"Mask (arr2d > 5):\n{mask}")
print(f"Elements > 5: {arr2d[mask]}")

# Get elements in specific range
mask = (arr2d >= 3) & (arr2d <= 7)
print(f"\nElements between 3 and 7: {arr2d[mask]}")

# ============================================================================
# 6. Fancy Indexing - Using arrays of indices
# ============================================================================
print("\n" + "=" * 70)
print("6. Fancy Indexing (Integer Array Indexing)")
print("=" * 70)

arr = np.array([10, 20, 30, 40, 50, 60])
print(f"Array: {arr}\n")

# Access specific indices
indices = np.array([0, 2, 4])
print(f"arr[[0, 2, 4]]: {arr[indices]}")

# Access with list
print(f"arr[[1, 3, 5]]: {arr[[1, 3, 5]]}")

# Negative indices
indices = np.array([0, -2, -1])
print(f"arr[[0, -2, -1]]: {arr[indices]}")

# ============================================================================
# 7. Fancy Indexing with 2D Arrays
# ============================================================================
print("\n" + "=" * 70)
print("7. Fancy Indexing with 2D Arrays")
print("=" * 70)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(f"2D Array:\n{arr2d}\n")

# Select specific rows
rows = np.array([0, 2, 3])
print(f"Rows [0, 2, 3]:\n{arr2d[rows]}\n")

# Select specific elements using row and column indices
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 1, 2])
print(f"Diagonal elements: {arr2d[row_indices, col_indices]}")

# ============================================================================
# 8. Using where() for conditional indexing
# ============================================================================
print("\n" + "=" * 70)
print("8. Using where() for Conditional Indexing")
print("=" * 70)

arr = np.array([10, 20, 30, 40, 50])
print(f"Array: {arr}\n")

# Find indices where value > 25
indices = np.where(arr > 25)
print(f"Indices where arr > 25: {indices}")
print(f"Values where arr > 25: {arr[indices]}")

# ============================================================================
# 9. Using where() with 2D arrays
# ============================================================================
print("\n" + "=" * 70)
print("9. Using where() with 2D Arrays")
print("=" * 70)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n{arr2d}\n")

# Find indices where value > 5
indices = np.where(arr2d > 5)
print(f"Indices where arr2d > 5:")
print(f"  Row indices: {indices[0]}")
print(f"  Col indices: {indices[1]}")
print(f"Values: {arr2d[indices]}")

# ============================================================================
# 10. Using nonzero() - Find non-zero elements
# ============================================================================
print("\n" + "=" * 70)
print("10. Using nonzero()")
print("=" * 70)

arr = np.array([0, 10, 0, 20, 0, 30])
print(f"Array: {arr}")

indices = np.nonzero(arr)
print(f"Indices of non-zero elements: {indices[0]}")
print(f"Non-zero values: {arr[indices]}")

# ============================================================================
# 11. Using argmax() and argmin() - Find indices
# ============================================================================
print("\n" + "=" * 70)
print("11. Using argmax() and argmin()")
print("=" * 70)

arr = np.array([15, 32, 8, 45, 22])
print(f"Array: {arr}")
print(f"Index of max value: {np.argmax(arr)}")
print(f"Index of min value: {np.argmin(arr)}")
print(f"Max value: {arr[np.argmax(arr)]}")
print(f"Min value: {arr[np.argmin(arr)]}")

# ============================================================================
# 12. Using argmax() and argmin() with 2D arrays
# ============================================================================
print("\n" + "=" * 70)
print("12. Using argmax/argmin with 2D Arrays")
print("=" * 70)

arr2d = np.array([[1, 5, 3], [8, 2, 4]])
print(f"2D Array:\n{arr2d}\n")

# Flatten and find
print(f"Index of max (flattened): {np.argmax(arr2d)}")
print(f"Index of min (flattened): {np.argmin(arr2d)}")

# Along axis
print(f"Max indices (axis 0): {np.argmax(arr2d, axis=0)}")
print(f"Max indices (axis 1): {np.argmax(arr2d, axis=1)}")

# ============================================================================
# 13. Using searchsorted() - Find insertion point
# ============================================================================
print("\n" + "=" * 70)
print("13. Using searchsorted()")
print("=" * 70)

sorted_arr = np.array([1, 3, 5, 7, 9])
print(f"Sorted array: {sorted_arr}")
print(f"Insertion point for 4: {np.searchsorted(sorted_arr, 4)}")
print(f"Insertion point for 6: {np.searchsorted(sorted_arr, 6)}")
print(f"Insertion point for 8: {np.searchsorted(sorted_arr, 8)}")

# ============================================================================
# 14. Modifying elements by indexing
# ============================================================================
print("\n" + "=" * 70)
print("14. Modifying Elements by Indexing")
print("=" * 70)

arr = np.array([10, 20, 30, 40, 50])
print(f"Original array: {arr}")

arr[0] = 100
print(f"After arr[0] = 100: {arr}")

arr[-1] = 500
print(f"After arr[-1] = 500: {arr}")

# Modify using boolean indexing
arr[arr > 100] = 999
print(f"After arr[arr > 100] = 999: {arr}")

# ============================================================================
# 15. Modifying 2D arrays by indexing
# ============================================================================
print("\n" + "=" * 70)
print("15. Modifying 2D Arrays")
print("=" * 70)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Original 2D array:\n{arr2d}\n")

arr2d[0, 0] = 99
print(f"After arr2d[0, 0] = 99:\n{arr2d}\n")

arr2d[1, :] = [40, 50, 60]
print(f"After arr2d[1, :] = [40, 50, 60]:\n{arr2d}\n")

arr2d[:, 2] = [100, 200, 300]
print(f"After arr2d[:, 2] = [100, 200, 300]:\n{arr2d}")
