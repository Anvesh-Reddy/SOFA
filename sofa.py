from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from recomEngine import recomEngine
#from ratingEngine import ratingEngine
from lookupData import lookupData

app = Flask(__name__)
app.debug = True
re = recomEngine()
#rt = ratingEngine()
ld = lookupData()
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_ava_food')
def get_available_food():
    food_list = ld.getFoodData()
    #food_list = food_list.to_json()
    return jsonify({"availableItems": food_list})

@app.route('/get_recom_food', methods=['POST'])
def get_recom_food():    
    content = request.get_json()
    user_id = content['user_id']
    order_category = content['order_category']
    date = content['date']
    # Some logic to post method        
    try:
        food_list = re.getRecom(user_id, date, order_category)
    except:
        food_list = []
        print("An exception occurred")    
          
    return json.dumps({'food_list': food_list})

@app.route('/get_rated_food', methods=['POST'])
def get_rated_food():
    content = request.get_json()
    user_id = content['user_id']
    date = content['date']
    # Some logic to post method        
    try:
        food_list = rt.getRating()
    except:
        food_list = []
        print("An exception occurred")    
          
    return json.dumps({'food_list': food_list})

'''
Run Commands

$env:FLASK_APP = "sofa.py"
$env:FLASK_ENV = "development"

export FLASK_APP = "sofa.py"
export FLASK_ENV = "development"

flask run
'''
