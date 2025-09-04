from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
   
def detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return f"Invalid Text! Please Try Again"

    # Extract emotion scores from result
    anger = result.get('anger', 0)
    disgust = result.get('disgust', 0)
    fear = result.get('fear', 0)
    joy = result.get('joy', 0)
    sadness = result.get('sadness', 0)
    dominant_emotion = result.get('dominant_emotion')
    
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def index():
    """Returns html for default index page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)