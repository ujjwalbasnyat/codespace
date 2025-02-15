import requests
url=" https://api.coincap.io/v2/assets/bitcoin"
response = requests.get(url)
data = response.json()

bitcoin_data = data['data']
print(bitcoin_data['supply'])