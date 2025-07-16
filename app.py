from flask import Flask, request, jsonify
from chatbot.model import ChatModel
from chatbot.filters import is_offensive
from chatbot.logger import log_session

app = Flask(__name__)
chatbot = ChatModel()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message")

    if is_offensive(user_input):
        return jsonify({"response": "I'm really concerned about what you're saying. Please talk to a mental health professional."})
    
    response = chatbot.get_response(user_input)
    log_session(user_input, response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
