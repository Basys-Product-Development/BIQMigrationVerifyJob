import requests
import xml.etree.ElementTree as ET
from config import BIQ_URL
from data.record_data_BIQ import save_transactions_to_csv_biqAPI 
import config as config

AUTHORIZATION = config.BIQAPIAUTHORIZATION
DEV_ACCOUNT = config.DEV_ACCOUNT
DEV_PASSWORD = config.DEV_PASSWORD
BATCH_NUMBER = int(config.BATCH_NUMBER) 

def fetch_data_biqAPI():
    batch_number = BATCH_NUMBER  
    no_transactions_found_count = 0
    all_transactions = [] 
    
    while True:
        soap_body = f"""<?xml version="1.0" encoding="UTF-8"?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:con="https://connect.synapsegateway.net/">
           <soap:Header/>
           <soap:Body>
              <con:GetTransactionsByBatch>
                 <con:Account>{DEV_ACCOUNT}</con:Account>
                 <con:Password>{DEV_PASSWORD}</con:Password>
                 <con:Batch>{batch_number}</con:Batch>
              </con:GetTransactionsByBatch>
           </soap:Body>
        </soap:Envelope>"""

        headers = {
            "Authorization": AUTHORIZATION,
            "Content-Type": "application/soap+xml; charset=utf-8",
            "Content-Length": str(len(soap_body))
        }

        try:
            response = requests.post(BIQ_URL, data=soap_body, headers=headers)

            if response.status_code == 200:
                root = ET.fromstring(response.content)

                result = root.find('.//{https://connect.synapsegateway.net/}GetTransactionsByBatchResult')

                if result is not None and not list(result):
                    print(f"No transactions found in batch {batch_number}.")
                    no_transactions_found_count += 1

                    if no_transactions_found_count >= 10:
                        print("Reached 10 consecutive empty batches. Ending loop.")
                        break
                else:
                    transactions = result.findall('.//{https://connect.synapsegateway.net/}QueryTransaction')
                    all_transactions.extend(transactions)
                    
                    print(f"Transactions found in batch {batch_number}.")
                    no_transactions_found_count = 0 

                batch_number += 1

            else:
                print(f"API Error: Status code {response.status_code}")
                break

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break

    if all_transactions:
        save_transactions_to_csv_biqAPI(all_transactions, filename="transactions_BIQ.csv")
    else:
        print("No transactions found across all batches.")
