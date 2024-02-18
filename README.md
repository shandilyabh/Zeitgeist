Zeitgeist is a CLI tool that can be used for article filtering and summarisation.
for an Input string, it return a JSON object containing following information: {summary, relatedArticles, keywords, ImageURLs, ArticleDescriptions}

workflow:
> searches for top 3 articles on the web against the input query provided by the user, using Custom Search Engine (Google) API & Langchain
> fetches links to the articles and forms a list: relatedArticles.
> scrapes the webpage of the first link for text. (scrape.py)
> the text is truncated to the maximum sequrence length (1024) of the text summarisation model.
> the text is processed by BART-Large-CNN model (via hugging face trabsformers library) for generating a summary.
