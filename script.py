from pymongo import MongoClient
import requests

MONGOURL = ""
DATABASE = "spotsaasdb"
COLLECTION = "products"

client = MongoClient(MONGOURL)
db = client[DATABASE]
collection = db[COLLECTION]

def isValidLink(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return True
        return False
    except:
        return False

processes_documents = 0
for document in collection.find():
    videoURL = []
    for url in document['videoUrls']:
        if(isValidLink(url)):
            videoURL.append(url)
        collection.update_one(
        {'_id': document['_id']},
        {'$set': {'videoUrls':videoURL} }
        )
    print(f'{processes_documents+1} documents processesed')

client.close()