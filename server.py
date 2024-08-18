"""
This module sets up a Flask application for sentiment analysis using the emotion detector.
It defines two routes:
- /emotionDetector: Analyzes the sentiment of provided text.
- /: Renders the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the sentiment of the provided text and returns the dominant emotion.
    
    Returns:
        str: The dominant emotion or an error message if the text is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    
    return response

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    
    Returns:
        str: Rendered HTML for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
