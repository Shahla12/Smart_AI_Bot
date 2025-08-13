// static/script.js
    // JavaScript for smart Mirror Chatbot
//This script handles the chat functionality, including sending messages and displaying responses.
const chat= document.getElementById('chat');
        const form = document.getElementById('chat-form');
        const input= document.getElementById('user-input');

        function scrollToBottom() {
            chat.scrollTop = chat.scrollHeight;
        }

        form.onsubmit = async (e) => {
            e.preventDefault();
            const userMsg = input.value;
            chat.innerHTML += `<div class="user"> ${userMsg}</div>`;
            input.value = '';
            scrollToBottom();
            const res = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: userMsg})
            });
            const data = await res.json();
            chat.innerHTML += `<div class="bot"> ${data.response}</div>`;
            scrollToBottom();
        };

        // Focus input on page load
        window.onload = () => {
            input.focus();
        };

// Function to update the current timestamp every second
function updateTimestamp() {
    const now = new Date();
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    };
    document.getElementById('current-timestamp').textContent = now.toLocaleString(undefined, options);
}

updateTimestamp();
setInterval(updateTimestamp, 1000);