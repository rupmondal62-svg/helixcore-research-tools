# Then build this script
from Bio import Entrez
import json

Entrez.email = "helixcoreintelligence@gmail.com"

def fetch_cancer_papers(keyword, max_results=20):
    handle = Entrez.esearch(
        db="pubmed",
        term=keyword,
        retmax=max_results
    )
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    papers = []
    for pid in ids:
        fetch = Entrez.efetch(
            db="pubmed",
            id=pid,
            rettype="abstract",
            retmode="text"
        )
        papers.append(fetch.read())
    
    return papers

results = fetch_cancer_papers("AI cancer drug discovery 2024")
for i, paper in enumerate(results[:5]):
    print(f"Paper {i+1}:\n{paper}\n{'='*50}")