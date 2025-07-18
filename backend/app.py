from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this
from quiz_generator import generate_quiz
from watsonx_adapter import get_model_response

app = Flask(__name__)
CORS(app)  # ✅ Allow requests from any origin

@app.route("/generate_quiz", methods=["POST"])
def quiz():
    data = request.json
    topic = data.get("topic")
    quiz = generate_quiz(topic)
    return jsonify(quiz)

if __name__ == "__main__":
    app.run(debug=True)
