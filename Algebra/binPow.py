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