import hmac
import hashlib
import requests
import time

# Replace with your actual API key and secret
API_KEY = "3J1lRzlqSVbOphcF1B9YhWtbbQTYwTUJuVKVErreStAnSpl8RIOqZytwyMmSBMD6G03hSR3t3biG8QHRbAQ"
API_SECRET = "BHmOrXrhDXKADMyY6L0b9drtuHxJ9KcTvj5HkA53h6IJwIR3jl9GAhXXd5HzkBFpgy5EXK8wHK8t23qLw"
# Base URL for BingX API
BASE_URL = 'https://api.bingx.com'

# Function to create a signature
def create_signature(secret, message):
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

# Function to get server time
def get_server_time():
    endpoint = '/api/v1/time'
    response = requests.get(BASE_URL + endpoint)
    return response.json()['serverTime']

# Function to get account information
def get_account_info():
    endpoint = '/api/v1/account'
    timestamp = str(get_server_time())
    query_string = f'timestamp={timestamp}'
    signature = create_signature(API_SECRET, query_string)
    headers = {
        'X-MBX-APIKEY': API_KEY
    }
    url = f'{BASE_URL}{endpoint}?{query_string}&signature={signature}'
    response = requests.get(url, headers=headers)
    return response.json()

# Main program
if __name__ == '__main__':
    account_info = get_account_info()
    print('Account Information:', account_info)