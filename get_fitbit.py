import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score
from sklearn.metrics import confusion_matrix, precision_score, recall_score,roc_curve, auc

import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

#Train model
df = pd.read_csv('cardio_train.csv', sep=";")

df.drop(df[(df['height'] > df['height'].quantile(0.975)) 
           | (df['height'] < df['height'].quantile(0.025))].index,inplace=True)

df.drop(df[(df['weight'] > df['weight'].quantile(0.975)) 
           | (df['weight'] < df['weight'].quantile(0.025))].index,inplace=True)

df.drop(df[(df['ap_hi'] > df['ap_hi'].quantile(0.975)) 
           | (df['ap_hi'] < df['ap_hi'].quantile(0.025))].index,inplace=True)

df.drop(df[(df['ap_lo'] > df['ap_lo'].quantile(0.975)) 
           | (df['ap_lo'] < df['ap_lo'].quantile(0.025))].index,inplace=True)

df['bmi'] = df['weight'] / ((df['height']/100) ** 2)

Y = df['cardio']

X = df.drop(['cardio', 'age'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.10)

logistic = LogisticRegression(random_state=12345)
hyperparameters = {'penalty':('l1','l2'),'C':[1,3]}
clf = GridSearchCV(logistic, hyperparameters, cv=3, verbose=0)
best_model = clf.fit(X_train, y_train)


def compute_net_calories():
    return None

def compute_average_sleep():
    return None

def compute_active_time():
    return None

# #Shawn Fan's account
# CLIENT_ID = "22BL47"
# CLIENT_SECRET = "f304815df20aa26cf23966fd0a189688"

#Austin Hwang's account
CLIENT_ID = "22BL49"
CLIENT_SECRET = "784dba49b60709f078f8dbb56f3b5e9b"

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/get_predictions', methods=["POST"])
def getPrediction():

    post_data = request.get_json()

    data = post_data.get('test_data')

    print(data)

    #Convert data to pandas dataframe
    data_df = pd.DataFrame(data, columns = list(df.columns))

    print(data_df)

    pred = best_model.predict(data_df)

    return jsonify(pred)

@app.route('/get_fitbit_data')
def getData():

    data = {}

    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)

    server.browser_authorize()

    ACCESS_TOKEN = str(server.fitbit.client.session.token["access_token"])

    REFRESH_TOKEN = str(server.fitbit.client.session.token["refresh_token"])

    auth2_client = fitbit.Fitbit(
        CLIENT_ID,
        CLIENT_SECRET,
        oauth2=True,
        access_token=ACCESS_TOKEN,
        refresh_token=REFRESH_TOKEN,
    )

    yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))

    # fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')

    period = "30d"

    # #Get meals
    # meals = auth2_client.get_meals()
    # print(meals)

    #Get height 
    height = 0

    #Get weight
    weight = 0

    #Get fat time series
    fat = auth2_client.time_series('body/fat', base_date=yesterday2, period=period)

    #Get BMI time series
    BMI = auth2_client.time_series('body/bmi', base_date=yesterday2, period=period)

    #Get calories series
    ytd = datetime.datetime.now() - datetime.timedelta(days=5)
    caloriesIn = auth2_client.time_series('foods/log/caloriesIn', base_date=yesterday2, period=period)
    caloriesOut = auth2_client.time_series('activities/tracker/calories', base_date=yesterday2, period=period)

    #Get activitiy time series
    very_active = auth2_client.time_series('activities/minutesVeryActive', base_date=yesterday2, period=period)
    fairly_active = auth2_client.time_series('activities/minutesFairlyActive', base_date=yesterday2, period=period)
    active = 1

    #Get sleep in the form of time series
    #To be completeed

    data['minutesActive'] = active
    data['bmi'] = BMI
    data['weight'] = weight
    data['height'] = height
    
    return data


if __name__ == '__main__':
    app.run(debug=True)