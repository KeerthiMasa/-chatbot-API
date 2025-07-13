📄 Cohere chatbot API 

This project is a chatbot web application built using Flask and powered by the Cohere API. It allows users to send messages and receive AI-generated responses in real-time through a simple web interface.



🛠️ Technologies Used

| Layer          | Technology                    | Purpose                                 |
| -------------- | ----------------------------- | --------------------------------------- |
| **Frontend**   | HTML, CSS, JavaScript         | Chat UI and user interaction            |
| **Backend**    | Python (Flask)                | Handling routes and API logic           |
| **AI API**     | Cohere API / OpenAI API       | Generating smart chatbot responses      |
| **CORS**       | `flask_cors`                  | Enabling frontend-backend communication |
| **Env Loader** | `python-dotenv`               | Loading environment variables securely  |
| **Storage**    | `chat_history.json` / MongoDB | Saving user-chat history                |
| **Hosting**    | Localhost (Flask dev server)  | Run app locally                         |

✨ Features

| Feature                   | Description                                                             |
| ------------------------- | ----------------------------------------------------------------------- |
| 🤖 AI Chat Response       | Takes user input and returns intelligent replies using Cohere or OpenAI |
| 💾 Chat History Saving    | Stores all past user-bot messages in a `chat_history.json` file         |
| 🔐 Secure API Handling    | Uses `.env` file to store API keys safely                               |
| 🌐 CORS Enabled           | Ensures the frontend can communicate with the backend across origins    |
| 🖥️ Frontend Interface    | Clean HTML/CSS/JS layout for chatting with the bot                      |
| 📦 JSON or MongoDB Option | Choose between local JSON or MongoDB to save and retrieve chat history  |


Now visit: http://127.0.0.1:5000 |
** (Optional) Push to GitHub

git add .
git commit -m "🚀 Initial commit"
git push -u origin main
``` |

---

Shall I give you the **File Structure** section next?
