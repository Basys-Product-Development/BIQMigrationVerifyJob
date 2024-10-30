import csv

def read_transaction_ids_from_csv(filename="transactions_iqpro.csv"):
    transaction_ids = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transaction_id = row.get("transactionId")
            if transaction_id:
                transaction_ids.append(transaction_id)
    return transaction_ids
