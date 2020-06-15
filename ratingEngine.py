import pandas as pd

class ratingEngine:
    def __init__(self):
        self.fooddata = pd.read_csv('data/FoodItemLookup.csv')
    
    def getRating(self):        
        return ["RatedChickenBiryani"]

