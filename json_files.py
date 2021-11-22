import json
import pprint

user_info = {
    "first_name": "Willie",
    "last_name": "Watkins",
    "email": "willie.watkins@example.com",
    "age": 23,
    "last_6_months_income": [12000, 12000, 11000, 12500, 10850, 9000],
}

print("Original data:")
pprint.pprint(user_info)

json_string = json.dumps(user_info)
print("JSON value type:", type(json_string))

with open("data.json", "w") as f:
    f.write(json_string)

with open("data.json") as f:
    json_data = f.read()

data = json.loads(json_data)
print("Python value type:", type(data))

print("Loaded data:")
pprint.pprint(data)
