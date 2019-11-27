import requests
from const import URL
from keys import API_KEY

def pull_news(country,category):
    """get the top news
    
    args:
    country(str) : two letter country code
    category(str) : specific category
    
    returns:
    data(dict) : a dictionary
    
    raises:
    none"""
    
    params = {
            'country' : country,
            'category' : category,
            'apiKey' : API_KEY
            }
    response = requests.get(TNEWS_URL,params=params)
    data = response.json()
    return data

def format_data(data):
    article_list=[]
    for article in data['articles']:
        title = article['title']
        content = article['content']
        url = article['url']
        source = article['source']['name']
        article_dict = {
            'title':title, 
            'content':content,
            'url':url,
            'source':source
            }
        article_list.append(article_dict)
    return article_list 


