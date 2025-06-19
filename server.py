''''This module runs a Flask web app that performs emotion analysis on given sentences'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def detect_emotion():
    '''Calls to emotion_detector function to perform analysis and returns the result'''
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    answer = f'''For the given statement, the system response is
    'anger' {result['anger']}, 'disgust' {result['disgust']}, 
    'fear' {result['fear']}, 'joy' {result['joy']} and
    'sadness' {result['sadness']}. The dominant emotion is
    {result['dominant_emotion']}.
    '''
    return answer


@app.route('/')
def index():
    '''returns the index'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
