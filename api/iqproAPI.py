import requests
from config import IQPRO_URL, BEARER

def fetch_data_iqproAPI():
    request_payload = {
        "sortColumn": "CreatedDateTime",
        "sortDirection": "ASC",
        "offset": 0,
        "limit": 100
    }
    
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(IQPRO_URL, json=request_payload, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("statusCode") == "OK":
            transactions = response_data["data"]["results"]
            print("Data fetched successfully.")
            return transactions
        else:
            print("Failed to fetch data:", response_data.get("statusCode"))
            return None
    else:
        print("Failed to fetch data:", response.status_code, response.text)
        return None
