"""
NumPy Reshape and Flatten - Changing array shapes
"""

import numpy as np

# ============================================================================
# 1. Reshape - Change array dimensions
# ============================================================================
print("=" * 70)
print("1. Reshape - Change Array Dimensions")
print("=" * 70)

arr = np.arange(12)
print(f"Original array: {arr}")
print(f"Original shape: {arr.shape}\n")

# Reshape to 2D
arr_2d = arr.reshape(3, 4)
print(f"Reshaped to (3, 4):\n{arr_2d}")
print(f"Shape: {arr_2d.shape}\n")

# Reshape to 3D
arr_3d = arr.reshape(2, 3, 2)
print(f"Reshaped to (2, 3, 2):\n{arr_3d}")
print(f"Shape: {arr_3d.shape}\n")

# Reshape back to 1D
arr_1d = arr_3d.reshape(-1)
print(f"Reshaped back to 1D: {arr_1d}")
print(f"Shape: {arr_1d.shape}")

# ============================================================================
# 2. Reshape with -1 (automatic dimension)
# ============================================================================
print("\n" + "=" * 70)
print("2. Reshape with -1 (Automatic Dimension)")
print("=" * 70)

arr = np.arange(24)
print(f"Array size: {arr.size}\n")

# Let numpy calculate one dimension
print(f"reshape(-1, 6): {arr.reshape(-1, 6).shape}")
print(f"reshape(4, -1): {arr.reshape(4, -1).shape}")
print(f"reshape(2, 3, -1): {arr.reshape(2, 3, -1).shape}")
print(f"reshape(-1, 1): {arr.reshape(-1, 1).shape}")
print(f"reshape(1, -1): {arr.reshape(1, -1).shape}")

# ============================================================================
# 3. Flatten - Convert to 1D
# ============================================================================
print("\n" + "=" * 70)
print("3. Flatten - Convert to 1D")
print("=" * 70)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}\n")

# Using flatten()
flattened = arr_2d.flatten()
print(f"flatten() result: {flattened}")
print(f"Shape: {flattened.shape}\n")

# Using reshape(-1)
reshaped = arr_2d.reshape(-1)
print(f"reshape(-1) result: {reshaped}")
print(f"Shape: {reshaped.shape}")

# ============================================================================
# 4. Flatten vs Reshape - Copy vs View
# ============================================================================
print("\n" + "=" * 70)
print("4. Flatten vs Reshape - Copy vs View")
print("=" * 70)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original 2D array:\n{arr_2d}\n")

# flatten() creates a copy
flat_copy = arr_2d.flatten()
flat_copy[0] = 999
print(f"After modifying flatten() result:")
print(f"Original: {arr_2d.flat[0]} (unchanged)")
print(f"Copy: {flat_copy[0]} (changed)\n")

# reshape() creates a view
reshaped_view = arr_2d.reshape(-1)
reshaped_view[0] = 999
print(f"After modifying reshape() result:")
print(f"Original: {arr_2d.flat[0]} (changed - it's a view!)")
print(f"View: {reshaped_view[0]} (changed)")

# ============================================================================
# 5. Ravel - Flatten with optional order
# ============================================================================
print("\n" + "=" * 70)
print("5. Ravel - Flatten with Order Options")
print("=" * 70)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr}\n")

# C-order (row-major) - default
raveled_c = np.ravel(arr, order='C')
print(f"Ravel with order='C' (row-major): {raveled_c}\n")

# Fortran order (column-major)
raveled_f = np.ravel(arr, order='F')
print(f"Ravel with order='F' (column-major): {raveled_f}")

# ============================================================================
# 6. Reshape with different orders
# ============================================================================
print("\n" + "=" * 70)
print("6. Reshape with Different Orders")
print("=" * 70)

arr = np.arange(6)
print(f"1D Array: {arr}\n")

# C-order (row-major)
arr_c = arr.reshape(2, 3, order='C')
print(f"reshape((2, 3), order='C'):\n{arr_c}\n")

# Fortran order (column-major)
arr_f = arr.reshape(2, 3, order='F')
print(f"reshape((2, 3), order='F'):\n{arr_f}")

# ============================================================================
# 7. Transpose
# ============================================================================
print("\n" + "=" * 70)
print("7. Transpose")
print("=" * 70)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original array:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}\n")

# Transpose using T attribute
transposed = arr_2d.T
print(f"Transposed using .T:\n{transposed}")
print(f"Shape: {transposed.shape}\n")

# Transpose using transpose()
transposed2 = np.transpose(arr_2d)
print(f"Transposed using transpose():\n{transposed2}\n")

# Double transpose
print(f"Double transpose:\n{arr_2d.T.T}")

# ============================================================================
# 8. Transpose 3D array
# ============================================================================
print("\n" + "=" * 70)
print("8. Transpose 3D Array")
print("=" * 70)

arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"Original 3D array shape: {arr_3d.shape}")
print(f"Original:\n{arr_3d}\n")

# Transpose reverses axes
transposed_3d = np.transpose(arr_3d)
print(f"Transposed shape (axes reversed): {transposed_3d.shape}")
print(f"Transposed:\n{transposed_3d}\n")

# Specify axes order
transposed_custom = np.transpose(arr_3d, axes=(2, 0, 1))
print(f"Transpose with axes=(2, 0, 1) shape: {transposed_custom.shape}")

# ============================================================================
# 9. Swapaxes - Swap specific axes
# ============================================================================
print("\n" + "=" * 70)
print("9. Swapaxes - Swap Specific Axes")
print("=" * 70)

arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"Original shape: {arr_3d.shape}\n")

# Swap axes 0 and 2
swapped = np.swapaxes(arr_3d, 0, 2)
print(f"After swapping axes 0 and 2: {swapped.shape}\n")

# Swap axes 1 and 2
swapped2 = np.swapaxes(arr_3d, 1, 2)
print(f"After swapping axes 1 and 2: {swapped2.shape}")

# ============================================================================
# 10. Moveaxis - Move axis to new position
# ============================================================================
print("\n" + "=" * 70)
print("10. Moveaxis - Move Axis to New Position")
print("=" * 70)

arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"Original shape: {arr_3d.shape}\n")

# Move axis 0 to position 2
moved = np.moveaxis(arr_3d, 0, 2)
print(f"Move axis 0 to position 2: {moved.shape}\n")

# Move axis 2 to position 0
moved2 = np.moveaxis(arr_3d, 2, 0)
print(f"Move axis 2 to position 0: {moved2.shape}")

# ============================================================================
# 11. Expand dims - Add new axis
# ============================================================================
print("\n" + "=" * 70)
print("11. Expand Dims - Add New Axis")
print("=" * 70)

arr = np.array([1, 2, 3])
print(f"Original array shape: {arr.shape}")
print(f"Array: {arr}\n")

# Add axis at position 0
expanded_0 = np.expand_dims(arr, axis=0)
print(f"expand_dims(axis=0) shape: {expanded_0.shape}")
print(f"Result: {expanded_0}\n")

# Add axis at position 1
expanded_1 = np.expand_dims(arr, axis=1)
print(f"expand_dims(axis=1) shape: {expanded_1.shape}")
print(f"Result:\n{expanded_1}\n")

# Add axis at position 2 (last)
expanded_2 = np.expand_dims(arr, axis=2)
print(f"expand_dims(axis=2) shape: {expanded_2.shape}")

# ============================================================================
# 12. Squeeze - Remove axes of length 1
# ============================================================================
print("\n" + "=" * 70)
print("12. Squeeze - Remove Axes of Length 1")
print("=" * 70)

arr = np.array([[[1, 2, 3]]])
print(f"Original shape: {arr.shape}")
print(f"Array: {arr}\n")

# Remove all axes of length 1
squeezed = np.squeeze(arr)
print(f"Squeezed shape: {squeezed.shape}")
print(f"Result: {squeezed}\n")

# Squeeze specific axis
arr2 = np.arange(6).reshape(1, 6, 1)
print(f"Array shape: {arr2.shape}")
squeezed_axis0 = np.squeeze(arr2, axis=0)
print(f"Squeeze axis 0: {squeezed_axis0.shape}")
squeezed_axis2 = np.squeeze(arr2, axis=2)
print(f"Squeeze axis 2: {squeezed_axis2.shape}")

# ============================================================================
# 13. Stack - Join arrays along new axis
# ============================================================================
print("\n" + "=" * 70)
print("13. Stack - Join Arrays Along New Axis")
print("=" * 70)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}\n")

# Stack along axis 0 (rows)
stacked_0 = np.stack([arr1, arr2], axis=0)
print(f"np.stack([arr1, arr2], axis=0) shape: {stacked_0.shape}")
print(f"Result:\n{stacked_0}\n")

# Stack along axis 1 (columns)
stacked_1 = np.stack([arr1, arr2], axis=1)
print(f"np.stack([arr1, arr2], axis=1) shape: {stacked_1.shape}")
print(f"Result:\n{stacked_1}")

# ============================================================================
# 14. Concatenate - Join arrays
# ============================================================================
print("\n" + "=" * 70)
print("14. Concatenate - Join Arrays")
print("=" * 70)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}\n")

# Concatenate along axis 0 (default)
concat = np.concatenate([arr1, arr2])
print(f"np.concatenate([arr1, arr2]): {concat}\n")

# 2D concatenation
arr2d_1 = np.array([[1, 2], [3, 4]])
arr2d_2 = np.array([[5, 6], [7, 8]])

print(f"Array 2D 1:\n{arr2d_1}\n")
print(f"Array 2D 2:\n{arr2d_2}\n")

# Along axis 0 (rows)
concat_0 = np.concatenate([arr2d_1, arr2d_2], axis=0)
print(f"Concatenate along axis 0:\n{concat_0}\n")

# Along axis 1 (columns)
concat_1 = np.concatenate([arr2d_1, arr2d_2], axis=1)
print(f"Concatenate along axis 1:\n{concat_1}")

# ============================================================================
# 15. Tile and Repeat
# ============================================================================
print("\n" + "=" * 70)
print("15. Tile and Repeat")
print("=" * 70)

arr = np.array([1, 2, 3])
print(f"Original array: {arr}\n")

# Tile - repeat entire array
tiled = np.tile(arr, 3)
print(f"np.tile(arr, 3): {tiled}\n")

# Tile in 2D
tiled_2d = np.tile(arr, (2, 3))
print(f"np.tile(arr, (2, 3)):\n{tiled_2d}\n")

# Repeat - repeat individual elements
repeated = np.repeat(arr, 3)
print(f"np.repeat(arr, 3): {repeated}\n")

# Repeat along axis
arr2d = np.array([[1, 2], [3, 4]])
repeated_axis0 = np.repeat(arr2d, 2, axis=0)
print(f"np.repeat(arr2d, 2, axis=0):\n{repeated_axis0}\n")

repeated_axis1 = np.repeat(arr2d, 2, axis=1)
print(f"np.repeat(arr2d, 2, axis=1):\n{repeated_axis1}")
