import os
import pandas as pd

def export_to_csv(cleaned_data, output_filename='cleaned_transactions.csv'):
    # Define the path to save the CSV in the project's 'data' folder
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', output_filename)

    # Convert the cleaned data to a DataFrame and save to CSV
    if isinstance(cleaned_data, pd.DataFrame):
        cleaned_data.to_csv(output_path, index=False)
        print(f"Cleaned data exported to: {output_path}")
    else:
        print("Invalid data format. Please provide a pandas DataFrame.")

# Example usage (you can replace 'cleaned_data' with your actual DataFrame)
if __name__ == "__main__":
    # Example DataFrame for testing
    example_data = pd.DataFrame({
        'transaction_id': [1, 2, 3],
        'amount': [100, 200, 300],
        'date': ['2024-03-01', '2024-03-02', '2024-03-03']
    })
    
    export_to_csv(example_data)