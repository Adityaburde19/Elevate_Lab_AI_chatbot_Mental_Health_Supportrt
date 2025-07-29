from flask import Flask, request, jsonify
from chatbot.model import ChatModel
from chatbot.filters import is_offensive, flag_keywords
from chatbot.logger import log_session
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

chatbot = ChatModel()

@app.route("/chat", methods=["POST"])
def chat():
    start_time = time.time()
    data = request.get_json()
    user_input = data.get("message", "").strip()
    session_id = data.get("session_id", "default")

    if not user_input:
        return jsonify({"error": "Message is empty"}), 400

    try:
        if is_offensive(user_input):
            flagged = flag_keywords(user_input)
            response = (
                "I'm really concerned about what you're saying. "
                "Please talk to a licensed mental health professional or call a local helpline. "
                f"(Detected: {', '.join(flagged)})"
            )
        else:
            response = chatbot.get_response(user_input, session_id)

        log_session(session_id, user_input, response)

        return jsonify({
            "response": response,
            "session_id": session_id,
            "elapsed_ms": round((time.time() - start_time) * 1000, 2)
        }), 200

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": "Something went wrong, please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True)
