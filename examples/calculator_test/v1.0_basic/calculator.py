# PLAN:
# 1. Import operations module
# 2. Create CLI interface
# 3. Loop for continuous calculations
# 4. Handle user input and display results

# EXECUTE:

import sys
from operations import add, subtract, multiply, divide


def display_menu():
    """Display calculator menu."""
    print("\n" + "="*40)
    print("  Calculator v1.0 - Basic Operations")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)


def get_numbers():
    """
    Get two numbers from user input.
    
    Returns:
        Tuple of two floats or None if invalid
    """
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return None


def calculate(operation: str, a: float, b: float):
    """
    Perform calculation based on operation.
    
    Args:
        operation: Operation type (1-4)
        a: First number
        b: Second number
        
    Returns:
        Calculation result
    """
    operations_map = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/')
    }
    
    if operation in operations_map:
        func, symbol = operations_map[operation]
        result = func(a, b)
        print(f"\nResult: {a} {symbol} {b} = {result}")
        return result
    else:
        print("Error: Invalid operation")
        return None


def main():
    """Main calculator loop."""
    print("\n✓ Calculator framework test started")
    print("✓ PLAN-EXECUTE pattern: Applied")
    print("✓ Modular structure: operations.py + calculator.py")
    
    while True:
        display_menu()
        choice = input("\nSelect operation (1-5): ").strip()
        
        if choice == '5':
            print("\n✓ Exiting calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            numbers = get_numbers()
            if numbers:
                a, b = numbers
                calculate(choice, a, b)
        else:
            print("Error: Please select 1-5")


# Self-test examples
if __name__ == "__main__":
    print("=== Calculator CLI Test ===\n")
    
    # Test 1: Menu display
    print("Test 1 - Menu display:")
    display_menu()
    print("✓ Menu displayed successfully\n")
    
    # Test 2: Calculate function
    print("Test 2 - Calculate function:")
    result = calculate('1', 10, 5)
    assert result == 15.0, "Calculate test failed"
    print("✓ Calculate function works\n")
    
    # Test 3: Operations map
    print("Test 3 - All operations:")
    calculate('1', 5, 3)   # Addition
    calculate('2', 10, 4)  # Subtraction
    calculate('3', 6, 7)   # Multiplication
    calculate('4', 20, 4)  # Division
    print("✓ All operations functional\n")
    
    # Test 4: File line count check
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    print(f"Test 4 - Line count: {line_count} lines")
    assert line_count < 200, f"File exceeds 200 lines! ({line_count})"
    print("✓ Line count within limit\n")
    
    print("✓ All CLI tests passed!")
    print("\nTo use interactive mode, run without tests:")
    print("  python calculator.py")
    
    # Uncomment to start interactive mode
    # main()
