import csv

def read_column_as_list(filename, column_name):
    """Reads a specific column from a CSV and returns it as a list of values for order-sensitive matching."""
    values = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = row.get(column_name)
            if value:
                values.append(value)
    return values

def compare_source_and_proc_ids():
    source_ids = read_column_as_list("source_transactions.csv", "sourceTransactionId")
    
    proc_ids = read_column_as_list("transactions_BIQ.csv", "Proc_ID")
    
    missing_in_proc = [id for id in source_ids if id not in proc_ids]
    missing_in_source = [id for id in proc_ids if id not in source_ids]

    with open("comparison_report.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Status"])
        
        for id in missing_in_proc:
            writer.writerow([id, "Missing in Proc_ID (transactions_BIQ.csv)"])
        
        for id in missing_in_source:
            writer.writerow([id, "Missing in SourceTransactionID (source_transactions.csv)"])
    
    print("Comparison complete. Report saved to comparison_report.csv.")
