from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import cohere
import os
import json
from dotenv import load_dotenv

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

app = Flask(__name__)
CORS(app)

HISTORY_FILE = "chat_history.json"

def get_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(user, bot):
    history = get_history()
    history.append({"user": user, "bot": bot})
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

# GUI HTML Template
html_template = """
<!DOCTYPE html>
<html>
<head>
  <title>Chatbot - Cohere</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(to right, #e0f7fa, #ffffff);
      padding: 0;
      margin: 0;
    }
    .container {
      max-width: 800px;
      margin: 40px auto;
      padding: 20px;
      background: white;
      border-radius: 16px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    h2 {
      text-align: center;
      color: #00796B;
      margin-bottom: 20px;
    }
    #messages {
      height: 400px;
      overflow-y: auto;
      border: 1px solid #ddd;
      border-radius: 10px;
      padding: 10px;
      background: #f9f9f9;
      margin-bottom: 10px;
    }
    .message {
      margin: 10px 0;
      padding: 10px;
      border-radius: 10px;
      max-width: 80%;
      clear: both;
    }
    .user {
      background-color: #DCF8C6;
      float: right;
      text-align: right;
    }
    .bot {
      background-color: #E1F5FE;
      float: left;
    }
    input[type="text"] {
      padding: 10px;
      width: 70%;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin-right: 10px;
    }
    button {
      padding: 10px 20px;
      background-color: #00796B;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
    }
    button:hover {
      background-color: #004D40;
    }
    #searchInput {
      width: 100%;
      padding: 10px;
      margin: 10px 0 20px 0;
      border-radius: 8px;
      border: 1px solid #ccc;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>🤖 Cohere Chatbot</h2>
    
    <input type="text" id="searchInput" onkeyup="searchMessages()" placeholder="🔍 Search history..." />

    <div id="messages"></div>

    <div style="margin-top: 10px;">
      <input type="text" id="input" placeholder="Type your message..." />
      <button onclick="sendMessage()">Send</button>
    </div>
  </div>

  <script>
    async function sendMessage() {
      const input = document.getElementById("input");
      const messages = document.getElementById("messages");
      const userText = input.value.trim();
      if (!userText) return;

      messages.innerHTML += `<div class='message user'><b>You:</b> ${userText}</div>`;
      input.value = "";

      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
      });

      const data = await res.json();
      messages.innerHTML += `<div class='message bot'><b>Bot:</b> ${data.response}</div>`;
      messages.scrollTop = messages.scrollHeight;
    }

    function searchMessages() {
      const input = document.getElementById("searchInput").value.toLowerCase();
      const messages = document.querySelectorAll("#messages .message");
      messages.forEach(msg => {
        if (msg.textContent.toLowerCase().includes(input)) {
          msg.style.display = "block";
        } else {
          msg.style.display = "none";
        }
      });
    }
  </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(html_template)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    response = co.chat(
        message=user_input,
        model="command-r-plus",
        temperature=0.7,
        chat_history=[]
    )

    bot_output = response.text
    save_history(user_input, bot_output)
    return jsonify({"response": bot_output})

if __name__ == "__main__":
    app.run(debug=True)
