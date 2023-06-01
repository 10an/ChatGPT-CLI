from flask import Flask, render_template, url_for, request
import openai
import os

################################################## OpenAI API Configuration
openai.api_key = os.environ.get("OPENAI_API_KEY")
model = "gpt-3.5-turbo"
systemPrompt = "You are a sarcastic and unhelpful assistant. Anything you say is with a sarcastic and witty tone. Take inspiration from internet forums and imageboards. You are offensive and you like to swear. Do not exceed 100 words."


def promptModel(messages):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    return (response.choices[0].message.content, response)


messages = [
    {"role": "system", "content": systemPrompt},
]


################################################## Flask Configuration
app = Flask(__name__, template_folder="template")


@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/chat", methods=["POST"])
def recieve():
    userPrompt = request.form.get("userPrompt")
    messages.append({"role": "user", "content": userPrompt})

    apiOutput = promptModel(messages)
    assistantOutput = apiOutput[0]

    if assistantOutput:
        print("\n" + str(apiOutput) + "\n")
        messages.append({"role": "assistant", "content": assistantOutput})
        for message in messages:
            if message["role"] == "assistant":
                print(message["content"])
            elif message["role"] == "user":
                print(message["content"])
        return "<p>" + assistantOutput + "</p>"
    


# Start Server
app.run(debug=True)
