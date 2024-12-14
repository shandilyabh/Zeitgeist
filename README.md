Zeitgeist is a CLI tool that can be used for article filtering and summarisation.
for an Input string, it returns a JSON object containing following information: {summary, relatedArticles, keywords, ImageURLs, ArticleDescriptions}

tools, libraries and APIs used:
1. Hugging Face Transformers Library (for text summarisation)
2. BeautifulSoup4 (for scraping the web)
3. Google Custom Search Engine & Programmable Search API
4. News API
5. Google Generative AI (PaLM API) (for keyword prediction)
