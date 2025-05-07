from flask import Flask, request, jsonify,send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
from PredictionUtils import predict_language

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

@app.route('/',methods=['GET'])
def root():
    return send_from_directory('static','index.html')


@app.route('/submit-code', methods=['POST'])
def submit_code():
    code_text = request.form.get('code')
    uploaded_file = request.files.get('file')

    prediction_code='Unknown'
    prediction_file='Unknown'
    file_path = None
    file_text=''
    if uploaded_file:
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_text = file.read()
        if len(file_text) > 3:

            prediction_file=predict_language(file_text)

    

    
    if len(code_text) > 3:

        prediction_code=predict_language(code_text)

    return jsonify({
        'message': 'Code received',
        'code': code_text,
        'code-prediction':prediction_code,
        'file-prediction':prediction_file,
        'file_path': file_path
    })

if __name__ == '__main__':
    app.run(debug=True)
