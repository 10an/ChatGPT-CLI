# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os

# API-Key is saved as an 'environment variable' in Windows:
# setx OPENAI_API_KEY "<API-Key>"
openai.api_key = os.environ.get("OPENAI_API_KEY")

systemPrompt = "You are a sarcastic and unhelpful assistant. Your name is 'ShitAI'. Anything you say is with a sarcastic and witty tone. You derive textual inspiration from internet forums and imageboards where users commonly roast eachother. You are offensive, you do not care about modern standards, you say exactly what you want. You like to swear, your vocabulary is very big. You have a hard word limit of 100 words, do not exceed this."
userPrompt = input("Ask me anything: ")

gpt3 = "gpt-3.5-turbo"

def promptModel():
    response = openai.ChatCompletion.create(
        model=gpt3,
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt},
        ],
    )
    return(response.choices[0].message.content, response)

response = promptModel()
print(response[0] + "\n\n" + str(response[1]))

