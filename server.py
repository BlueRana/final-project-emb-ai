"""
This module implements a Flask server that exposes two routes:
- "/" : Serves the home page with an input form.
- "/emotionDetector" : Accepts text input via query parameters, 
  calls the Watson Emotion Detection API through the emotion_detector function,
  and returns the detected emotion scores and dominant emotion.

Error handling is incorporated to handle invalid or blank inputs gracefully, 
returning an appropriate message when no dominant emotion is detected.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    """
    Flask route handler for '/emotionDetector'.

    Retrieves the 'textToAnalyze' query parameter from the request,
    calls the emotion_detector function to analyze the emotion of the input text,
    and returns a formatted string displaying the emotion scores and dominant emotion.

    If the input text is invalid or no dominant emotion is detected, 
    returns an error message prompting the user to try again.

    This function is designed to work within the cloud-ide-kubernetes environment 
    as part of the Developing AI Applications with Python and Flask course.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return "Invalid Text! Please Try Again", 400

    # Extract emotion scores from result
    anger = result.get('anger', 0)
    disgust = result.get('disgust', 0)
    fear = result.get('fear', 0)
    joy = result.get('joy', 0)
    sadness = result.get('sadness', 0)
    dominant_emotion = result.get('dominant_emotion')
    # Returns each emotion, thier score amd domiinant emotion
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
