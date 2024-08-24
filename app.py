import os
from dotenv import load_dotenv
import openai
from flask import Flask, request, jsonify

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_request():
    data = request.json
    user_input = data.get('user_input')
    
    if not user_input:
        return jsonify({'error': 'No user_input provided'}), 400
    
    response_text = generate_response(user_input)
    return jsonify({'response': response_text})

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an English teacher, and must help the user to practice English"},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    app.run(port=8080)
