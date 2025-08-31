# main.py — The master script to run all steps

# Import functions from other scripts
from load_data import load_datasets
from explore_data import explore_data
from preprocess_data import preprocess_data
from visualize_data import visualize_data

def main():
    print("Starting Financial Transactions Analysis Project...\n")
    
    # Load datasets
    data = load_datasets()
    print("\nData loaded successfully!\n")
    
    # Explore the data
    explore_data(data)
    print("\nData exploration complete!\n")
    
    # Preprocess the data
    cleaned_data = preprocess_data(data)
    print("\nData preprocessing complete!\n")
    
    # Visualize insights
    visualize_data(cleaned_data)
    print("\nData visualization complete!\n")
    
    print("\n🎉 Project completed successfully!")

if __name__ == "__main__":
    main()
