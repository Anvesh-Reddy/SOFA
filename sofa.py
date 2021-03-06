from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from recomEngine import recomEngine
from ratingEngine import ratingEngine
from forecastEngine import forecastEngine
from lookupData import lookupData

app = Flask(__name__)
app.debug = True
re = recomEngine()
rt = ratingEngine()
fe = forecastEngine()
ld = lookupData()
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_ava_food')
def get_available_food():    
    args = request.args
    print(args)  
    order_cat = args['order_cat']
    food_list = ld.getFoodData(order_cat)    
    return jsonify({"availableItems": food_list})

@app.route('/get_past_orders', methods=['POST'])
def get_past_orders():
    content = request.get_json()
    user_id = content['user_id']
    past_orders = ld.getPastOrders(user_id)    
    return json.dumps({'past_orders': past_orders})

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

@app.route('/save_feedback', methods=['POST'])
def save_feedback():
    content = request.get_json()
    print(content)
    order_id = content['order_id']
    emoji = content['emoji']
    comment = content['comment']
    # Some logic to post method        
    try:
        response = rt.saveFeedback(emoji, comment, order_id)
    except:
        response = ""
        print("An exception occurred")          
    return json.dumps({"response": response})

@app.route('/get_feedbacks')
def getPosNegFeedbacks():    
    feedbacks = rt.getPosNegFeedbacks()          
    return json.dumps({'feedbacks': feedbacks})

@app.route('/get_forecast_data')
def getForecastData():    
    response = fe.get_forecast()     
    return json.dumps({"output": response})


if __name__ == "__main__":
    app.run()
'''
Run Commands

$env:FLASK_APP = "sofa.py"
$env:FLASK_ENV = "development"

export FLASK_APP = "sofa.py"
export FLASK_ENV = "development"

flask run
'''
