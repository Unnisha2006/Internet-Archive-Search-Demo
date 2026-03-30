import json
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/books')

with open("1_data.json") as f:
    data = json.load(f)

docs = []

for doc in data:
    docs.append({
        "id": str(doc["id"]),
        "title": doc["title"],
        "author": doc["author"],
        "text": doc["text"],
        "year": doc["year"]
    })

solr.add(docs)
solr.commit()

print("Indexed successfully into Solr")