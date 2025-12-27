import requests
import json

# baseURL = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo"

def get_stock_details(org):
    baseUrl = "https://www.alphavantage.co/"
    apikey = "demo"
    query = f"query?function=TIME_SERIES_MONTHLY&symbol={org}&apikey={apikey}"

    try:
        response = requests.get(url=baseUrl+query).json()
        final_data = response['Meta Data'], response['Monthly Time Series']['2025-12-26']
        return final_data
    except Exception as e:
        print("Error occurred:",e)

   

def save_to_file(data):
    try:
        with open("output.json", "w+") as f:
            json.dump(data, f, indent=4)
            print("File Updated Successfully !!")
    except Exception as e:
        print("Error occurred:", e)

    
def user_input():
        company = input("Enter company for view stock's : " )
        return company


if __name__ == "__main__":

    org = user_input()   
    data = get_stock_details(org)
    save_to_file(data)