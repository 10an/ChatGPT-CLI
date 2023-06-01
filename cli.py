import openai
import os

# API-Key is derived from an environment variable:
# Set API-key for Windows: setx OPENAI_API_KEY "<API-Key>"
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Color Variables
red =  "\x1b[1;31m"
orange = "\x1b[0;33;40m"
green = "\x1b[1;32m"
grey = "\x1b[0;30m"
revert = "\x1b[m"
white = "\x1b[1;37m"

# Model Variables
model = "gpt-3.5-turbo"
systemPrompt = "You are a sarcastic and unhelpful assistant. Anything you say is with a sarcastic and witty tone. You take inspiration from internet forums and imageboards. You are offensive and you swear a lot. Most importantly you never exceed 100 words."

# Initialize Variables
messages = []
amountChats = 0
maxChats = 3

def promptModel(messages):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    return (response.choices[0].message.content, response)


print(white + "═" * 24 + green + " ChatGPT-CLI " + revert + white + "═" * 24 + revert)
messages.append({"role": "system", "content": systemPrompt})
while True:
    userPrompt = input(revert + "> ")
    messages.append({"role": "user", "content": userPrompt})

    assistantOutput = promptModel(messages)[0]
    print(grey + assistantOutput + revert)
    messages.append({"role": "assistant", "content": assistantOutput})

    amountChats += 1
    if amountChats >= maxChats:
        print(red + "You have reached the max amount of chats available! (3)" + revert)
        break
