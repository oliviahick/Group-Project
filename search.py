import requests

def recipe_search(ingredient):
# Register to get an APP ID and key https://developer.edamam.com/

user = input("Who is the user? Olivia/Megan")

if user == "Megan":
    app_id = ''
    app_key = ''
elif user =="Olivia"
    app_id = 'd13f3378'
    app_key = 'c565b141f1289b921f22834414f67eb0	—'

url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key)

result = requests.get(url)

data = result.json()
return data['hits']

def run():
ingredient = input('Enter an ingredient: ')
results = recipe_search(ingredient)
for result in results:
recipe = result['recipe']
print(recipe['label'])
print(recipe['uri'])
print()

run()
