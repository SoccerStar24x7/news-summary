from newsapi import NewsApiClient

def NewsFromBBC(news_api_key, query):

    newsapi = NewsApiClient(api_key=news_api_key)
    """
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
    news = requests.get(url).json()

    articles = news["articles"]
    """

    articles = newsapi.get_everything(q=query, language='en')
    # You can also specify date range, etc.

    return articles
