import datetime
import pymongo
import requests
import os
import threading

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["reddit"]



client_secret = "6O9rtv5ykg5wRR6X6C_j0sm-XGOCAQ"
client_id = "Ki9oc_LFCg4qv7vhaKxwjA"
user_agent = "datasc"
username = "Fresh-Sock7461"
password = "datascience5"
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': username, 'password': password}
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
api_url = 'https://oauth.reddit.com'
headers = {}
subreddits = []
ids = []


def validate():
    bearer_response = requests.post(base_url + 'api/v1/access_token',
                                    data=data,
                                    headers={'user-agent': 'datasc'},
                                    auth=auth)
    if bearer_response.status_code == 200:
        bearer_details = bearer_response.json()
        token = 'bearer ' + bearer_details['access_token']
        headers['Authorization'] = token
        headers['User-Agent'] = user_agent
        response = requests.get(api_url + '/api/v1/me', headers=headers)
        return response.status_code == 200

def getsubs():
    query = (
            'politics' or 'USpolitics' or '2022Elections'or'MidTerms2022' 
            or 'Roe V Wade' or 'GOP' or 'DEMS' 
            or 'abortion' or 'us elections 2022' or 'Election2022' or 'Democrats' or 'Republican' )
    payload = {'q': query, 'limit': 100, 'sort': 'relevance' or 'top' or 'new' or 'hot', 'type': 'sr'}
    subreddit_response = requests.get(api_url + '/search/',
                                      headers=headers, params=payload)
    if subreddit_response.status_code == 200:
        values = subreddit_response.json()
        for i in range(len(values['data']['children'])):
            subreddits.append(values['data']['children'][i]['data']['display_name'])
            ids.append(values['data']['children'][i]['data']['name'])

def getcomments():
    for sub_reddit in subreddits:
        comments_response = requests.get(api_url + '/r/' + sub_reddit + '/comments/', headers=headers)
        if comments_response.status_code == 200:
            values = comments_response.json()
            if values.get('data') is not None:
                val = values.get('data').get('children')
                find(val, sub_reddit, 0, 0, )
    subreddits.clear()

def recordcheck(commentId):
    return mycol.count_documents({"commentId": commentId}, limit=1) == 0

def find(x, subin, indx, indc):
    if len(x) <= indx:
        return
    if x[indx].get('data').get("children") is None:
        if recordcheck(x[indx].get('data').get('id')):
            my_dict = {"subReddits": subin,
                       "comments": x[indx].get('data').get('body'),
                       "created_utc": x[indx].get('data').get('created_utc'),
                       "time": datetime.datetime.now(),
                       "commentId": x[indx].get('data').get('id')
                       }
            mycol.insert_one(my_dict)
            print(my_dict)
        find(x, subin, indx + 1, indc)
    else:
        find(x[indx].get('data').get('children'), subin, 0, 0)

def getdata():
    if validate() is True:
        getsubs()
        getcomments()

def trigger():
    time = 60.0 * 5
    threading.Timer(time, trigger).start()
    os.system('clear')
    getdata()

try:
    trigger()
except Exception as ex:
    file = open('error.txt', 'w+')
    file.write('error caught: %s' % ex)
    file.close()

