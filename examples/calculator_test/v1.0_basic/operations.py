# PLAN:
# 1. Define basic operations (+, -, *, /)
# 2. Input validation
# 3. Error handling for division by zero
# 4. Return results with proper type

# EXECUTE:

from typing import Union

def add(a: float, b: float) -> float:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
        
    Example:
        >>> add(2, 3)
        5.0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.
    
    Args:
        a: First number
        b: Second number to subtract
        
    Returns:
        Difference of a and b
        
    Example:
        >>> subtract(5, 3)
        2.0
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
        
    Example:
        >>> multiply(4, 5)
        20.0
    """
    return a * b


def divide(a: float, b: float) -> Union[float, str]:
    """
    Divide a by b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Quotient or error message if division by zero
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(10, 0)
        'Error: Division by zero'
    """
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Self-test examples
if __name__ == "__main__":
    import time
    
    print("=== Calculator Operations Test v1.0 ===\n")
    
    # Test 1: Basic addition
    result = add(10, 5)
    print(f"Test 1 - Addition: 10 + 5 = {result}")
    assert result == 15.0, "Addition test failed"
    
    # Test 2: Subtraction
    result = subtract(10, 5)
    print(f"Test 2 - Subtraction: 10 - 5 = {result}")
    assert result == 5.0, "Subtraction test failed"
    
    # Test 3: Multiplication
    result = multiply(4, 5)
    print(f"Test 3 - Multiplication: 4 * 5 = {result}")
    assert result == 20.0, "Multiplication test failed"
    
    # Test 4: Division
    result = divide(20, 4)
    print(f"Test 4 - Division: 20 / 4 = {result}")
    assert result == 5.0, "Division test failed"
    
    # Test 5: Division by zero
    result = divide(10, 0)
    print(f"Test 5 - Division by zero: 10 / 0 = {result}")
    assert result == "Error: Division by zero", "Division by zero test failed"
    
    # Test 6: Negative numbers
    result = add(-5, 3)
    print(f"Test 6 - Negative numbers: -5 + 3 = {result}")
    assert result == -2.0, "Negative number test failed"
    
    # Test 7: Decimals
    result = multiply(2.5, 4.0)
    print(f"Test 7 - Decimals: 2.5 * 4.0 = {result}")
    assert result == 10.0, "Decimal test failed"
    
    # Test 8: Performance measurement
    print(f"\nTest 8 - Performance:")
    start = time.time()
    for i in range(10000):
        add(i, i)
        subtract(i, i)
        multiply(i, i)
        divide(i, 1)
    elapsed = time.time() - start
    print(f"  10,000 operations completed in {elapsed:.4f}s")
    print(f"  Average: {elapsed/10000*1000:.6f}ms per operation")
    
    print("\n✓ All tests passed!")
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    print(f"✓ File line count: {line_count} lines (target: <200)")
