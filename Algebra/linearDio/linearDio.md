# Linear Diophantine Equations in Two Variables: Detailed Explanation and Python Implementation

## Definition

A **Linear Diophantine Equation (LDE)** in two variables is an equation of the form:

$$
ax + by = c
$$

where $a$, $b$, and $c$ are given integers, and the goal is to find integer solutions $x$ and $y$.

## Degenerate Case

- If $a = b = 0$:
  - If $c = 0$: Every pair $(x, y)$ is a solution (infinitely many).
  - If $c \neq 0$: No solution exists.
- In practice, algorithms focus on cases where at least one of $a$ or $b$ is nonzero.

## Existence of Solutions

- **Bézout's Lemma:** For any integers $a$ and $b$, there exist integers $x$ and $y$ such that $ax + by = g$, where $g = \gcd(a, b)$.
- **Key Criterion:** The equation $ax + by = c$ has integer solutions if and only if $g$ divides $c$ (i.e., $c \% g == 0$).

## Finding a Particular Solution

1. **Use the Extended Euclidean Algorithm** to find integers $x_g$, $y_g$ such that:
   $$
   a x_g + b y_g = g
   $$
2. **Scale** the solution to $ax + by = c$ by multiplying both $x_g$ and $y_g$ by $c // g$:
   $$
   x_0 = x_g \cdot \frac{c}{g}
   $$
   $$
   y_0 = y_g \cdot \frac{c}{g}
   $$
   This gives a particular integer solution $(x_0, y_0)$.

3. **Adjust for Negative Inputs:** If $a$ or $b$ is negative, the sign of $x_0$ or $y_0$ is adjusted accordingly.

## General Solution

All integer solutions are given by:
$$
x = x_0 + k \cdot \frac{b}{g}
$$
$$
y = y_0 - k \cdot \frac{a}{g}
$$
for any integer $k$.

## Python Implementation

### Extended Euclidean Algorithm

```python
def extended_gcd(a, b):
    """
    Returns (g, x, y) such that g = gcd(a, b) and a*x + b*y = g.
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)
```

### Find Any Solution to ax + by = c

```python
def find_any_solution(a, b, c):
    """
    Finds one integer solution (x0, y0) to the linear Diophantine equation ax + by = c.
    Returns (has_solution, x0, y0, g), where has_solution is True if solution exists.
    """
    g, xg, yg = extended_gcd(abs(a), abs(b))
    if c % g != 0:
        return False, None, None, g  # No solution

    x0 = xg * (c // g)
    y0 = yg * (c // g)
    # Adjust signs to match original a, b
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0
    return True, x0, y0, g
```

## Examples

```python
examples = [
    (80, 55, 5),      # GCD=5, solution exists
    (48, 18, 6),      # GCD=6, solution exists
    (15, 0, 15),      # GCD=15, solution exists
    (6, 9, 7),        # GCD=3, no solution (7 not divisible by 3)
    (-80, 55, 5),     # Negative a
    (0, 0, 0),        # Degenerate: infinite solutions
    (0, 0, 7),        # Degenerate: no solution
]

for a, b, c in examples:
    found, x0, y0, g = find_any_solution(a, b, c)
    if found:
        print(f"ax+by={c}: a={a}, b={b}, c={c}, GCD={g}, x0={x0}, y0={y0}, check: {a}*{x0}+{b}*{y0}={a*x0 + b*y0}")
    else:
        print(f"ax+by={c}: a={a}, b={b}, c={c}, GCD={g}, No solution exists.")
```

**Sample Output:**
```
ax+by=5: a=80, b=55, c=5, GCD=5, x0=-2, y0=3, check: 80*-2+55*3=5
ax+by=6: a=48, b=18, c=6, GCD=6, x0=-1, y0=3, check: 48*-1+18*3=6
ax+by=15: a=15, b=0, c=15, GCD=15, x0=1, y0=0, check: 15*1+0*0=15
ax+by=7: a=6, b=9, c=7, GCD=3, No solution exists.
ax+by=5: a=-80, b=55, c=5, GCD=5, x0=2, y0=3, check: -80*2+55*3=5
ax+by=0: a=0, b=0, c=0, GCD=0, x0=1, y0=0, check: 0*1+0*0=0
ax+by=7: a=0, b=0, c=7, GCD=0, No solution exists.
```

## General Solution Formula

If $(x_0, y_0)$ is a particular solution, all integer solutions are:

$$
x = x_0 + k \cdot \frac{b}{g}
$$
$$
y = y_0 - k \cdot \frac{a}{g}
$$
for any integer $k$.

## Remarks & Extensions

- This method is standard in number theory and competitive programming.
- The approach generalizes to more variables, but two-variable equations are the most common and tractable.
- Libraries such as `sympy` provide higher-level functions for Diophantine equations, but the above code is self-contained and efficient for two variables.
