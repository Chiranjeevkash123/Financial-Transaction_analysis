import pandas as pd

def load_datasets():
    transactions_df = pd.read_csv(r'C:\Users\chira\OneDrive\Desktop\New folder (3)\Financial_Transactions_Analysis\scripts\data\transactions_data.csv')

    cards_df = pd.read_csv(r'C:\Users\chira\OneDrive\Desktop\New folder (3)\Financial_Transactions_Analysis\scripts\data\cards.csv')
    customers_df = pd.read_csv(r'C:\Users\chira\OneDrive\Desktop\New folder (3)\Financial_Transactions_Analysis\scripts\data\customers.csv')
    # mcc_codes_df = pd.read_json(r'C:\Users\chira\OneDrive\Desktop\New folder (3)\Financial_Transactions_Analysis\scripts\data\mcc_codes.json')
    # fraud_labels_df = pd.read_json(r'C:\Users\chira\OneDrive\Desktop\New folder (3)\Financial_Transactions_Analysis\scripts\data\train_fraud_labels.json')


    return {
        "transactions": transactions_df,
        "cards": cards_df,
        "customers": customers_df,
        # "mcc_codes": mcc_codes_df,
        # "fraud_labels": fraud_labels_df
    }
