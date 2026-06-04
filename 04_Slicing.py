"""
NumPy Array Slicing - Selecting subsets of arrays
"""

import numpy as np

# ============================================================================
# 1. 1D Array Slicing
# ============================================================================
print("=" * 70)
print("1. 1D Array Slicing")
print("=" * 70)

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Array: {arr}\n")

print(f"arr[2:5]: {arr[2:5]}")        # Elements from index 2 to 4
print(f"arr[:3]: {arr[:3]}")          # Elements from start to index 2
print(f"arr[5:]: {arr[5:]}")          # Elements from index 5 to end
print(f"arr[::2]: {arr[::2]}")        # Every 2nd element
print(f"arr[1::2]: {arr[1::2]}")      # Every 2nd element starting from 1
print(f"arr[::-1]: {arr[::-1]}")      # Reversed array
print(f"arr[8:2:-1]: {arr[8:2:-1]}")  # Reverse from index 8 to 3

# ============================================================================
# 2. 2D Array Slicing - Rows
# ============================================================================
print("\n" + "=" * 70)
print("2. 2D Array Slicing - Rows")
print("=" * 70)

arr2d = np.arange(1, 16).reshape(3, 5)
print(f"2D Array:\n{arr2d}\n")

print(f"First row [0]: {arr2d[0]}")
print(f"Second row [1]: {arr2d[1]}")
print(f"Last row [-1]: {arr2d[-1]}\n")

print(f"First two rows [0:2]:\n{arr2d[0:2]}\n")
print(f"All rows [:]:\n{arr2d[:]}\n")
print(f"Reversed rows [::-1]:\n{arr2d[::-1]}")

# ============================================================================
# 3. 2D Array Slicing - Columns
# ============================================================================
print("\n" + "=" * 70)
print("3. 2D Array Slicing - Columns")
print("=" * 70)

arr2d = np.arange(1, 16).reshape(3, 5)
print(f"2D Array:\n{arr2d}\n")

print(f"First column [:, 0]: {arr2d[:, 0]}")
print(f"Last column [:, -1]: {arr2d[:, -1]}\n")

print(f"First two columns [:, 0:2]:\n{arr2d[:, 0:2]}\n")
print(f"Columns 1 to 3 [:, 1:4]:\n{arr2d[:, 1:4]}\n")
print(f"Every 2nd column [:, ::2]:\n{arr2d[:, ::2]}")

# ============================================================================
# 4. 2D Array Slicing - Rows and Columns
# ============================================================================
print("\n" + "=" * 70)
print("4. 2D Array Slicing - Rows and Columns")
print("=" * 70)

arr2d = np.arange(1, 16).reshape(3, 5)
print(f"2D Array:\n{arr2d}\n")

print(f"arr2d[0:2, 0:3]:\n{arr2d[0:2, 0:3]}\n")
print(f"arr2d[1:3, 2:5]:\n{arr2d[1:3, 2:5]}\n")
print(f"arr2d[0:3:2, 0:5:2]:\n{arr2d[0:3:2, 0:5:2]}\n")
print(f"arr2d[:, 1:4]:\n{arr2d[:, 1:4]}\n")
print(f"arr2d[1:3, :]:\n{arr2d[1:3, :]}")

# ============================================================================
# 5. 3D Array Slicing
# ============================================================================
print("\n" + "=" * 70)
print("5. 3D Array Slicing")
print("=" * 70)

arr3d = np.arange(1, 25).reshape(2, 3, 4)
print(f"3D Array shape: {arr3d.shape}")
print(f"3D Array:\n{arr3d}\n")

print(f"First 2D slice [0]:\n{arr3d[0]}\n")
print(f"Second element of first 2D slice [0, 1]:\n{arr3d[0, 1]}\n")
print(f"arr3d[0:2, 1:3, 0:2]:\n{arr3d[0:2, 1:3, 0:2]}\n")
print(f"arr3d[:, :, ::2]:\n{arr3d[:, :, ::2]}")

# ============================================================================
# 6. Slicing with Step
# ============================================================================
print("\n" + "=" * 70)
print("6. Slicing with Step")
print("=" * 70)

arr = np.arange(0, 20)
print(f"Array: {arr}\n")

print(f"Every 3rd element [::3]: {arr[::3]}")
print(f"Every 4th element [::4]: {arr[::4]}")
print(f"Every 2nd starting at 1 [1::2]: {arr[1::2]}")
print(f"Every 3rd starting at 2 [2::3]: {arr[2::3]}")

# Negative steps (reverse)
print(f"\nReverse [::−1]: {arr[::-1]}")
print(f"Every 2nd reversed [::−2]: {arr[::-2]}")
print(f"From 15 to 5 reversed [15:5:−1]: {arr[15:5:-1]}")

# ============================================================================
# 7. Slicing and Modifying
# ============================================================================
print("\n" + "=" * 70)
print("7. Slicing and Modifying")
print("=" * 70)

arr = np.arange(10)
print(f"Original: {arr}")

arr[2:5] = [20, 30, 40]
print(f"After arr[2:5] = [20, 30, 40]: {arr}")

arr[::2] = 0
print(f"After arr[::2] = 0: {arr}")

# ============================================================================
# 8. Copy vs View in Slicing
# ============================================================================
print("\n" + "=" * 70)
print("8. Copy vs View in Slicing")
print("=" * 70)

original = np.arange(10)
slice_view = original[2:5]
slice_copy = original[2:5].copy()

print(f"Original: {original}")
print(f"View: {slice_view}")
print(f"Copy: {slice_copy}\n")

# Modify view - affects original
original[3] = 999
print(f"After modifying original[3] = 999:")
print(f"Original: {original}")
print(f"View: {slice_view}")
print(f"Copy: {slice_copy}")

# ============================================================================
# 9. Ellipsis (...) in Slicing
# ============================================================================
print("\n" + "=" * 70)
print("9. Ellipsis (...) in Slicing")
print("=" * 70)

arr3d = np.arange(24).reshape(2, 3, 4)
print(f"3D Array shape: {arr3d.shape}\n")

print(f"arr3d[0, ...] (same as arr3d[0, :, :]):\n{arr3d[0, ...]}\n")
print(f"arr3d[..., 0] (same as arr3d[:, :, 0]):\n{arr3d[..., 0]}\n")
print(f"arr3d[0, ...] shape: {arr3d[0, ...].shape}")

# ============================================================================
# 10. Slicing with Newaxis
# ============================================================================
print("\n" + "=" * 70)
print("10. Slicing with np.newaxis")
print("=" * 70)

arr1d = np.array([1, 2, 3])
print(f"1D array shape: {arr1d.shape}")
print(f"Array: {arr1d}\n")

arr_2d = arr1d[np.newaxis, :]
print(f"arr1d[np.newaxis, :] shape: {arr_2d.shape}")
print(f"Result:\n{arr_2d}\n")

arr_col = arr1d[:, np.newaxis]
print(f"arr1d[:, np.newaxis] shape: {arr_col.shape}")
print(f"Result:\n{arr_col}\n")

# Add dimension at different positions
arr1d = np.array([1, 2, 3])
print(f"Original shape: {arr1d.shape}")
print(f"Add at start [np.newaxis, :]: {arr1d[np.newaxis, :].shape}")
print(f"Add at end [:, np.newaxis]: {arr1d[:, np.newaxis].shape}")

# ============================================================================
# 11. Advanced slicing with multiple conditions
# ============================================================================
print("\n" + "=" * 70)
print("11. Advanced Slicing with Conditions")
print("=" * 70)

arr = np.arange(1, 11)
print(f"Array: {arr}\n")

# Get elements at indices where condition is true
even_mask = arr % 2 == 0
print(f"Even numbers: {arr[even_mask]}")

# Multiple conditions
between_3_and_8 = (arr >= 3) & (arr <= 8)
print(f"Numbers between 3 and 8: {arr[between_3_and_8]}")

# ============================================================================
# 12. Slicing 2D arrays - Submatrices
# ============================================================================
print("\n" + "=" * 70)
print("12. Extracting Submatrices")
print("=" * 70)

arr2d = np.arange(1, 26).reshape(5, 5)
print(f"5x5 Matrix:\n{arr2d}\n")

print(f"Top-left 3x3:\n{arr2d[:3, :3]}\n")
print(f"Bottom-right 2x2:\n{arr2d[-2:, -2:]}\n")
print(f"Center 3x3:\n{arr2d[1:4, 1:4]}")

# ============================================================================
# 13. Strided slicing patterns
# ============================================================================
print("\n" + "=" * 70)
print("13. Strided Slicing Patterns")
print("=" * 70)

arr2d = np.arange(1, 26).reshape(5, 5)
print(f"5x5 Matrix:\n{arr2d}\n")

print(f"Every 2nd row (::2):\n{arr2d[::2]}\n")
print(f"Every 2nd column (::2):\n{arr2d[:, ::2]}\n")
print(f"Every 2nd row and column (::2, ::2):\n{arr2d[::2, ::2]}")

# ============================================================================
# 14. Slicing with negative indices
# ============================================================================
print("\n" + "=" * 70)
print("14. Slicing with Negative Indices")
print("=" * 70)

arr = np.arange(10)
print(f"Array: {arr}\n")

print(f"Last 3 elements [-3:]: {arr[-3:]}")
print(f"All but last 2 [:-2]: {arr[:-2]}")
print(f"From -7 to -2 [-7:-2]: {arr[-7:-2]}")

# ============================================================================
# 15. Combining slicing operations
# ============================================================================
print("\n" + "=" * 70)
print("15. Combining Slicing Operations")
print("=" * 70)

arr2d = np.arange(1, 26).reshape(5, 5)
print(f"Original 5x5 matrix:\n{arr2d}\n")

# Complex slice: rows 1-4, columns 1-4, every 2nd element
result = arr2d[1:4, 1:4][::2]
print(f"arr2d[1:4, 1:4][::2]:\n{result}")
