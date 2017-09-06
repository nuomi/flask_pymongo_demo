from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_HOST'] = 'mongo_test'
app.config['MONGO_DBNAME'] = 'db_test'

mongo = PyMongo(app)



@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route('/all')
def home_page():
    collection = mongo.db.collection.find()
    print('print count')
    print(collection.count())

    item_array= []
    for record in collection:
        del record['_id']
        item_array.append(record)
   
    return jsonify(item_array)

@app.route('/add')
def add():
    item = {'name':'John'}
    try:
        mongo.db.collection.insert(item)
        return jsonify({'ok':1})
    except Exception as e:
        print('on /add ', e)
        return jsonify({'ok':0})

@app.route('/flush')
def flush():
    try:
        mongo.db.collection.drop()
        return jsonify({'ok':1})
    except Exception as e:
        print('on /add ', e)
        return jsonify({'ok':0})



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
