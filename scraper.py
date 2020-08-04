import scrape_mars as sd

Dict1 = sd.scrape
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn) 
client.drop_database(mars_db)
db = client.mars_db
collection = db.items
for x in Dict1:
    try:
        collection.insert_one(x)
    except:
        pass