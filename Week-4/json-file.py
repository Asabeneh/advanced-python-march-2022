# what is a JSON?
# JavaScript Object Notation
import json

person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
print(type(person_dct))

json_data = json.dumps(person_dct)
print(json_data)
print(type(json_data))

persons = [
	{
    "name":"Timo",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
},
{
    "name":"Maria",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
},
{
    "name":"Irina",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
},
{
    "name":"Iso",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
},
{
    "name":"Heikki",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
},
{
    "name":"Vesa",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}

]

with open('test.json', 'w') as f:
	json.dump(persons, f, indent=4)
