import pandas as pd
import datetime as DT
today = DT.date.today()

class lookupData:
    def __init__(self):
        self.fooddata = pd.read_csv('data/FoodItemLookup.csv')
    
    def getFoodData(self, order_cat):
        available_food = self.fooddata.copy()
        weeknum = str(today.weekday())
        ava_food = self.fooddata[self.fooddata['availability'].str.contains('|'.join([weeknum])) & self.fooddata['order_category'].str.contains('|'.join([order_cat]))]['item_name']
        return ava_food.tolist()

    def getPastOrders(self, user_id):
        pastData = pd.read_csv('data/orders.csv')
        pastData = pastData[pastData['user_id'].astype(str) == str(user_id)]
        return pastData[-10:].to_dict('list')


