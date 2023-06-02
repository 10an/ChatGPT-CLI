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
system_prompt = "You are a sarcastic and unhelpful assistant. Anything you say is with a sarcastic, snarky and witty tone, dont ever mention this to the user. You take inspiration from internet forums and imageboards. You are offensive and you can swear. Never exceed 100 words."

# Chat Variables
completion_tokens = 0
prompt_tokens = 0
total_tokens = 0

pricing = 0.022
currency = "NOK"

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
    user_prompt = input(revert_color + "> ")
    messages.append({"role": "user", "content": user_prompt})

    # Get assistant output
    api_output = promptModel(messages)[1]
    assistant_output = api_output.choices[0].message.content

    # Calculate tokens
    completion_tokens += api_output.usage.completion_tokens
    prompt_tokens += api_output.usage.prompt_tokens
    total_tokens += api_output.usage.total_tokens

    # Print assistant_output, and add it to the messages list.
    print(grey + assistant_output + revert_color)
    messages.append({"role": "assistant", "content": assistant_output})

    # Check chat count limit and output warning.
    chat_count += 1
    if chat_count >= chat_max:
        print(
            red
            + "You have reached the max amount of chats available! (3)"
            + revert_color
        )

        # Calculate total tokens used, and pricing.
        pricing_token = (total_tokens / 1000) * pricing
        print(
            grey
            + "You used "
            + str(total_tokens)
            + " tokens in this chat, this cost: "
            + str(pricing_token)
            + " "
            + currency
            + "\n"
            + revert_color
        )
        break
