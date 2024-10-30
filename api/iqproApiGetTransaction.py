import requests
import config as config
def fetch_data_iqproApiGetTransaction(transaction_id):
    headers = {
        "Authorization": f"Bearer {config.BEARER}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(f"{config.IQPRO_GET_TRANSACTIONS}/{transaction_id}", headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        
        # print(f"API 3 response for transactionId {transaction_id}: {response_data}")
        
        data = response_data.get("data", {})
        source_properties = data.get("sourceProperties", {})
        source_transaction_id = source_properties.get("sourceTransactionId")
        
        if source_transaction_id is None:
            print(f"Warning: sourceTransactionId not found for transactionId {transaction_id}")
        
        return source_transaction_id
    else:
        print(f"Failed to fetch data for transactionId {transaction_id}: {response.status_code}")
        return None
