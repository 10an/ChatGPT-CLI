import openai
import os

# Derive API-key from an environment variable.
# Set API-key for Windows: setx OPENAI_API_KEY "<API-Key>"
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Color Variables
red = "\x1b[1;31m"
orange = "\x1b[0;33;40m"
green = "\x1b[1;32m"
grey = "\x1b[0;30m"
white = "\x1b[1;37m"
revert_color = "\x1b[m"

# Model Variables
model_name = "gpt-3.5-turbo"
system_prompt = "You are a sarcastic and unhelpful assistant. Anything you say is with a sarcastic and witty tone. You take inspiration from internet forums and imageboards. You are offensive and you swear a lot. Most importantly, you never exceed 100 words."

# Chat Variables
messages = []
chat_count = 0
chat_max = 3

# Function to prompt the OpenAI model with a list of messages and return the generated response.
def promptModel(messages):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
    )
    return (response.choices[0].message.content, response)

# Introduction
print(
    white
    + "═" * 24
    + green
    + " ChatGPT-CLI "
    + revert_color
    + white
    + "═" * 24
    + revert_color
)

# Append system prompt to the messages list
messages.append({"role": "system", "content": system_prompt})

while True:
    # Get user input and add it to the messages list.
    userPrompt = input(revert_color + "> ")
    messages.append({"role": "user", "content": userPrompt})

    # Get assistant output, print it, and add it to the messages list.
    assistantOutput = promptModel(messages)[0]
    print(grey + assistantOutput + revert_color)
    messages.append({"role": "assistant", "content": assistantOutput})

    # Check chat count limit.
    chat_count += 1
    if chat_count >= chat_max:
        print(
            red
            + "You have reached the max amount of chats available! (3)"
            + revert_color
        )
        break