import fetch_articles
import prompt
import ask_llama

try:
    news_api_key = "ENTER NEWSAPI KEY"
except:
    print("User: You must add a valid NewsAPI Key. Program is shutting off.")
    exit(2)


query = "ENTER QUERY"

try:
    num_of_articles = int("ENTER # OF ARTICLES")
except ValueError:
    print("User: Please enter # of articles you want. Defaulting to 5 articles.")
    num_of_articles = 5

prompt = prompt.get_prompt()


# Driver Code
if __name__ == '__main__':
    # function call
    articles = fetch_articles.NewsFromBBC(news_api_key=news_api_key, query=query)

    response = str(ask_llama.ask(model_name="llama3.2:latest", prompt=prompt, articles=articles))

    print(response)
