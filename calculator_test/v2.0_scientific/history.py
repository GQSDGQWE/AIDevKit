# PLAN:
# 1. Store calculation history
# 2. Display history
# 3. Clear history function
# 4. Export history to file

# EXECUTE:

from datetime import datetime
from typing import List, Dict
import json


class CalculationHistory:
    """Manage calculation history."""
    
    def __init__(self):
        self.history: List[Dict] = []
    
    def add(self, operation: str, operands: List[float], result: float):
        """
        Add calculation to history.
        
        Args:
            operation: Operation name
            operands: List of operands
            result: Calculation result
        """
        entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'operands': operands,
            'result': result
        }
        self.history.append(entry)
    
    def display(self, count: int = None):
        """
        Display calculation history.
        
        Args:
            count: Number of recent entries to show (None for all)
        """
        if not self.history:
            print("No calculation history")
            return
        
        entries = self.history[-count:] if count else self.history
        print(f"\n{'='*60}")
        print(f"  Calculation History (Last {len(entries)} entries)")
        print(f"{'='*60}")
        
        for i, entry in enumerate(entries, 1):
            time = entry['timestamp'].split('T')[1][:8]
            ops = ', '.join(str(x) for x in entry['operands'])
            print(f"{i}. [{time}] {entry['operation']}({ops}) = {entry['result']}")
        
        print(f"{'='*60}\n")
    
    def clear(self):
        """Clear all history."""
        self.history.clear()
        print("✓ History cleared")
    
    def export(self, filename: str = "calculator_history.json"):
        """
        Export history to JSON file.
        
        Args:
            filename: Output filename
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2)
        print(f"✓ History exported to {filename}")
    
    def __len__(self):
        return len(self.history)


# Self-test examples
if __name__ == "__main__":
    print("=== History Manager Test ===\n")
    
    # Test 1: Create history
    hist = CalculationHistory()
    print(f"Test 1 - Created history: {len(hist)} entries")
    
    # Test 2: Add entries
    hist.add("add", [10, 5], 15)
    hist.add("multiply", [4, 7], 28)
    hist.add("power", [2, 8], 256)
    print(f"Test 2 - Added 3 entries: {len(hist)} total")
    assert len(hist) == 3, "Add entries test failed"
    
    # Test 3: Display history
    print(f"\nTest 3 - Display all:")
    hist.display()
    
    # Test 4: Display last 2
    print(f"Test 4 - Display last 2:")
    hist.display(2)
    
    # Test 5: Export
    print(f"Test 5 - Export:")
    hist.export("test_history.json")
    
    # Test 6: Clear
    print(f"\nTest 6 - Clear:")
    hist.clear()
    assert len(hist) == 0, "Clear test failed"
    
    # Test 7: Line count
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    print(f"\nTest 7 - Line count: {line_count} lines (target: <200)")
    assert line_count < 200, "Line count exceeded!"
    
    print("\n✓ All history tests passed!")
