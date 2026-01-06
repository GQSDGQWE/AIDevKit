# PLAN:
# 1. Extend basic operations with scientific functions
# 2. Add power, square root, logarithm
# 3. Maintain <200 lines limit
# 4. Include comprehensive tests

# EXECUTE:

import math
import sys
import os
from typing import Union

# Simple implementation of basic operations (v2.0 is standalone)
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> Union[float, str]:
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base: float, exponent: float) -> float:
    """
    Calculate base raised to exponent.
    
    Args:
        base: Base number
        exponent: Exponent
        
    Returns:
        base ** exponent
        
    Example:
        >>> power(2, 3)
        8.0
    """
    return base ** exponent


def square_root(n: float) -> Union[float, str]:
    """
    Calculate square root of n.
    
    Args:
        n: Number to find square root of
        
    Returns:
        Square root or error message if negative
        
    Example:
        >>> square_root(16)
        4.0
        >>> square_root(-1)
        'Error: Cannot calculate square root of negative number'
    """
    if n < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(n)


def logarithm(n: float, base: float = math.e) -> Union[float, str]:
    """
    Calculate logarithm of n with given base.
    
    Args:
        n: Number to find logarithm of
        base: Logarithm base (default: e for natural log)
        
    Returns:
        log_base(n) or error message
        
    Example:
        >>> logarithm(8, 2)
        3.0
        >>> logarithm(0)
        'Error: Cannot calculate logarithm of non-positive number'
    """
    if n <= 0:
        return "Error: Cannot calculate logarithm of non-positive number"
    if base <= 0 or base == 1:
        return "Error: Invalid logarithm base"
    return math.log(n, base)


def modulo(a: float, b: float) -> Union[float, str]:
    """
    Calculate a modulo b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Remainder of a/b or error message
        
    Example:
        >>> modulo(10, 3)
        1.0
    """
    if b == 0:
        return "Error: Modulo by zero"
    return a % b


# Self-test examples
if __name__ == "__main__":
    import time
    
    print("=== Scientific Calculator Test v2.0 ===\n")
    
    # Test 1: Power function
    result = power(2, 3)
    print(f"Test 1 - Power: 2^3 = {result}")
    assert result == 8.0, "Power test failed"
    
    # Test 2: Square root
    result = square_root(16)
    print(f"Test 2 - Square root: √16 = {result}")
    assert result == 4.0, "Square root test failed"
    
    # Test 3: Square root of negative
    result = square_root(-1)
    print(f"Test 3 - Square root negative: √(-1) = {result}")
    assert "Error" in str(result), "Negative square root test failed"
    
    # Test 4: Logarithm base 2
    result = logarithm(8, 2)
    print(f"Test 4 - Logarithm: log₂(8) = {result}")
    assert abs(result - 3.0) < 0.0001, "Logarithm test failed"
    
    # Test 5: Natural logarithm
    result = logarithm(math.e)
    print(f"Test 5 - Natural log: ln(e) = {result}")
    assert abs(result - 1.0) < 0.0001, "Natural log test failed"
    
    # Test 6: Modulo
    result = modulo(10, 3)
    print(f"Test 6 - Modulo: 10 % 3 = {result}")
    assert result == 1.0, "Modulo test failed"
    
    # Test 7: Integration with basic operations
    print(f"\nTest 7 - Mixed operations:")
    r1 = add(power(2, 3), multiply(3, 4))
    print(f"  2^3 + 3*4 = {r1}")
    assert r1 == 20.0, "Mixed operation test failed"
    
    # Test 8: Performance
    print(f"\nTest 8 - Performance:")
    start = time.time()
    for i in range(1, 1001):
        power(i, 2)
        square_root(i)
        if i > 1:
            logarithm(i, 2)
        modulo(i, 7)
    elapsed = time.time() - start
    print(f"  1,000 scientific operations: {elapsed:.4f}s")
    
    # Test 9: Line count
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    print(f"\nTest 9 - Line count: {line_count} lines (target: <200)")
    assert line_count < 200, f"File exceeds 200 lines!"
    
    print("\n✓ All v2.0 tests passed!")
