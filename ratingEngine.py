import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer #install vader lexicon from nltk

class ratingEngine:
    def __init__(self):
        pass
        

    def sentiment_analysis(self,text):
        vader = SentimentIntensityAnalyzer()
        negative = vader.polarity_scores(text)['neg']
        neutral  = vader.polarity_scores(text)['neu']
        positive = vader.polarity_scores(text)['pos']        
        if negative == max(negative , neutral , positive):
            sentiment = "negative"
        elif positive == max(negative , neutral , positive):
            sentiment = "positive"
        else:
            sentiment = "neutral"
        return sentiment 

    def getRating(self):
        pass

    def getPosNegFeedbacks(self):
        feedback = pd.read_csv('data/orders.csv')
        feedback.sort_values(['timestamp'],ascending = False,inplace = True)
        response  = feedback.dropna()[:10][['feedback','sentiment']].to_dict(orient='records')
        return response 

    def saveFeedback(self,emoji,comment,orderid):
        pastfeedback = pd.read_csv('data/orders.csv')
        print(emoji)
        user_rating = None
        
        user_rating = emoji
        if user_rating is None or user_rating == 0:
            user_rating = ""

        print(user_rating)

        pastfeedback.loc[pastfeedback['order_id'].astype(str) == str(orderid) ,'rating'] = user_rating
        pastfeedback.loc[pastfeedback['order_id'].astype(str) == str(orderid) ,'feedback'] = comment
        if comment != "":
            pastfeedback.loc[pastfeedback['order_id'].astype(str) == str(orderid) ,'sentiment'] = self.sentiment_analysis(comment)
        else:
            pastfeedback.loc[pastfeedback['order_id'].astype(str) == str(orderid) ,'sentiment'] = ""
        pastfeedback.to_csv('data/orders.csv',index = False)
        return "Feedback is saved"

        

        



