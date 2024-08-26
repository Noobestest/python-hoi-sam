import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import path

def initialization():
    firebase_path = path.dirname(__file__)
    cred = credentials.Certificate(firebase_path + "/serviceAccount.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    return db