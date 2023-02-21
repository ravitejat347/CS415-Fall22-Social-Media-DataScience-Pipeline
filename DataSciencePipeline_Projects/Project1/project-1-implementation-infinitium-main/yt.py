
import pymongo
import os
import threading
import googleapiclient.discovery

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["youtube"]

videoIds = ["VJjFX8ecxXw","5EYv7cwVz10","rxzEzbk40hM","6IrZzEqI0h4","x5hAqXzmME4","AjkLAC5uGEQ",
"045eW3OqPAQ"]

def getdata():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    mycol.delete_many({})
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    count=0
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    
    for i in range(0,len(videoIds)):
        request = youtube.commentThreads().list(
            part="id,snippet,replies",
            moderationStatus="published",
            maxResults=10000,
            order="relevance",
            videoId=videoIds[i]
        
        )
        response = request.execute()
        for i in range(len(response['items'])):
            data = dict(comment = response['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'],
            likeCount = response['items'][i]['snippet']['topLevelComment']['snippet']['likeCount'],
            time=response['items'][i]['snippet']['topLevelComment']['snippet']['updatedAt'])                                          
            x = mycol.insert_one(data)  
            count=count+1 
            print(response)
    print(count)

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
