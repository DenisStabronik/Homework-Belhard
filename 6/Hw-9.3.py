import json
import yaml
data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}
serialized = json.dumps(data)
print(data)
deserialized = json.loads(serialized)
print(deserialized)

with open("json.txt", "w") as f:
    json.dump(data, f)

with open("json.txt", "r") as f:
    deserialized_json = json.load(f)
print(deserialized_json)