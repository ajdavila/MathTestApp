# main.py

import pandas as pd
from excel_reader import ExcelReader
from math_operations import MathOperations

def main():
    # Initialize the ExcelReader and MathOperations classes
    excel_reader = ExcelReader()
    math_operations = MathOperations()

    # Prompt user for the Excel file path
    file_path = input("Enter the path to your Excel file: ").strip()

    try:
        # Read data from the Excel file
        #reader = ExcelReader()
        data = excel_reader.read_excel(file_path)  # Use the user-provided file path

        # Print the raw data for debugging
        print("Raw Data:")
        print(data)

        # Convert DataFrame to a list of lists
        if isinstance(data, pd.DataFrame):
            data = data.values.tolist()

        # Validate data
        if data is not None and len(data) > 0:
            for row_index, row in enumerate(data):
                if len(row) >= 2:  # Ensure the row has at least two columns
                    a = row[0]  # First number
                    b = row[1]  # Second number

                    print(f"\nRow {row_index + 1}:")
                    print(f"Numbers: a = {a}, b = {b}")
                    print(f"Addition: {math_operations.add(a, b)}")
                    print(f"Subtraction: {math_operations.subtract(a, b)}")
                    print(f"Multiplication: {math_operations.multiply(a, b)}")
                    print(f"Division: {math_operations.divide(a, b)}")

                    # Example for average and percentage
                    numbers = [a, b]  # Example list for average
                    print(f"Average: {math_operations.average(numbers)}")
                    print(f"Percentage of {a} out of {b}: {math_operations.percentage(a, b)}%")
                else:
                    print(f"Row {row_index + 1} is invalid. Ensure it contains at least two columns.")
        else:
            print("Invalid data format in the Excel file. Ensure it contains at least two columns.")
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()