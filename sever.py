from flask import Fllask, render_template,request
from EmotionDetection.emotion_detection import emotion_detector

add = Flask("Emotion Detector")

@app.route("/emotionDetector")
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows emotions, each emotion 
        score and thedominat emotion for the provided text.
    '''
def detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    result= emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return f"Invalid Text! Please Try Again"
    return f"For the given statement, the system response is " \
       f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
       f"'joy': {joy}, and 'sadness': {sadness}."\
       f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def index():
    """Returns html for default index page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")