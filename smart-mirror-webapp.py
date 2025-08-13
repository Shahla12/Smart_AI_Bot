import logging
from flask import Flask,render_template, request, jsonify
from gemini_setup import get_gemini_response

# setup logging for the web app to capture errors and info
logging.basicConfig(
    level= logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

app = Flask(__name__)

@app.route('/')
def index():
    logging.info("Rendering main page.")
    try:
        return render_template("index.html")
    except Exception as e:
        logging.error(f"Error rendering index.html file: {e}")
        return "Error rendering page.",500
    
@app.route('/chat',methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        logging.info(f"Recieved chat message: {user_message}")
        response = get_gemini_response(user_message)
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error in chat(): {e}")
        return jsonify({'response': "An error occured while processing your message."})
    

#_____________ Run the flask App_____________
if __name__=='__main__':
    try:
        logging.info("Starting Flask App...")
        app.run(debug=True)
    except Exception as e:
        logging.error(f"Error starting Flask App: {e}")
