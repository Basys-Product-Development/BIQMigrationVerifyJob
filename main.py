from api.biqAPI import fetch_data_biqAPI
from api.iqproAPI import fetch_data_iqproAPI
from data.record_data_BIQ import save_transactions_to_csv_biqAPI
from data.record_data_IQPRO import save_transactions_to_csv_IQPro
def main():
    # Process data from BIQ
    print("Fetching data from BIQ...")
    data_biq = fetch_data_biqAPI()
    if data_biq:
        print("Saving data from BIQ API to CSV...")
        save_transactions_to_csv_biqAPI(data_biq, "transactions_biq.csv")
    else:
        print("No data retrieved from BIQ API or an error occurred.")
    
    # Process data from IQPRO
    print("\nFetching data from IQPro...")
    data_iqpro = fetch_data_iqproAPI()
    if data_iqpro:
        print("Saving data from IQPro API to CSV...")
        save_transactions_to_csv_IQPro(data_iqpro, "transactions_iqpro.csv")
    else:
        print("No data retrieved from IQPro API or an error occurred.")

if __name__ == "__main__":
    main()
