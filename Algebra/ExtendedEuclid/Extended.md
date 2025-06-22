# Extended Euclidean Algorithm: Detailed Explanation and Python Implementation

## Definition and Purpose

The **Extended Euclidean Algorithm** is an extension of the classic Euclidean algorithm for finding the greatest common divisor (GCD) of two integers $a$ and $b$. In addition to computing $\gcd(a, b)$, it also finds integers $x$ and $y$ such that:

$$
a \cdot x + b \cdot y = \gcd(a, b)
$$

This equation is known as **Bézout's identity**. The coefficients $x$ and $y$ are called Bézout coefficients. This algorithm is fundamental in number theory, particularly for solving linear Diophantine equations and for finding modular inverses in cryptography.

## How the Algorithm Works

### Base Case

When $b = 0$, the GCD is $a$, and the coefficients are $x = 1$, $y = 0$, because:

$$
a \cdot 1 + 0 \cdot 0 = a
$$

### Recursive Step

Suppose you have already computed the GCD and coefficients for $(b, a \bmod b)$:

$$
b \cdot x_1 + (a \bmod b) \cdot y_1 = g
$$

Recall that $a \bmod b = a - \lfloor a/b \rfloor \cdot b$, so:

$$
g = b \cdot x_1 + (a - \lfloor a/b \rfloor \cdot b) \cdot y_1 = a \cdot y_1 + b \cdot (x_1 - y_1 \cdot \lfloor a/b \rfloor)
$$

Therefore, the coefficients for $(a, b)$ are:

$$
x = y_1
$$
$$
y = x_1 - y_1 \cdot \lfloor a/b \rfloor
$$

## Python Implementations

### 1. Recursive Implementation

This directly follows the recursive logic described above:

```python
def extended_gcd_recursive(a, b):
    """
    Returns a tuple (g, x, y) such that g = gcd(a, b) and a*x + b*y = g.
    """
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd_recursive(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

# Example usage:
g, x, y = extended_gcd_recursive(80, 55)
print(f"For a=80, b=55: GCD={g}, x={x}, y={y}. Check: {80*x + 55*y} = {g}")
# Output: For a=80, b=55: GCD=5, x=-2, y=3. Check: 5 = 5

g, x, y = extended_gcd_recursive(48, 18)
print(f"For a=48, b=18: GCD={g}, x={x}, y={y}. Check: {48*x + 18*y} = {g}")
# Output: For a=48, b=18: GCD=6, x=-1, y=3. Check: 6 = 6
```
This implementation is widely used and matches the mathematical derivation.

### 2. Iterative Implementation

The iterative version maintains two pairs of coefficients and updates them in parallel with the Euclidean steps:

```python
def extended_gcd_iterative(a, b):
    """
    Returns a tuple (g, x, y) such that g = gcd(a, b) and a*x + b*y = g.
    """
    x0, y0 = 1, 0  # Coefficients for 'a'
    x1, y1 = 0, 1  # Coefficients for 'b'
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Example usage:
g, x, y = extended_gcd_iterative(80, 55)
print(f"For a=80, b=55 (iterative): GCD={g}, x={x}, y={y}. Check: {80*x + 55*y} = {g}")
# Output: For a=80, b=55 (iterative): GCD=5, x=-2, y=3. Check: 5 = 5

g, x, y = extended_gcd_iterative(48, 18)
print(f"For a=48, b=18 (iterative): GCD={g}, x={x}, y={y}. Check: {48*x + 18*y} = {g}")
# Output: For a=48, b=18 (iterative): GCD=6, x=-1, y=3. Check: 6 = 6
```
This form is efficient and avoids recursion stack depth issues.

## Applications

- **Solving Linear Diophantine Equations:** Find integer solutions to $ax + by = c$ if and only if $c$ is divisible by $\gcd(a, b)$.
- **Computing Modular Inverses:** If $a$ and $m$ are coprime, the modular inverse of $a$ modulo $m$ is the $x$ coefficient in $ax + my = 1$.
- **Cryptography:** Essential for RSA and other public-key algorithms.

## Example: Modular Inverse

To compute the modular inverse of $a$ modulo $m$:

```python
def modinv(a, m):
    g, x, y = extended_gcd_iterative(a, m)
    if g != 1:
        raise ValueError("No modular inverse exists")
    else:
        return x % m

# Example usage:
print(modinv(3, 11))  # Output: 4, since 3*4 ≡ 1 mod 11
```

## Summary Table

| Method      | Returns                | Handles Negatives | Stack Safe | Use Case                |
|-------------|------------------------|-------------------|------------|-------------------------|
| Recursive   | (g, x, y)              | Yes               | No         | Simple, mathematical    |
| Iterative   | (g, x, y)              | Yes               | Yes        | Large inputs, efficiency|

## Key Takeaways

- The Extended Euclidean Algorithm computes both the GCD and Bézout coefficients efficiently.
- Both recursive and iterative forms are standard and widely used in practice.
- It is foundational for modular arithmetic, cryptography, and number theory.

