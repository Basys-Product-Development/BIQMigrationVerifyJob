import csv

TRANSACTION_HEADERS = ["transactionId", "sourceTransactionId"]

def save_source_transactions_to_csv(transactions, filename="source_transactions.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=TRANSACTION_HEADERS)
        writer.writeheader()
        
        for transaction in transactions:
            writer.writerow(transaction)

    print(f"Data saved to {filename}")
