from flask import Flask, render_template, request
import openai
import os

################################################## OpenAI API Configuration
messages = []

# Model Variables
model_name = "gpt-3.5-turbo"
system_prompt = "Say Hello Only!"


# Function to prompt the OpenAI model with a list of messages and return the generated response.
def prompt_model(messages):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
    )
    return (response.choices[0].message.content, response)


################################################## Flask Configuration
app = Flask(__name__, template_folder="template")


@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/", methods=["POST"])
def recieve_prompt():
    user_message = request.form.get("userprompt")
    messages.append({"role": "user", "content": user_message})

    assistant_message = prompt_model(messages)[0]
    messages.append({"role": "assistant", "content": assistant_message})

    return render_template("index.html", messages=messages)


# Start Server
app.run(debug=True)
