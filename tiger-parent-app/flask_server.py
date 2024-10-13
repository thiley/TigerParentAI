from flask import Flask, request, jsonify
from flask_cors import CORS
from openAPIConnection import get_response

app = Flask(__name__)

CORS(app)

@app.route('/response_text', methods = ['POST'])
def response_text():
    #extract input from JSON request
    user_input = request.json.get('input')

    gpt_response = get_response(user_input)

    return jsonify({'response' : gpt_response})

if __name__ == '__main__':
    app.run(debug=True)