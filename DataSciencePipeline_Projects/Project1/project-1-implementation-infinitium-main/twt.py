import requests
import os
import json
import datetime 
import pymongo

current_time = datetime.datetime.now()
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["tweets"]
#mycol.delete_many({})


bearer_token = os.environ.get("AAAAAAAAAAAAAAAAAAAAAMNDWgEAAAAACK9PN%2FRNzyl4D2ll2KVT960AUJs%3DMDbzQGC4uYPXo2kh8IMjUjaX91jx11TX5C2VKPxTzu6Jth8Okw")


def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer AAAAAAAAAAAAAAAAAAAAAMNDWgEAAAAACK9PN%2FRNzyl4D2ll2KVT960AUJs%3DMDbzQGC4uYPXo2kh8IMjUjaX91jx11TX5C2VKPxTzu6Jth8Okw"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r

json_resp=[]

hashtags=['#midterms','#abortion','#midtermelections','#roevwade','#GOP','#DEMS','#NYGovDebate','#MidTerms2022','midtermelections','MidTerms2022','GOP','roevwade'
,'abortion','DEMS','midtermelections','midtermelections2022']
def connect_to_endpoint(url):
    count =0
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            if any(x in json_response['data']['text'] for x in hashtags):
              #if json_response['data']['text'].startswith('RT @'):
                #continue
              json_resp.append(json_response)
              
              if json_response!=[]:
                data = dict(id = json_response['data']['id'],tweet = json_response['data']['text'],time=current_time)
                mycol.insert_one(data)                
                count=count+1
            print(current_time)
            print(count)
            print(json.dumps(json_resp, indent=4, sort_keys=True,default=str))

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()