## Binary Exponentiation (Exponentiation by Squaring): Detailed Explanation and Python Implementation

### **Definition**

**Binary Exponentiation** is an efficient algorithm to compute \( a^n \) (where \( a \) is the base and \( n \) is the exponent) using only \( O(\log n) \) multiplications, as opposed to the naive \( O(n) \) approach. The method leverages the binary representation of the exponent and the associativity of multiplication (i.e., \( (X \cdot Y) \cdot Z = X \cdot (Y \cdot Z) \)) to minimize the number of operations.

---

### **Algorithmic Idea**

- **Naive Method:** Multiply \( a \) by itself \( n \) times.
- **Binary Exponentiation:**
  - Express \( n \) in binary.
  - Use the properties:
    - \( a^{b+c} = a^b \cdot a^c \)
    - \( a^{2b} = (a^b)^2 \)
  - For each bit in the binary representation of \( n \), precompute powers of \( a \) for powers of two (\( a^1, a^2, a^4, a^8, \ldots \)), and multiply those corresponding to '1' bits.

#### **Example: Compute \( 3^{13} \)**
- \( 13 = 1101_2 \) (binary)
- \( 3^{13} = 3^8 \cdot 3^4 \cdot 3^1 \)
- Precompute:
  - \( 3^1 = 3 \)
  - \( 3^2 = 9 \)
  - \( 3^4 = 81 \)
  - \( 3^8 = 6561 \)
- Multiply the selected powers: \( 3^{13} = 6561 \cdot 81 \cdot 3 = 1594323 \)

---

### **Recursive Formulation**

\[
a^n = 
\begin{cases}
1 & \text{if } n = 0 \\
(a^{n/2})^2 & \text{if } n > 0 \text{ and } n \text{ is even} \\
(a^{(n-1)/2})^2 \cdot a & \text{if } n > 0 \text{ and } n \text{ is odd}
\end{cases}
\]

---

### **Iterative Python Implementation**

```python
def binpow(a, n):
    """
    Calculates a^n using binary exponentiation (iterative approach).

    Args:
        a (int or float): The base.
        n (int): The exponent (non-negative integer).

    Returns:
        int or float: The result of a raised to the power of n.
    """
    result = 1
    while n > 0:
        if n & 1:
            result *= a
        a *= a
        n >>= 1  # Shift n right by 1 bit (n //= 2)
    return result

# Example usage:
print(f"3^13 = {binpow(3, 13)}")  # Output: 1594323
print(f"2^10 = {binpow(2, 10)}")  # Output: 1024
print(f"5^0 = {binpow(5, 0)}")    # Output: 1
