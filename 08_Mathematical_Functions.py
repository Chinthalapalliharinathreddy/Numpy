"""
NumPy Mathematical Functions - Comprehensive mathematical operations
"""

import numpy as np

# ============================================================================
# 1. Basic Mathematical Functions
# ============================================================================
print("=" * 70)
print("1. Basic Mathematical Functions")
print("=" * 70)

arr = np.array([1, 4, 9, 16, 25])
print(f"Array: {arr}\n")

print(f"Square root (np.sqrt): {np.sqrt(arr)}")
print(f"Squared (arr ** 2): {arr ** 2}")
print(f"Cube root (np.cbrt): {np.cbrt(arr)}")
print(f"Absolute (np.abs([-1, -2, -3])): {np.abs(np.array([-1, -2, -3]))}")
print(f"Power (np.power(arr, 2)): {np.power(arr, 2)}")

# ============================================================================
# 2. Exponential Functions
# ============================================================================
print("\n" + "=" * 70)
print("2. Exponential Functions")
print("=" * 70)

arr = np.array([0, 1, 2, 3])
print(f"Array: {arr}\n")

print(f"e^x (np.exp): {np.exp(arr)}")
print(f"e^x - 1 (np.expm1): {np.expm1(arr)}")
print(f"2^x (np.exp2): {np.exp2(arr)}")
print(f"10^x (np.power(10, arr)): {np.power(10, arr)}")

# ============================================================================
# 3. Logarithmic Functions
# ============================================================================
print("\n" + "=" * 70)
print("3. Logarithmic Functions")
print("=" * 70)

arr = np.array([1, 10, 100, 1000])
print(f"Array: {arr}\n")

print(f"Natural log (np.log): {np.log(arr)}")
print(f"ln(x+1) (np.log1p([0, 9, 99, 999])): {np.log1p(np.array([0, 9, 99, 999]))}")
print(f"Log base 10 (np.log10): {np.log10(arr)}")
print(f"Log base 2 (np.log2): {np.log2(arr)}")

# ============================================================================
# 4. Trigonometric Functions
# ============================================================================
print("\n" + "=" * 70)
print("4. Trigonometric Functions")
print("=" * 70)

angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(f"Angles (in radians): {angles}\n")

print(f"sin: {np.sin(angles)}")
print(f"cos: {np.cos(angles)}")
print(f"tan: {np.tan(angles)}")

# ============================================================================
# 5. Inverse Trigonometric Functions
# ============================================================================
print("\n" + "=" * 70)
print("5. Inverse Trigonometric Functions")
print("=" * 70)

values = np.array([0, 0.5, 1])
print(f"Values: {values}\n")

print(f"arcsin: {np.arcsin(values)}")
print(f"arccos: {np.arccos(values)}")
print(f"arctan([0, 1, -1]): {np.arctan(np.array([0, 1, -1]))}")

# ============================================================================
# 6. Hyperbolic Functions
# ============================================================================
print("\n" + "=" * 70)
print("6. Hyperbolic Functions")
print("=" * 70)

arr = np.array([0, 1, 2])
print(f"Array: {arr}\n")

print(f"sinh: {np.sinh(arr)}")
print(f"cosh: {np.cosh(arr)}")
print(f"tanh: {np.tanh(arr)}")

# ============================================================================
# 7. Degree and Radian Conversion
# ============================================================================
print("\n" + "=" * 70)
print("7. Degree and Radian Conversion")
print("=" * 70)

degrees = np.array([0, 30, 45, 60, 90, 180])
print(f"Degrees: {degrees}\n")

radians = np.radians(degrees)
print(f"To radians: {radians}\n")

back_to_degrees = np.degrees(radians)
print(f"Back to degrees: {back_to_degrees}")

# ============================================================================
# 8. Rounding Functions
# ============================================================================
print("\n" + "=" * 70)
print("8. Rounding Functions")
print("=" * 70)

arr = np.array([1.23, 2.56, 3.89, 4.12, 5.67])
print(f"Array: {arr}\n")

print(f"np.round: {np.round(arr)}")
print(f"np.round(decimals=1): {np.round(arr, decimals=1)}")
print(f"np.floor: {np.floor(arr)}")
print(f"np.ceil: {np.ceil(arr)}")
print(f"np.trunc: {np.trunc(arr)}")

# ============================================================================
# 9. Sign Function
# ============================================================================
print("\n" + "=" * 70)
print("9. Sign Function")
print("=" * 70)

arr = np.array([-5, -2, 0, 3, 7])
print(f"Array: {arr}")
print(f"np.sign: {np.sign(arr)}")

# ============================================================================
# 10. Absolute and Maximum/Minimum
# ============================================================================
print("\n" + "=" * 70)
print("10. Absolute, Maximum, and Minimum")
print("=" * 70)

arr = np.array([-5, 3, -2, 8, -1])
print(f"Array: {arr}\n")

print(f"np.abs: {np.abs(arr)}")
print(f"np.maximum(arr, 0): {np.maximum(arr, 0)}")
print(f"np.minimum(arr, 0): {np.minimum(arr, 0)}")

# ============================================================================
# 11. Sum and Product
# ============================================================================
print("\n" + "=" * 70)
print("11. Sum and Product")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}\n")

print(f"np.sum: {np.sum(arr)}")
print(f"np.prod: {np.prod(arr)}")
print(f"np.cumsum: {np.cumsum(arr)}")
print(f"np.cumprod: {np.cumprod(arr)}")

# ============================================================================
# 12. Mean, Median, Standard Deviation, Variance
# ============================================================================
print("\n" + "=" * 70)
print("12. Statistical Functions")
print("=" * 70)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {arr}\n")

print(f"np.mean: {np.mean(arr)}")
print(f"np.median: {np.median(arr)}")
print(f"np.std (standard deviation): {np.std(arr)}")
print(f"np.var (variance): {np.var(arr)}")
print(f"np.min: {np.min(arr)}")
print(f"np.max: {np.max(arr)}")
print(f"np.percentile(50): {np.percentile(arr, 50)}")
print(f"np.percentile(25): {np.percentile(arr, 25)}")
print(f"np.percentile(75): {np.percentile(arr, 75)}")

# ============================================================================
# 13. Gradient - Numerical differentiation
# ============================================================================
print("\n" + "=" * 70)
print("13. Gradient - Numerical Differentiation")
print("=" * 70)

x = np.array([0, 1, 2, 3, 4])
y = x ** 2
print(f"x: {x}")
print(f"y = x^2: {y}\n")

gradient = np.gradient(y)
print(f"np.gradient(y): {gradient}")

# 2D gradient
z = np.array([[1, 2, 4], [5, 7, 10], [10, 14, 20]])
print(f"\n2D array:\n{z}")
gy, gx = np.gradient(z)
print(f"\nGradient along y-axis:\n{gy}")
print(f"\nGradient along x-axis:\n{gx}")

# ============================================================================
# 14. Diff - Differences between elements
# ============================================================================
print("\n" + "=" * 70)
print("14. Diff - Element Differences")
print("=" * 70)

arr = np.array([1, 2, 4, 7, 11])
print(f"Array: {arr}")
print(f"np.diff: {np.diff(arr)}\n")

# 2D diff
arr2d = np.array([[1, 3, 6], [2, 5, 9]])
print(f"2D array:\n{arr2d}")
print(f"\nDiff along axis 0:\n{np.diff(arr2d, axis=0)}")
print(f"\nDiff along axis 1:\n{np.diff(arr2d, axis=1)}")

# ============================================================================
# 15. Convolve - Convolution of two arrays
# ============================================================================
print("\n" + "=" * 70)
print("15. Convolve - Convolution")
print("=" * 70)

signal = np.array([1, 2, 3, 4, 5])
kernel = np.array([1, 1])
print(f"Signal: {signal}")
print(f"Kernel: {kernel}\n")

convolved = np.convolve(signal, kernel, mode='same')
print(f"Convolution (mode='same'): {convolved}")

# ============================================================================
# 16. Interp - Linear interpolation
# ============================================================================
print("\n" + "=" * 70)
print("16. Interp - Linear Interpolation")
print("=" * 70)

xp = np.array([1, 2, 3, 4, 5])
fp = np.array([2, 4, 6, 8, 10])
x = np.array([1.5, 2.5, 3.5, 4.5])

print(f"Known points x: {xp}")
print(f"Known values f(x): {fp}")
print(f"Interpolation points: {x}\n")

interpolated = np.interp(x, xp, fp)
print(f"Interpolated values: {interpolated}")

# ============================================================================
# 17. Polyfit - Polynomial fitting
# ============================================================================
print("\n" + "=" * 70)
print("17. Polyfit - Polynomial Fitting")
print("=" * 70)

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
print(f"x: {x}")
print(f"y: {y}\n")

# Fit a polynomial of degree 1 (linear)
coeffs = np.polyfit(x, y, 1)
print(f"Linear fit coefficients (degree 1): {coeffs}")
print(f"Equation: y = {coeffs[0]:.4f}*x + {coeffs[1]:.4f}\n")

# Quadratic fit
y_quad = x ** 2 + 2 * x + 1
coeffs_quad = np.polyfit(x, y_quad, 2)
print(f"Quadratic fit coefficients (degree 2): {coeffs_quad}")

# ============================================================================
# 18. Polyval - Evaluate polynomial
# ============================================================================
print("\n" + "=" * 70)
print("18. Polyval - Evaluate Polynomial")
print("=" * 70)

coeffs = np.array([2, 3, 1])  # 2x^2 + 3x + 1
x = np.array([0, 1, 2, 3])
print(f"Polynomial coefficients (2x^2 + 3x + 1): {coeffs}")
print(f"x values: {x}\n")

y = np.polyval(coeffs, x)
print(f"Polynomial values: {y}")

# ============================================================================
# 19. Roots - Find polynomial roots
# ============================================================================
print("\n" + "=" * 70)
print("19. Roots - Find Polynomial Roots")
print("=" * 70)

# x^2 - 5x + 6 = 0, roots are 2 and 3
coeffs = np.array([1, -5, 6])
print(f"Polynomial coefficients (x^2 - 5x + 6): {coeffs}")

roots = np.roots(coeffs)
print(f"Roots: {roots}")

# ============================================================================
# 20. Complex number functions
# ============================================================================
print("\n" + "=" * 70)
print("20. Complex Number Functions")
print("=" * 70)

c = np.array([1+2j, 3+4j, 5+6j])
print(f"Complex numbers: {c}\n")

print(f"Real part: {np.real(c)}")
print(f"Imaginary part: {np.imag(c)}")
print(f"Absolute value (magnitude): {np.abs(c)}")
print(f"Angle (phase): {np.angle(c)}")
print(f"Conjugate: {np.conj(c)}")
