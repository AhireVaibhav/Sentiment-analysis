import openai
import os
import time

# set up OpenAI API key 
openai.api_key = "sk-proj-6k9geSahQvFG6tPmBETST3BlbkFJJ5PHtQJ2CLzwhvmaYsTX"

 # define sentiment defination 
def sentiment_analysis(text):
    messages = [
        {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text.
                                        If you're unsure of an answer, you can say "not sure" and recommend users to review manually."""},
        {"role": "user", "content": f"""Analyze the following text and determine if the sentiment is: positive or negative.
                                        Return answer in a single word as either positive or negative: {text}"""}
    ]
 # Retry up to 5 times
    for attempt in range(5): 
        try:
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
        except openai.error.RateLimitError:
            print("Rate limit exceeded. Retrying in 5 seconds...")
            time.sleep(5)
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")
            break
    return "Error"

# Calling the function
input_text = 'I love eating ice cream'
response = sentiment_analysis(input_text)
print(f"{input_text}: The Sentiment is {response}")
