import csv

TRANSACTION_HEADERS_BIQ = [
    "Proc_ID"
]

def save_transactions_to_csv_biqAPI(transactions, filename="transactions_BIQ.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(TRANSACTION_HEADERS_BIQ)
        
        for transaction in transactions:
            transaction_data = [
                transaction.findtext(f'{{https://connect.synapsegateway.net/}}{header}', default='') 
                for header in TRANSACTION_HEADERS_BIQ
            ]
            writer.writerow(transaction_data)

    print(f"Data saved to {filename}")
