from pymongo import MongoClient
import csv
import json
import ast

# mongoClient = MongoClient(
#     "mongodb+srv://Ulysses:<password>@cluster0.6oh1v.mongodb.net/cs573Data?retryWrites=true&w=majority")
# print(mongoClient)
# db = mongoClient.cs573Data
# db.ted_talk.drop()

csvfile = open('ted_main.csv', 'r', encoding="utf-8")
reader = list(csv.DictReader(csvfile))
oneLine = dict(reader[0])
header = list(oneLine.keys())
print(header)
result = []
for each in reader:
    row = {}
    for field in header:
        # ratings
        # related talks
        # tags
        if field == "ratings" or field == "related_talks" or field == "tags":
            row[field] = ast.literal_eval(each[field])
        elif field == "url":
            row[field] = each[field].strip()
        else:
            row[field] = each[field]
    result.append(row)

with open('ted_talk.json', 'w') as outfile:
    json.dump(result, outfile)