import fetch_articles
import prompt
import ask_llama

news_api_key = "4d6be2d9c963477695807c50b3c45274"

query = "technology"

prompt = prompt.get_prompt()


# Driver Code
if __name__ == '__main__':
    # function call
    articles = fetch_articles.NewsFromBBC(news_api_key=news_api_key, query=query)

    response = str(ask_llama.ask(model_name="llama3.2:latest", prompt=prompt, articles=articles))

    print(response)
