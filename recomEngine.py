import pandas as pd
import datetime as DT
today = DT.date.today() #- DT.timedelta(days=1)

class recomEngine:
    def __init__(self):
        today = DT.date.today()
        self.today = DT.date.today()        
        self.fooddata = pd.read_csv('data/FoodItemLookup.csv')
    
    def getRecom(self, user_id, date, order_category):
        self.pastdata = pd.read_csv('data/orders.csv')
        print(date)
        print(user_id)
        print(order_category)

        if not date:
            curDate = today
        else:
            curDate = DT.datetime.strptime(date, '%Y-%m-%d')
        
        preWeek1 = curDate - DT.timedelta(days=7)
        preWeek2 = preWeek1 - DT.timedelta(days=7)
        
        dates = [preWeek1.strftime("%Y-%m-%d"), preWeek2.strftime("%Y-%m-%d")]

        newdata = self.pastdata.copy()
                
        # Condition to filter out date range data
        isDate = (dates[0] == newdata['timestamp'].str[:10]) | (dates[1] == newdata['timestamp'].str[:10])
        isCat = order_category == newdata['order_category']

        recData = newdata[isDate & isCat][['user_id', 'item_id']]        
        
        #Condition to get user details
        isUser = recData['user_id'].astype(str) == user_id        
        
        items = recData[isUser]['item_id']
        print("items", items)
        nonUserData = recData[~isUser]

        #print(recData)
        #Getting list of users who ordered similar food
        compareUsers = nonUserData[nonUserData.item_id.isin(items)]['user_id']

        recFoods = nonUserData[nonUserData['user_id'].isin(compareUsers)]
        recItems = recFoods['item_id'].unique()
        #print(recItems)
        fooditems = self.fooddata[self.fooddata.item_id.isin(recItems)].item_name
        return fooditems.tolist()

