"""
NumPy frombuffer()
frombuffer() creates an array from binary data (bytes-like object)
Useful for reading binary files and interpreting raw data
"""

import numpy as np

# Example 1: Create array from bytes object
bytes_data = b'\x01\x02\x03\x04\x05'
arr1 = np.frombuffer(bytes_data, dtype=np.uint8)
print("Array from bytes (uint8):")
print(arr1)

# Example 2: Interpret bytes as 16-bit integers
bytes_int = b'\x01\x00\x02\x00\x03\x00\x04\x00'
arr2 = np.frombuffer(bytes_int, dtype=np.int16)
print("\nBytes as 16-bit integers:")
print(arr2)

# Example 3: Interpret bytes as 32-bit floats
bytes_float = b'\x00\x00\x00\x3f\x00\x00\x00\x40'  # 0.5 and 2.0
arr3 = np.frombuffer(bytes_float, dtype=np.float32)
print("\nBytes as 32-bit floats:")
print(arr3)

# Example 4: Read binary data from file (simulated)
import io
binary_stream = io.BytesIO(b'\x0a\x0b\x0c\x0d')
arr4 = np.frombuffer(binary_stream.read(), dtype=np.uint8)
print("\nData from binary stream:")
print(arr4)

# Example 5: Using memoryview
data = bytearray([10, 20, 30, 40, 50])
mv = memoryview(data)
arr5 = np.frombuffer(mv, dtype=np.uint8)
print("\nArray from memoryview:")
print(arr5)

# Example 6: frombuffer() with offset and count
bytes_with_offset = b'\x00\x00\x01\x00\x02\x00\x03\x00'
arr6 = np.frombuffer(bytes_with_offset, dtype=np.int16, offset=2, count=3)
print("\nArray with offset=2, count=3:")
print(arr6)

# Example 7: Converting structured data
struct_bytes = b'AB'  # ASCII 65, 66
arr7 = np.frombuffer(struct_bytes, dtype=np.uint8)
print("\nASCII bytes as integers:")
print(arr7, "->", chr(arr7[0]) + chr(arr7[1]))

# Example 8: Large binary data handling
large_binary = b'\xff' * 1000
arr8 = np.frombuffer(large_binary, dtype=np.uint8)
print(f"\nLarge array shape: {arr8.shape}, first 5: {arr8[:5]}")
