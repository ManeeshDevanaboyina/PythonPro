import json
input='''[
    {
        "name"="Maneesh",
        "No"="8333935371",
        "address"="Eluru"
    },

]'''

data=json.loads(input)
print("Name:",data['name'])
