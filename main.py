import fetch_articles
import prompt
import ask_llama


news_api_key = "ENTER NEWSAPI KEY"

query = "ENTER QUERY"

num_of_articles = int("ENTER # OF ARTICLES")


prompt = prompt.get_prompt()


# Driver Code
if __name__ == '__main__':
    # function call
    articles = fetch_articles.NewsFromBBC(news_api_key=news_api_key, query=query)

    response = str(ask_llama.ask(model_name="llama3.2:latest", prompt=prompt, articles=articles))

    print(response)
