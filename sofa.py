from flask import Flask, request
from flask_cors import CORS
import json
from recomEngine import recomEngine

app = Flask(__name__)
app.debug = True
re = recomEngine()
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_recom_food', methods=['POST'])
def get_recom_food():
    user_id = request.form['user_id']
    date = request.form['date']
    # Some logic to post method
    food_list = re.getRecom(user_id, date)
    '''
    try:
        food_list = re.getRecom(user_id, date)
    except:
        print("An exception occurred")
    finally:
        food_list = []
    '''

    return json.dumps({'food_list': food_list})