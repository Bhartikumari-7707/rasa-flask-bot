from flask import Flask, render_template, request, jsonify
import requests

# RASA_API_URL =  "http://127.0.0.1:5005/webhooks/rest/webhook"
import os

RASA_API_URL = os.getenv("RASA_API_URL", "http://127.0.0.1:5005/webhooks/rest/webhook")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    # Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else "Sorry, I did not understand that."

    return jsonify({'response': bot_response})


# if __name__ == "__main__":
#     app.run(debug=True, port=3000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# if __name__ == '__main__':
#     import os
#     port = int(os.environ.get("PORT", 3000))
#     app.run(host='0.0.0.0', port=port)
