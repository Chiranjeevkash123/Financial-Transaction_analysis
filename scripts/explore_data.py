def explore_data(data):
    print("🔍 Exploring Transactions Dataset:")
    print(data['transactions'].info())
    print(data['transactions'].describe())

    print("\n🔍 Exploring Customers Dataset:")
    print(data['customers'].info())
    print(data['customers'].describe())
