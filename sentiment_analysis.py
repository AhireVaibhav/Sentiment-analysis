import openai
import os

# Make sure to set your OpenAI API key as an environment variable for security
openai.api_key = "sk-proj-6k9geSahQvFG6tPmBETST3BlbkFJJ5PHtQJ2CLzwhvmaYsTX"

def sentiment_analysis(text):
    messages = [
        {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text.
                                        If you're unsure of an answer, you can say "not sure" and recommend users to review manually."""},
        {"role": "user", "content": f"""Analyze the following text and determine if the sentiment is: positive or negative.
                                        Return answer in a single word as either positive or negative: {text}"""}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0
    )

    response_text = response['choices'][0]['message']['content'].strip().lower()

    return response_text

# Calling the function
input_text = 'I love eating ice cream'
response = sentiment_analysis(input_text)
print(f"{input_text}: The Sentiment is {response}")
