import json
with open('data1.json','r') as file:
    data=json.load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)
