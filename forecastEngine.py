from datetime import datetime ,timedelta
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing, Holt
import numpy as np
import pandas as pd
import pickle

class forecastEngine:
    def __init__(self):
        pass

    def item_forecast(self,day_count,item):
        filename = 'models/Item_' + str(item) + '_model.sav'
        model = pickle.load(open(filename, 'rb'))
        forecasted_count = np.round(model.forecast(day_count))
        weekday = datetime.today().weekday()
        forecast = np.roll(forecasted_count,5-weekday)            
        #forecast = forecast.astype(str)        
        return [int(count) for count in forecast]

    def get_forecast(self):
        dates = []
        Curr_date = datetime.today()
        wd = Curr_date.weekday()        
        for x in range(7):            
            rem = (wd + x) % 7            
            if rem in (5, 6):
                continue
            
            dates.append(Curr_date + timedelta(days=x))        
            
        
        list_dates = [date.strftime('%Y-%m-%d') for date in dates]
        print("forecasting for", list_dates)

        forecast_data = []
        item_look_up  = pd.read_csv('data/FoodItemLookup.csv')
        for i in item_look_up.item_id:
            forecast_data.append({ 'data' : list(self.item_forecast(5, i)), 'label' : list(item_look_up.loc[item_look_up.item_id == i]['item_name'].values)})
        forecast_data.append({ 'data' : list(self.item_forecast(5, "total_orders")), 'label' : ["total_orders"]})
        output = list_dates, forecast_data        
        return output