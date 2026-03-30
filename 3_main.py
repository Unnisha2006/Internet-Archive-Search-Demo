from fastapi import FastAPI
import pysolr

app = FastAPI()

solr = pysolr.Solr('http://localhost:8983/solr/books')

@app.get("/search")
def search(q: str):
    results = solr.search(q, **{
        "df": "text",
        "hl": "true",
        "hl.fl": "title,text"
    })

    return {
        "results": [
            {
                "id": r.get("id"),
                "title": r.get("title"),
                "author": r.get("author"),
                "year": r.get("year")
            }
            for r in results
        ]
    }