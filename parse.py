import yaml
with open('data1.yaml', 'r') as file:
    data = yaml.safe_load(file)
user = data['user']
print(user['name'])
for role in data['user']['roles']:
    print(role)
