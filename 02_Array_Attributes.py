"""
NumPy Array Attributes - Understanding array properties
"""

import numpy as np

# ============================================================================
# 1. Shape - Dimensions of array
# ============================================================================
print("=" * 70)
print("1. Array Shape")
print("=" * 70)

arr1d = np.array([1, 2, 3, 4, 5])
print(f"1D array: {arr1d}")
print(f"Shape: {arr1d.shape}")  # (5,)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D array:\n{arr2d}")
print(f"Shape: {arr2d.shape}")  # (2, 3) - 2 rows, 3 columns

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"\n3D array:\n{arr3d}")
print(f"Shape: {arr3d.shape}")  # (2, 2, 2)

# ============================================================================
# 2. Ndim - Number of dimensions
# ============================================================================
print("\n" + "=" * 70)
print("2. Number of Dimensions (ndim)")
print("=" * 70)

arr1d = np.array([1, 2, 3])
arr2d = np.array([[1, 2], [3, 4]])
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"1D array ndim: {arr1d.ndim}")
print(f"2D array ndim: {arr2d.ndim}")
print(f"3D array ndim: {arr3d.ndim}")

# ============================================================================
# 3. Size - Total number of elements
# ============================================================================
print("\n" + "=" * 70)
print("3. Total Number of Elements (size)")
print("=" * 70)

arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.arange(24).reshape(2, 3, 4)

print(f"1D array (shape {arr1d.shape}): size = {arr1d.size}")
print(f"2D array (shape {arr2d.shape}): size = {arr2d.size}")
print(f"3D array (shape {arr3d.shape}): size = {arr3d.size}")

# ============================================================================
# 4. Dtype - Data type of elements
# ============================================================================
print("\n" + "=" * 70)
print("4. Data Type (dtype)")
print("=" * 70)

int_arr = np.array([1, 2, 3])
float_arr = np.array([1.5, 2.5, 3.5])
complex_arr = np.array([1+2j, 3+4j])
bool_arr = np.array([True, False, True])
string_arr = np.array(['a', 'b', 'c'])

print(f"Integer array dtype: {int_arr.dtype}")
print(f"Float array dtype: {float_arr.dtype}")
print(f"Complex array dtype: {complex_arr.dtype}")
print(f"Boolean array dtype: {bool_arr.dtype}")
print(f"String array dtype: {string_arr.dtype}")

# Specify dtype explicitly
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
arr_float32 = np.array([1.5, 2.5, 3.5], dtype=np.float32)
arr_complex64 = np.array([1+2j, 3+4j], dtype=np.complex64)

print(f"\nExplicit dtypes:")
print(f"int32: {arr_int32.dtype}")
print(f"float32: {arr_float32.dtype}")
print(f"complex64: {arr_complex64.dtype}")

# ============================================================================
# 5. Itemsize - Size in bytes of each element
# ============================================================================
print("\n" + "=" * 70)
print("5. Item Size (itemsize)")
print("=" * 70)

arr_int32 = np.array([1, 2, 3], dtype=np.int32)
arr_int64 = np.array([1, 2, 3], dtype=np.int64)
arr_float32 = np.array([1.5, 2.5], dtype=np.float32)
arr_float64 = np.array([1.5, 2.5], dtype=np.float64)

print(f"int32 itemsize: {arr_int32.itemsize} bytes")
print(f"int64 itemsize: {arr_int64.itemsize} bytes")
print(f"float32 itemsize: {arr_float32.itemsize} bytes")
print(f"float64 itemsize: {arr_float64.itemsize} bytes")

# ============================================================================
# 6. Nbytes - Total size in bytes
# ============================================================================
print("\n" + "=" * 70)
print("6. Total Bytes (nbytes)")
print("=" * 70)

arr_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
arr_float64 = np.array([1.5, 2.5, 3.5, 4.5], dtype=np.float64)

print(f"int32 array (5 elements): nbytes = {arr_int32.nbytes} (5 * 4)")
print(f"float64 array (4 elements): nbytes = {arr_float64.nbytes} (4 * 8)")

# ============================================================================
# 7. Strides - Bytes to step in each dimension
# ============================================================================
print("\n" + "=" * 70)
print("7. Strides")
print("=" * 70)

arr_1d = np.arange(5)
arr_2d = np.arange(12).reshape(3, 4)
arr_3d = np.arange(24).reshape(2, 3, 4)

print(f"1D array strides: {arr_1d.strides}")
print(f"2D array strides: {arr_2d.strides}")
print(f"3D array strides: {arr_3d.strides}")

# ============================================================================
# 8. Base - Original array if view
# ============================================================================
print("\n" + "=" * 70)
print("8. Base (view vs copy)")
print("=" * 70)

original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
copy = original[1:4].copy()

print(f"Original array: {original}")
print(f"View of array: {view}")
print(f"View base points to original: {view.base is original}")
print(f"Copy of array: {copy}")
print(f"Copy base is None: {copy.base is None}")

# ============================================================================
# 9. T - Transpose attribute
# ============================================================================
print("\n" + "=" * 70)
print("9. Transpose (T)")
print("=" * 70)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original 2D array:\n{arr_2d}")
print(f"Shape: {arr_2d.shape}")
print(f"\nTransposed array:\n{arr_2d.T}")
print(f"Shape: {arr_2d.T.shape}")

# ============================================================================
# 10. Real and Imag - Complex number parts
# ============================================================================
print("\n" + "=" * 70)
print("10. Real and Imaginary Parts (Complex)")
print("=" * 70)

complex_arr = np.array([1+2j, 3+4j, 5+6j])
print(f"Complex array: {complex_arr}")
print(f"Real parts: {complex_arr.real}")
print(f"Imaginary parts: {complex_arr.imag}")

# ============================================================================
# 11. Flat - Flattened iterator
# ============================================================================
print("\n" + "=" * 70)
print("11. Flat Iterator")
print("=" * 70)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array:\n{arr_2d}")
print(f"Flattened (using flat): {list(arr_2d.flat)}")

# ============================================================================
# 12. Flags - Array flags and properties
# ============================================================================
print("\n" + "=" * 70)
print("12. Array Flags")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"\nFlags:")
print(f"C_CONTIGUOUS: {arr.flags['C_CONTIGUOUS']}")
print(f"F_CONTIGUOUS: {arr.flags['F_CONTIGUOUS']}")
print(f"OWNDATA: {arr.flags['OWNDATA']}")
print(f"WRITEABLE: {arr.flags['WRITEABLE']}")

# ============================================================================
# 13. Contiguity - Memory layout
# ============================================================================
print("\n" + "=" * 70)
print("13. Memory Contiguity")
print("=" * 70)

arr_c = np.array([[1, 2, 3], [4, 5, 6]], order='C')
arr_f = np.array([[1, 2, 3], [4, 5, 6]], order='F')

print(f"C-contiguous array (row-major):")
print(f"  Array:\n{arr_c}")
print(f"  Strides: {arr_c.strides}")

print(f"\nF-contiguous array (column-major):")
print(f"  Array:\n{arr_f}")
print(f"  Strides: {arr_f.strides}")

# ============================================================================
# 14. Summary function - Array information
# ============================================================================
print("\n" + "=" * 70)
print("14. Array Summary")
print("=" * 70)

arr = np.arange(20).reshape(4, 5).astype(float)
print(f"Array:\n{arr}\n")
print(f"Shape:       {arr.shape}")
print(f"Ndim:        {arr.ndim}")
print(f"Dtype:       {arr.dtype}")
print(f"Size:        {arr.size}")
print(f"Itemsize:    {arr.itemsize} bytes")
print(f"Nbytes:      {arr.nbytes} bytes")
print(f"Strides:     {arr.strides}")

# ============================================================================
# 15. Accessing multiple attributes at once
# ============================================================================
print("\n" + "=" * 70)
print("15. Accessing Multiple Attributes")
print("=" * 70)

arr = np.arange(10)
attributes = {
    'shape': arr.shape,
    'ndim': arr.ndim,
    'dtype': arr.dtype,
    'size': arr.size,
    'nbytes': arr.nbytes
}

for attr, value in attributes.items():
    print(f"{attr:10}: {value}")
