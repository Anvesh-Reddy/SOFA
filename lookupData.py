import pandas as pd
import datetime as DT
today = DT.date.today() - DT.timedelta(days=1)

class lookupData:
    def __init__(self):
        self.fooddata = pd.read_csv('data/FoodItemLookup.csv')
    
    def getFoodData(self, order_cat):
        available_food = self.fooddata.copy()
        weeknum = str(today.weekday())
        ava_food = available_food[available_food['availability'].str.contains('|'.join([weeknum])) & available_food['order_category'].str.contains('|'.join([order_cat]))]
        return ava_food[['item_id', 'item_name', 'price']].to_dict(orient='records')

    def getPastOrders(self, user_id):
        pastData = pd.read_csv('data/orders.csv')
        pastData = pastData[pastData['user_id'].astype(str) == str(user_id)]        
        mergedData = pd.merge(pastData[['order_id', 'order_date', 'order_category', 'item_id', 'feedback', 'sentiment', 'rating']], self.fooddata[['item_id', 'item_name', 'price']], on='item_id')        
        mergedData.fillna("", inplace=True)
        mergedData = mergedData.sort_values(['order_date'], ascending=False)   
        return mergedData[:10].to_dict(orient='records')


