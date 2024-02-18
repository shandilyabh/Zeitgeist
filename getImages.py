# to take the query and search for top three images with news descriptions via News API
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()
news_api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=news_api_key)

def getImagesWithDesc(query:str):
    all_articles = newsapi.get_everything(q=query,
                                        sources="the-hindu,the-times-of-india,google-news-in", 
                                        language='en',
                                        sort_by='relevancy',
                                        page_size=3,
                                        page=1)
    
    # saving the top three articles' Images and descriptions:
    imageLinks = []
    articleDescriptions = []
    for i in range(len(all_articles['articles'])):
        imageLinks.append(all_articles['articles'][i]['urlToImage'])
        articleDescriptions.append(all_articles['articles'][i]['title'])

    return [imageLinks if (len(all_articles['articles']) < 3) else imageLinks[:3], articleDescriptions if (len(all_articles['articles']) < 3) else articleDescriptions[:3]]