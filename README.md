# NumPy Learning Repository

A comprehensive guide to learning NumPy with detailed examples and sample code for every function and concept.

## 📚 Contents

This repository contains 8 Python files covering different aspects of NumPy:

### 1. **01_Array_Creation.py** - Creating Arrays
Learn multiple ways to create NumPy arrays:
- Creating arrays from lists (1D, 2D, 3D)
- `arange()` - Create arrays with regular intervals
- `linspace()` - Evenly spaced numbers
- `logspace()` - Logarithmically spaced numbers
- `zeros()` - Arrays filled with zeros
- `ones()` - Arrays filled with ones
- `full()` - Arrays filled with specific values
- `eye()` / `identity()` - Identity matrices
- `diag()` - Diagonal arrays
- Random arrays (random, randint, randn)
- `tile()` and `repeat()` - Array repetition
- `reshape()` and `concatenate()` - Array manipulation
- `asarray()` and `fromiter()` - Convert data to arrays
- Different data types (int32, float64, complex, bool)

**Total Functions/Concepts:** 20+

---

### 2. **02_Array_Attributes.py** - Understanding Array Properties
Explore the properties and characteristics of arrays:
- `shape` - Array dimensions
- `ndim` - Number of dimensions
- `size` - Total number of elements
- `dtype` - Data type of elements
- `itemsize` - Bytes per element
- `nbytes` - Total bytes of array
- `strides` - Byte steps in each dimension
- `base` - Original array (if view)
- `T` - Transpose property
- `real` and `imag` - Complex number parts
- `flat` - Flattened iterator
- `flags` - Array flags and properties
- Memory contiguity (C-contiguous, F-contiguous)
- Array summary and attributes

**Total Attributes:** 14+

---

### 3. **03_Indexing.py** - Accessing Array Elements
Master array indexing techniques:
- 1D array indexing (positive and negative indices)
- 2D array indexing (rows and columns)
- 3D array indexing
- Boolean indexing (conditional access)
- Fancy indexing (integer array indexing)
- `where()` - Conditional indexing
- `nonzero()` - Find non-zero elements
- `argmax()` and `argmin()` - Find index of max/min
- `searchsorted()` - Find insertion point
- Modifying elements by indexing
- Modifying 2D arrays

**Total Functions/Concepts:** 15+

---

### 4. **04_Slicing.py** - Selecting Array Subsets
Learn array slicing operations:
- 1D array slicing (start:stop:step)
- 2D array slicing (rows and columns)
- 3D array slicing
- Slicing with steps and strides
- Slicing and modifying arrays
- Copy vs View in slicing
- Ellipsis (`...`) in slicing
- `np.newaxis` - Add new dimensions
- Advanced slicing with conditions
- Extracting submatrices
- Strided slicing patterns
- Negative indices in slicing
- Combining slicing operations

**Total Concepts:** 13+

---

### 5. **05_Array_Operations.py** - Element-wise Operations
Perform mathematical operations on arrays:
- Basic arithmetic operations (+, -, *, /, //, %, **)
- Arithmetic with scalars
- Unary operations (negation, abs, sqrt)
- Comparison operations (==, !=, <, >, <=, >=)
- Logical operations (AND, OR, NOT)
- Sum, mean, median, std, var (statistical functions)
- Operations along axes (axis-specific calculations)
- Cumulative operations (cumsum, cumprod)
- Sorting arrays and finding sort indices
- `unique()` - Find unique elements with counts
- `clip()` - Limit values to range
- Rounding operations (round, floor, ceil, trunc)
- Trigonometric functions (sin, cos, tan, arcsin, etc.)
- Exponential and logarithm functions
- `sign()` function
- `dot()` - Dot product
- Element-wise operations (ufuncs)
- `where()` - Conditional selection
- `any()` and `all()` - Boolean checks
- In-place operations

**Total Functions/Concepts:** 20+

---

### 6. **06_Broadcasting.py** - Operating on Different Shapes
Master NumPy broadcasting rules:
- Broadcasting scalar with array
- Broadcasting 1D and 2D arrays
- Broadcasting column and row vectors
- Broadcasting with different dimensions
- Broadcasting 3D and 1D arrays
- Using `np.newaxis` for explicit control
- Outer product using broadcasting
- Common broadcasting operations
- Row and column standardization
- Broadcasting rules summary
- Invalid broadcasting examples
- Using `keepdims` for broadcasting
- Broadcasting in matrix operations
- Broadcasting efficiency
- Broadcasting with reshape

**Total Concepts:** 15+

---

### 7. **07_Reshape_Flatten.py** - Changing Array Shapes
Transform array structures:
- `reshape()` - Change array dimensions
- Reshape with -1 (automatic dimension)
- `flatten()` - Convert to 1D (creates copy)
- `ravel()` - Flatten with order options (creates view)
- Flatten vs Reshape - Copy vs View
- Transpose (`.T` and `transpose()`)
- Transpose 3D arrays
- `swapaxes()` - Swap specific axes
- `moveaxis()` - Move axis to new position
- `expand_dims()` - Add new axis
- `squeeze()` - Remove axes of length 1
- `stack()` - Join arrays along new axis
- `concatenate()` - Join arrays
- `tile()` and `repeat()` - Array repetition

**Total Functions/Concepts:** 14+

---

### 8. **08_Mathematical_Functions.py** - Mathematical Operations
Comprehensive mathematical operations:
- Basic math functions (sqrt, cbrt, power)
- Exponential functions (exp, expm1, exp2)
- Logarithmic functions (log, log1p, log10, log2)
- Trigonometric functions (sin, cos, tan)
- Inverse trigonometric functions (arcsin, arccos, arctan)
- Hyperbolic functions (sinh, cosh, tanh)
- Degree/radian conversion
- Rounding functions (round, floor, ceil, trunc)
- `sign()` function
- Maximum/minimum operations
- Sum and product operations
- Statistical functions (mean, median, std, var, percentile)
- `gradient()` - Numerical differentiation
- `diff()` - Element differences
- `convolve()` - Convolution
- `interp()` - Linear interpolation
- `polyfit()` - Polynomial fitting
- `polyval()` - Evaluate polynomial
- `roots()` - Find polynomial roots
- Complex number functions (real, imag, abs, angle, conj)

**Total Functions/Concepts:** 20+

---

## 🚀 Quick Start

### Installation
```bash
pip install numpy
```

### Running Examples
```bash
python 01_Array_Creation.py
python 02_Array_Attributes.py
python 03_Indexing.py
python 04_Slicing.py
python 05_Array_Operations.py
python 06_Broadcasting.py
python 07_Reshape_Flatten.py
python 08_Mathematical_Functions.py
```

---

## 📊 Learning Path

**Beginner:**
1. Start with `01_Array_Creation.py` to understand how to create arrays
2. Learn array properties in `02_Array_Attributes.py`
3. Practice indexing in `03_Indexing.py`
4. Master slicing in `04_Slicing.py`

**Intermediate:**
5. Perform operations in `05_Array_Operations.py`
6. Understand broadcasting in `06_Broadcasting.py`
7. Transform arrays in `07_Reshape_Flatten.py`

**Advanced:**
8. Apply mathematical functions in `08_Mathematical_Functions.py`

---

## 📋 Interview Questions

See **Interview_Questions.md** for commonly asked NumPy interview questions with detailed answers.

---

## 🎯 Key Concepts Covered

### Arrays
- 1D, 2D, 3D arrays and beyond
- Array creation and initialization
- Array properties (shape, dtype, size, etc.)

### Indexing & Slicing
- Positive and negative indexing
- Boolean indexing
- Fancy indexing
- Slicing with steps

### Operations
- Element-wise arithmetic
- Axis-specific operations
- Universal functions (ufuncs)
- In-place operations

### Transformations
- Reshape and flatten
- Transpose and axis manipulation
- Stack and concatenate
- Broadcasting rules

### Advanced Topics
- Polynomial operations
- Interpolation
- Numerical differentiation
- Complex numbers

---

## 💡 Tips & Tricks

### 1. Use -1 in reshape
```python
arr = np.arange(12)
# Let NumPy calculate one dimension
arr.reshape(-1, 4)  # Shape becomes (3, 4)
```

### 2. Broadcasting saves memory
```python
# No copy created, computed on-the-fly
result = large_array + small_array
```

### 3. View vs Copy
```python
view = arr[2:5]      # Creates a view
copy = arr[2:5].copy()  # Creates a copy
```

### 4. Axis parameter
```python
arr.sum(axis=0)  # Sum along columns (first axis)
arr.sum(axis=1)  # Sum along rows (second axis)
```

### 5. keepdims for broadcasting
```python
mean = arr.mean(axis=0, keepdims=True)
centered = arr - mean  # Broadcasts correctly
```

---

## 📚 Additional Resources

- [Official NumPy Documentation](https://numpy.org/doc/)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)

---

## 📝 Notes

Each Python file includes:
- Detailed comments explaining each function
- Print statements showing before/after results
- Multiple examples for each concept
- Real-world use cases
- Common mistakes to avoid

Run each file individually to see the output and learn interactively!

---

## 🤝 Contributing

Feel free to fork this repository and add more examples or explanations!

---

## 📄 License

This repository is free to use for educational purposes.

---

## ⭐ Star & Follow

If you find this repository helpful, please star it! Happy Learning! 🎉
