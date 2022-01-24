import requests

# url = "https://pokeapi.co/api/v2/pokemon?offset=1100limit=100"
#
# response = requests.get(url)
#
# data = response.json()



# limit = 100
# pokemon = []
#
# for page_num in range(12):
#     print ('_____')
#     offset = page_num * limit
#     # print("offset is ", offset)
#     # print('limit is ', limit)
#     url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}"
#     print('requesting', url)
#     response = requests.get(url)
#     data = response.json()
#     pokemon.extend(data['results'])
#
# print(len(pokemon))

# --------------------------------------------------------------------------

url = "https://pokeapi.co/api/v2/pokemon?limit=100"
pokemon = []
while url:
    print('------')
    print('requesting', url)
    response = requests.get(url)
    data = response.json()
    url = data['next']
    pokemon.extend(data['results'])

print(len(pokemon))
