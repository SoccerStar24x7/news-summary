def get_prompt():

    summary_size = 20
    num_of_articles = 10

    prompt = f"Hey Llama, I am going to give you a python dictionary with many different news articles."
    "In this dictionary there is some buffer info, but please filter that out. "
    "I want you to summarize each article. For each article, you are going to: "
    f"1) Give a summarized title about the article; keep it less than {summary_size} words."
    " 2) Give a 2-3 sentence summary of the news article."
    " This should cover the main parts of the article.  "
    f" 3) Give the URL of the article. Do this for the first {num_of_articles} articles that were released closest to today. "
    "Please do not inject random new information into the summaries,"
    " but rather rephrase it to be more concise, but keeping the main points still there."
    " PLEASE ONLY RESPOND WITH THE INFO LISTED ABOVE; DO NOT SAY 'Sure! I can do that!' or any"
    "sort of reassurance like that. Please only respond with the info above, and nothing else."
    "The format should be as follows: "
    "Title: [title of article], "
    "Summary: [summary of article], "
    "URL: [url of article]."
    "The articles are listed after this: "

    return prompt