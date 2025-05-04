import ollama


def ask(model_name, prompt, articles):
    try:
        fizz = str(articles)
        promptz = prompt + fizz
        # Send a prompt to the model
        response = str(ollama.chat(model=model_name,
                               messages=[{'role': 'user', 'content': promptz}]))

        index = response.index("content=")
        return response[(index + 8):]

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1