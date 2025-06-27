import pandas as pd  # Ensure pandas is imported

class ExcelReader:
    def read_excel(self, file_path):
        # Read the Excel file using pandas
        data = pd.read_excel(file_path)  # Correctly use pandas to read the file
        
        # Return the data as a DataFrame
        return data
