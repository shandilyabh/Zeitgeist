from transformers import pipeline
from search import searchIt
from scrape import scrape
import json
from math import floor
from further import furtherSearch
from getImages import getImagesWithDesc

def json_output(query: str, summary:str, relatedArticles:list, keywords:list, imageLinks:list, descriptions:list):
    '''
    to create a JSON output object:
    '''
    output = {
        "input": query,
        "summary": summary,
        "sources": relatedArticles,
        "keywords": keywords,
        "imageLinks": imageLinks,
        "descriptions": descriptions
    }
    return json.dumps(output, indent=4)

def main():
    query = input("enter the query: ")
    article_urls = searchIt(query)
    text = scrape(article_urls)[:floor(1024*2.9)]

    model = "facebook/bart-large-cnn"
    customise = input("wish to customise the model[Y/N]: ").lower()
    if customise == "y":
        max = input("Max length: ")
        min = input("Min Length: ")
        summariser = pipeline("summarization", model=model)
        summary = summariser(text, max_length=max, min_length=min, do_sample=False)[0]['summary_text']
    else:
        summariser = pipeline("summarization", model=model)
        summary = summariser(text, max_length=250, min_length=50, do_sample=False)[0]['summary_text']
    
    keywords = furtherSearch(text)
    images, articleDescriptions = getImagesWithDesc(query)

    # the JSON output object here:
    output = json_output(query, summary, article_urls, keywords=keywords, imageLinks=images, descriptions=articleDescriptions)
    print(output)
    return output

if __name__ == "__main__":
    main()
