# project-1-implementation-infinitium
project-1-implementation-infinitium created by GitHub Classroom
## Project Abstract

Abortion has always been a controversy around the world. In 1973, the U.S. Supreme Court determined the verdict of the case of Roe vs. Wade. This decision proved to be a landmark one for the nation. The U.S. Supreme Court ruled that the decision whether to continue or terminate a pregnancy depends on the individual, not the government. However, in June 2022, the Supreme Court reversed the decision of Roe vs. Wade and declared that there is no longer a federal constitutional right to an abortion. In the light of these recent events, it seems that this issue will have a high impact on the midterm elections of the United States. 

In this project, we intend to gain an overview of the general public and their thoughts on this particular issue and how it will affect the midterm elections being held in November of this year. Social media is the best option to gather data for this. We will collect data from various forms of social media such as Twitter, Reddit, and YouTube to analyze the impact of abortion rights on the midterm elections being held.

## Team - Infinitium

* Ami Chauhan, achauha4@binghamton.edu
* Kirtika Jawerilal, kjaweri1@binghamton.edu
* Prarthna Mohanraj, pmohanr1@binghamton.edu
* Suryavardhan Thummala, sthumma1@binghamton.edu
* Ravi Teja Tadiboina, rtadibo1@binghamton.edu

## Tech-stack

* `python` - The project is developed and tested using python v3.8. [Python Website](https://www.python.org/)
* `request` - Request is a popular HTTP networking module(aka library) for python programming language. [Request Website](https://docs.python-requests.org/en/latest/#)
* `MongoDB`- This project uses NoSQL database for saving collected data. 
    * [MongoDB Website](https://www.mongodb.com/)


## Three data-source documentation

This section must include two things for each source: (1) A specific end-point URL(aka API) or Website link if you are crawling web-pages (2) Documentation of the API

* `Twitter`
  * [Sampled Stream API](https://api.twitter.com/2/tweets/sample/stream) - <A regular 1% volume stream API from Twitter.>
* `Reddit` - We are using `r/politics`, `r/USpolitics`,`r/RoevWade`...
  * [r/politics](https://reddit.com/r/politics) - <This subreddit is for news and discussion about U.S. politics.>
  * [r/USpolitics](https://reddit.com/r/USpolitics) - <This subreddit is for US politics.>
  * [r/RoevWade](https://reddit.com/r/RoevWade) - <This subreddit is for a discussion of Roe v Wade.>
  * [Search API](https://www.reddit.com/dev/api/#GET_search) - <API used to search for subreddits and extract information.>
* `YouTube`
  * [Google Client API](https://developers.google.com/youtube/v3/libraries) - <API used to interact with YouTube to retrieve comments.>

## System Architecture

![System Architecture]
![Project1Diagram](https://user-images.githubusercontent.com/112434936/199145291-393b35f4-2abe-4e0a-b260-dec83c7edf37.PNG)

## How to run the project?

Install `Python` and `MongoDB`

```bash
pip3 install pymongo
cd project-1-implementation-infinitium/src/
python3 twt.py
python3 rdt.py
python3 yt.py
```

## Database schema - NoSQL (Remove this section if you are using SQL database)

```bash

collection_1: tweets
{
  "id": ...,
  "tweet": ...,
  "time": ...
}

collection_2: reddit
{
  "id": ...,
  "subReddits": ...,
  "comments": ...,
  "created_utc": ...,
  "time": ...,
  "commentId": ...
}

collection_3: youtube
{
  "id": ...,
  "comment": ...,
  "likeCount": ...,
  "time": ...
}
```

Notes:

- Need twitter developer account credentials
- Need reddit secret key and id
- Need google client oAuth and API key
