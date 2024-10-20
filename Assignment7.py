import json
import pymongo
data = {}
with open('data.json') as file:
data = json.load(file)
city_country
=
{
"new_york": "usa",
"dallas": "usa",
"beijing": "china",
"colombo": "sri_lanka",
"hong_kong": "china",
"kandy": "sri_lanka",
"wuhan": "china", "chicago": "usa"
# print(data['visa_rates'][city_country["beijing"]])
myclient
=
pymongo.MongoClient ("mongodb://localhost:27017/")
db = myclient["passenger_management_system"]
collection =
db["tickets"]
for t in db['tickets'].find({}):
total = data['visa_rates'][city_country[t['visa_stampped_locations'][-1]]] + int(t['ticket_price'])
print(f"Ticket ID: {t['ticket_id']}")
print("Passenger Name: {t['passenger_name']}")
print (f"Visa Stamped Locations: {', '.join(t['visa_stampped_locations'])}")
print (f"Ticket Price: {t['ticket_price']}")
print (f"Destination: {t['destination']}")
print(f"Total Price: {total}\n")