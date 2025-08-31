def preprocess_data(data):
    # Example cleaning steps
    transactions_df = data['transactions'].dropna()
    customers_df = data['customers'].dropna()
    
    cleaned_data = {
        "transactions": transactions_df,
        "customers": customers_df
    }
    
    return cleaned_data
