import csv
from typing import List

from Whisky import Whisky, FieldName


whiskies: list[Whisky] = []

with open("data.csv", 'r') as file:
    dictreader = csv.DictReader(file)
    header = next(dictreader)
    for row in dictreader:
        whiskies.append(
            Whisky(row['Name'], row["Rating"], row["Country"], row["Category"], row["Price"], row["ABV"], row["Age"],
                   row["Brand"]))


condition = True
x = ""
while condition:
    x = input("what do you want?")
    if x in ["name", "rating", "country"]:
        condition = False

for i in range(0, 10):
    val = ""
    if x == "name": val = whiskies[i].name
    elif x == "rating": val = whiskies[i].rating
    elif x == "country": val = whiskies[i].country
    print(val)

