from api.biqAPI import fetch_data_biqAPI
from api.iqproAPI import fetch_data_iqproAPI
from api.iqproApiGetTransaction import fetch_data_iqproApiGetTransaction
from data.record_data_BIQ import save_transactions_to_csv_biqAPI
from data.record_data_IQPRO import save_transactions_to_csv_IQPro
from data.record_data_IQPRO_GetTransactions import save_source_transactions_to_csv
from data.read_data_IQPRO import read_transaction_ids_from_csv
from comparison.compare_data import compare_source_and_proc_ids

def main():
    
    ###############################################
    # print("Fetching data from biq api...")
    # data_biq api = fetch_data_biqAPI()
    # if data_biq api:
    #     print("Saving data from biq api to transactions_BIQ.csv...")
    #     save_transactions_to_csv_biqAPI(data_biq api, filename="transactions_BIQ.csv")
    # else:
    #     print("No data retrieved from biq api or an error occurred.")
    ################################################
    
    print("\nFetching data from iqpro api...")
    data_iqproApi = fetch_data_iqproAPI()
    if data_iqproApi:
        print("Saving data from iqpro api to transactions_iqpro.csv...")
        save_transactions_to_csv_IQPro(data_iqproApi, filename="transactions_iqpro.csv")
    else:
        print("No data retrieved from iqpro api or an error occurred.")
        return  

    print("\nReading transaction IDs from transactions_iqpro.csv...")
    transaction_ids = read_transaction_ids_from_csv("transactions_iqpro.csv")
    if not transaction_ids:
        print("No transaction IDs found in transactions_iqpro.csv.")
        return

    print("\nFetching sourceTransactionIds from iqpro getTransaction...")
    transactions_with_source_ids = []
    for transaction_id in transaction_ids:
        source_transaction_id = fetch_data_iqproApiGetTransaction(transaction_id)
        transactions_with_source_ids.append({
            "transactionId": transaction_id,
            "sourceTransactionId": source_transaction_id
        })

    print("Saving sourceTransactionIds to source_transactions.csv...")
    save_source_transactions_to_csv(transactions_with_source_ids, filename="source_transactions.csv")

if __name__ == "__main__":
    main()
    compare_source_and_proc_ids()