from flask import Flask, request, jsonify, render_template
from fake_news_model.model import predict as predict_fake_news
from deepfake_model.detect import detect_deepfake

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/fake-news', methods=['POST'])
def detect_fake_news():
    data = request.json
    text = data.get('text', '')
    result = predict_fake_news(text)
    return jsonify(result)

@app.route('/api/deepfake', methods=['POST'])
def detect_deepfake_api():
    data = request.json
    video_path = data.get('video_path', '')
    result = detect_deepfake(video_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
