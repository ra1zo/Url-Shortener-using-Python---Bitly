import bitly_api

ACCESS_TOKEN = "Enter_Your_Tokens"

x = bitly_api.Connection(access_token=ACCESS_TOKEN)

url_input = input("Enter The URL:  ")

response = x.shorten(url_input)

print(response)
