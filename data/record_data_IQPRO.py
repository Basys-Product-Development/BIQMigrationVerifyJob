import csv

TRANSACTION_HEADERS_IQPro = [
    "transactionId", "type", "amount", "maskedCard",
    "billingFirstName", "billingLastName"
]

def save_transactions_to_csv_IQPro(transactions, filename="transactions_IQPro.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(TRANSACTION_HEADERS_IQPro)
        
        for transaction in transactions:
            row = [transaction.get(header, '') for header in TRANSACTION_HEADERS_IQPro]
            writer.writerow(row)

    print(f"Data saved to {filename}")
