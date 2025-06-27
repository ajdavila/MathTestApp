import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import pandas as pd
import sys
from pathlib import Path

# Add the MathTestApp directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))

from main import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value='test.xlsx')
    @patch('main.ExcelReader')
    @patch('main.MathOperations')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_math_operations, mock_excel_reader, mock_input):
        # Mock ExcelReader behavior
        mock_excel_reader_instance = mock_excel_reader.return_value
        mock_excel_reader_instance.read_excel.return_value = pd.DataFrame([[10, 5], [20, 4]])

        # Mock MathOperations behavior
        mock_math_operations_instance = mock_math_operations.return_value
        mock_math_operations_instance.add.side_effect = lambda a, b: a + b
        mock_math_operations_instance.subtract.side_effect = lambda a, b: a - b
        mock_math_operations_instance.multiply.side_effect = lambda a, b: a * b
        mock_math_operations_instance.divide.side_effect = lambda a, b: a / b if b != 0 else 'undefined'
        mock_math_operations_instance.average.side_effect = lambda nums: sum(nums) / len(nums)
        mock_math_operations_instance.percentage.side_effect = lambda a, b: (a / b) * 100 if b != 0 else 'undefined'

        # Run the main function
        main()

        # Validate output
        output = mock_stdout.getvalue()
        self.assertIn("Row 1:", output)
        self.assertIn("Addition: 15", output)
        self.assertIn("Subtraction: 5", output)
        self.assertIn("Multiplication: 50", output)
        self.assertIn("Division: 2.0", output)
        self.assertIn("Average: 7.5", output)
        self.assertIn("Percentage of 10 out of 5: 200.0%", output)

        self.assertIn("Row 2:", output)
        self.assertIn("Addition: 24", output)
        self.assertIn("Subtraction: 16", output)
        self.assertIn("Multiplication: 80", output)
        self.assertIn("Division: 5.0", output)
        self.assertIn("Average: 12.0", output)
        self.assertIn("Percentage of 20 out of 4: 500.0%", output)

if __name__ == '__main__':
    unittest.main()
