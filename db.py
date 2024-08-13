import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client['LabDoofNataliaML']
#
userCollection = db['users']
indicationCollection = db['indications']
categoryCollection = db['categories']
examServiceCollection = db['examServices']