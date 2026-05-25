from flask import Flask,render_template,request
import os

from ocr import extract_text
from summarizer import generate_summary

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():

    file = request.files['image']

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    # OCR
    extracted_text = extract_text(filepath)

    # SUMMARY
    summary = generate_summary(extracted_text)

    return render_template(
        'result.html',
        extracted_text=extracted_text,
        summary=summary
    )

if __name__ == '__main__':
    print("Starting Flask App...")
    app.run(host='0.0.0.0', port=5000, debug=True)