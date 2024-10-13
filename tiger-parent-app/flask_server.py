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

    return jsonify({'response' : gpt_response, 'audio_url' : f'/get_audio/{audio_file}'})

@app.route('/get_audio/<filename>', methods = ['GET'])
def get_audio(filename):
    return send_file(filename, mimetype='audio/mpeg')


@app.route('/delete_audio', methods = ['POST'])
def delete_audio():
    data = request.json
    filename = data.get('filename')  # Get the filename from the request
    if filename:
        try:
            os.remove(f"{filename}")
            return jsonify({'message': 'Audio file deleted successfully'})
        except FileNotFoundError:
            return jsonify({'error': 'File not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'No filename provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)