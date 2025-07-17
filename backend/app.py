from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/prompt", methods=["POST"])
def generate_response():
    data = request.get_json()
    prompt = data.get("prompt")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return jsonify({"response": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)
