"""
NumPy Array Creation - Different ways to create arrays
"""

import numpy as np

# ============================================================================
# 1. Creating arrays from lists
# ============================================================================
print("=" * 70)
print("1. Creating Arrays from Lists")
print("=" * 70)

# 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(f"1D array: {arr1d}")
print(f"Type: {type(arr1d)}")

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array:\n{arr2d}")

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"\n3D array:\n{arr3d}")

# ============================================================================
# 2. Using arange() - Create arrays with regular intervals
# ============================================================================
print("\n" + "=" * 70)
print("2. Using arange()")
print("=" * 70)

# arange(start, stop, step)
arr_range1 = np.arange(10)
print(f"np.arange(10): {arr_range1}")

arr_range2 = np.arange(2, 10)
print(f"np.arange(2, 10): {arr_range2}")

arr_range3 = np.arange(0, 20, 2)
print(f"np.arange(0, 20, 2): {arr_range3}")

arr_range4 = np.arange(10, 0, -1)
print(f"np.arange(10, 0, -1): {arr_range4}")

# ============================================================================
# 3. Using linspace() - Create arrays with specific number of elements
# ============================================================================
print("\n" + "=" * 70)
print("3. Using linspace()")
print("=" * 70)

# linspace(start, stop, num_elements)
arr_linspace1 = np.linspace(0, 10, 5)
print(f"np.linspace(0, 10, 5): {arr_linspace1}")

arr_linspace2 = np.linspace(0, 1, 11)
print(f"np.linspace(0, 1, 11): {arr_linspace2}")

# ============================================================================
# 4. Using logspace() - Create arrays with logarithmic spacing
# ============================================================================
print("\n" + "=" * 70)
print("4. Using logspace()")
print("=" * 70)

# logspace(start, stop, num_elements, base=10)
arr_logspace = np.logspace(0, 4, 5)
print(f"np.logspace(0, 4, 5): {arr_logspace}")

arr_logspace_base2 = np.logspace(0, 3, 4, base=2)
print(f"np.logspace(0, 3, 4, base=2): {arr_logspace_base2}")

# ============================================================================
# 5. Using zeros() - Create arrays filled with zeros
# ============================================================================
print("\n" + "=" * 70)
print("5. Using zeros()")
print("=" * 70)

zeros_1d = np.zeros(5)
print(f"np.zeros(5): {zeros_1d}")

zeros_2d = np.zeros((3, 4))
print(f"np.zeros((3, 4)):\n{zeros_2d}")

zeros_int = np.zeros(5, dtype=int)
print(f"np.zeros(5, dtype=int): {zeros_int}")

# ============================================================================
# 6. Using ones() - Create arrays filled with ones
# ============================================================================
print("\n" + "=" * 70)
print("6. Using ones()")
print("=" * 70)

ones_1d = np.ones(5)
print(f"np.ones(5): {ones_1d}")

ones_2d = np.ones((2, 3))
print(f"np.ones((2, 3)):\n{ones_2d}")

ones_complex = np.ones(4, dtype=complex)
print(f"np.ones(4, dtype=complex): {ones_complex}")

# ============================================================================
# 7. Using full() - Create arrays filled with a specific value
# ============================================================================
print("\n" + "=" * 70)
print("7. Using full()")
print("=" * 70)

full_arr = np.full(5, 7)
print(f"np.full(5, 7): {full_arr}")

full_2d = np.full((3, 3), 3.14)
print(f"np.full((3, 3), 3.14):\n{full_2d}")

# ============================================================================
# 8. Using eye() - Create identity matrix
# ============================================================================
print("\n" + "=" * 70)
print("8. Using eye()")
print("=" * 70)

eye_mat = np.eye(3)
print(f"np.eye(3):\n{eye_mat}")

eye_mat_offset = np.eye(4, k=1)
print(f"np.eye(4, k=1):\n{eye_mat_offset}")

# ============================================================================
# 9. Using identity() - Create identity matrix
# ============================================================================
print("\n" + "=" * 70)
print("9. Using identity()")
print("=" * 70)

identity_mat = np.identity(3)
print(f"np.identity(3):\n{identity_mat}")

# ============================================================================
# 10. Using diag() - Create diagonal array
# ============================================================================
print("\n" + "=" * 70)
print("10. Using diag()")
print("=" * 70)

diag_arr = np.diag([1, 2, 3])
print(f"np.diag([1, 2, 3]):\n{diag_arr}")

# ============================================================================
# 11. Using random arrays
# ============================================================================
print("\n" + "=" * 70)
print("11. Using random()")
print("=" * 70)

# Random values between 0 and 1
rand_arr = np.random.random(5)
print(f"np.random.random(5): {rand_arr}")

# Random integers
rand_int = np.random.randint(0, 10, 5)
print(f"np.random.randint(0, 10, 5): {rand_int}")

# Random normal distribution
rand_normal = np.random.randn(5)
print(f"np.random.randn(5): {rand_normal}")

# ============================================================================
# 12. Using tile() - Repeat array
# ============================================================================
print("\n" + "=" * 70)
print("12. Using tile()")
print("=" * 70)

arr = np.array([1, 2, 3])
tiled = np.tile(arr, 3)
print(f"Original: {arr}")
print(f"np.tile(arr, 3): {tiled}")

tiled_2d = np.tile(arr, (2, 3))
print(f"np.tile(arr, (2, 3)):\n{tiled_2d}")

# ============================================================================
# 13. Using repeat() - Repeat elements
# ============================================================================
print("\n" + "=" * 70)
print("13. Using repeat()")
print("=" * 70)

arr = np.array([1, 2, 3])
repeated = np.repeat(arr, 3)
print(f"Original: {arr}")
print(f"np.repeat(arr, 3): {repeated}")

repeated_2d = np.repeat([1, 2], 2, axis=1)
print(f"np.repeat([1, 2], 2, axis=1):\n{repeated_2d}")

# ============================================================================
# 14. Using reshape - Create and reshape arrays
# ============================================================================
print("\n" + "=" * 70)
print("14. Using reshape()")
print("=" * 70)

arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(f"Original shape (12,): {arr}")
print(f"Reshaped (3, 4):\n{reshaped}")

# ============================================================================
# 15. Using concatenate - Combine arrays
# ============================================================================
print("\n" + "=" * 70)
print("15. Using concatenate()")
print("=" * 70)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
combined = np.concatenate([arr1, arr2])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Concatenated: {combined}")

# ============================================================================
# 16. Using stack - Stack arrays along new dimension
# ============================================================================
print("\n" + "=" * 70)
print("16. Using stack()")
print("=" * 70)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
stacked = np.stack([arr1, arr2])
print(f"np.stack([arr1, arr2]):\n{stacked}")

# ============================================================================
# 17. Create array from existing data
# ============================================================================
print("\n" + "=" * 70)
print("17. Using asarray()")
print("=" * 70)

list_data = [1, 2, 3, 4, 5]
arr_from_list = np.asarray(list_data)
print(f"From list: {arr_from_list}")

tuple_data = (10, 20, 30)
arr_from_tuple = np.asarray(tuple_data)
print(f"From tuple: {arr_from_tuple}")

# ============================================================================
# 18. Create array with specified dtype
# ============================================================================
print("\n" + "=" * 70)
print("18. Arrays with Different Data Types")
print("=" * 70)

int_arr = np.array([1, 2, 3], dtype=np.int32)
print(f"int32 array: {int_arr}, dtype: {int_arr.dtype}")

float_arr = np.array([1, 2, 3], dtype=np.float64)
print(f"float64 array: {float_arr}, dtype: {float_arr.dtype}")

complex_arr = np.array([1, 2, 3], dtype=np.complex128)
print(f"complex128 array: {complex_arr}, dtype: {complex_arr.dtype}")

bool_arr = np.array([True, False, True], dtype=bool)
print(f"bool array: {bool_arr}, dtype: {bool_arr.dtype}")

# ============================================================================
# 19. Using fromiter() - Create array from iterator
# ============================================================================
print("\n" + "=" * 70)
print("19. Using fromiter()")
print("=" * 70)

# Create array from range
arr_iter = np.fromiter(range(5), dtype=float)
print(f"np.fromiter(range(5), dtype=float): {arr_iter}")

# ============================================================================
# 20. Using append() - Append values to array
# ============================================================================
print("\n" + "=" * 70)
print("20. Using append()")
print("=" * 70)

arr = np.array([1, 2, 3])
appended = np.append(arr, [4, 5, 6])
print(f"Original: {arr}")
print(f"After append([4, 5, 6]): {appended}")
