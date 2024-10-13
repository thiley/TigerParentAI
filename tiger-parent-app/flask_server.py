import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from openAPIConnection import get_response
from TigerParentVoice import text_to_speech_file

app = Flask(__name__)

CORS(app)

@app.route('/response_text', methods = ['POST'])
def response_text():
    #extract input from JSON request
    user_input = request.json.get('input')

    gpt_response = get_response(user_input)
    #file path of the mp3
    audio_file = text_to_speech_file(gpt_response)
    return jsonify({'response' : gpt_response, 'audio_url' : f'/response_speech/{audio_file}'})

@app.route('/response_speech/<filename>', methods = ['POST'])
def response_speech(filename):
    return send_file(f"audio/{filename}", mimetype='audio/mpeg')

@app.route('/delete_mp3', methods = ['POST'])
def delete_mp3():
    data = request.json
    filename = data.get('filename')  # Get the filename from the request
    if filename:
        try:
            os.remove(f"audio/{filename}")
            return jsonify({'message': 'Audio file deleted successfully'})
        except FileNotFoundError:
            return jsonify({'error': 'File not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'No filename provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)