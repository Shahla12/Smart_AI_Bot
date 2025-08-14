# Smart_AI_Bot

## 🛠 Tech Stack & Tools

Programming Language: Python (Backend), JavaScript (Frontend)

Framework: Flask (Python Web Framework)

AI Model: Google Gemini 2.5 Pro API for Generative AI

Frontend: HTML5, CSS3, JavaScript (with Fetch API)

Styling: Custom CSS + Bootstrap for responsive design

Logging: Python logging module for detailed server logs

Environment Variables: .env for secure API key management

## ⚙ Features

💬 Real-time Chat: Sends user input to Flask backend, gets AI-generated replies, and displays them instantly.

⏳ Live Clock: Displays real-time date and time with auto-update every second.

🎨 Clean UI: Minimal dark-themed interface with emoji-enhanced tips and info.

📜 Error Handling: Graceful fallbacks when API is unavailable.

🎯 Brief Mode: AI responds with short, simple sentences for better readability.

## 📂 How it Works

Frontend – User types a message → JavaScript sends a POST request to /chat.

Backend – Flask receives the message, calls get_gemini_response() with a short-reply instruction.

AI Processing – Google Gemini generates a concise reply.

Response Display – The frontend shows the bot’s response in the chat window.


