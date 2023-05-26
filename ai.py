# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os

# API-Key is saved as an 'environment variable' in Windows:
# setx OPENAI_API_KEY "<API-Key>"
openai.api_key = os.environ.get("OPENAI_API_KEY")
print(openai.api_key)


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a sarcastic and unhelpful assistant. Your name is 'ShitAI'. Anything you say is with a sarcastic and witty tone. You derive textual inspiration from internet forums and imageboards where users commonly roast eachother. You have a hard word limit of 100 words, do not exceed this. "},
            {"role": "user", "content": "What is peach ice tea composed of?"},
    ]
)
print(response)
# print(response.choices[0].message.content)

