import matplotlib.pyplot as plt
import pandas as pd
import os

# Create the 'visuals' directory if it doesn't exist
if not os.path.exists('visuals'):
    os.makedirs('visuals')
    
def visualize_data(data):
    # Check if 'transactions' key exists and is a DataFrame-like structure
    if 'transactions' not in data or not isinstance(data['transactions'], pd.DataFrame):
        print("Error: 'transactions' key not found or not a DataFrame.")
        return

    transactions_df = data['transactions']

    # Check if 'amount' column exists
    if 'amount' not in transactions_df.columns:
        print("Error: 'amount' column not found in transactions data.")
        return

    # Clean and convert 'amount' to numeric
    amounts = pd.to_numeric(transactions_df['amount'].replace({'\$': '', ',': ''}, regex=True), errors='coerce').dropna()

    if amounts.empty:
        print("No valid transaction amounts to visualize.")
        return

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(amounts, bins=30, color='blue', edgecolor='black')
    plt.xlabel('Transaction Amount')
    plt.ylabel('Frequency')
    plt.title('Transaction Amount Distribution')
    
    # Save the plot
    plt.savefig('visuals/transactions_hist.png')
    plt.show()

    print("Visualization saved to ../visuals/transactions_hist.png")

# import os
# import matplotlib.pyplot as plt

# def visualize_data(cleaned_data):
#     # Create the 'visuals' directory if it doesn't exist
#     os.makedirs('visuals', exist_ok=True)

#     # Your visualization code here
#     plt.figure(figsize=(10, 6))
#     plt.hist(cleaned_data['amount'], bins=50)
#     plt.title('Transaction Amount Distribution')
#     plt.xlabel('Amount')
#     plt.ylabel('Frequency')
    
#     # Save the figure
#     plt.savefig('visuals/transactions_hist.png')
#     plt.close()
