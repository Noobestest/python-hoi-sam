from flask import Flask
from database.database import initialization
import json

app = Flask(__name__)
#db = initialization()

@app.get("/")
def read_root():
    #db.collection('persons').add({'name':'Me'})
    #details = db.collection('persons').get()
    #for detail in details:
    #    print(detail)
    return {"url": "Hii" }


# another route to serve a user
@app.get("/data/")
def read_data():
    return {"name": "GeeksForGeeks",
            "url": "https://practice.geeksforgeeks.org/"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)