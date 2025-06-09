# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

# Input: Read the complex number
complex_number = complex(input().strip())

# Calculate modulus and argument
r = abs(complex_number)  # Modulus
theta = cmath.phase(complex_number)  # Argument

# Output: Print the results
print(f"{r:.3f}")
print(f"{theta:.3f}")
