from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__)
CORS(app)


bcrypt = Bcrypt(app)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY") or "super-secret"
jwt = JWTManager(app)
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
