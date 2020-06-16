import pandas as pd
import datetime as DT
today = DT.date.today()

class lookupData:
    def __init__(self):
        self.fooddata = pd.read_csv('data/FoodItemLookup.csv')
    
    def getFoodData(self):
        available_food = self.fooddata.copy()
        weeknum = str(today.weekday())
        ava_food = self.fooddata[self.fooddata['availability'].str.contains('|'.join([weeknum]))]['item_name']
        return ava_food.tolist()

