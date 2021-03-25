travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
add_new_country=["Russia", 2, ["Moscow", "Saint Petersburg"]]
travel_log.append(add_new_country)
def visited():
    for i in travel_log[2] :
        print(f"estes es lo que vota {i}")
#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
visited()