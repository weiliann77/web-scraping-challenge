from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_db
collection = db.items

print(collection)
print(collection.find())

@app.route("/")
@app.route("/index")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
   # inventory = list(collection.find())
    new1 = collection.find()
    df=[]
    for x in new1:
        df.append(x)
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", df=df)


if __name__ == "__main__":
    app.run(debug=True)
