import json
import requests

# Define a function named emtion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):
    """
    Analyze the given text to detect emotions using the Watson NLP Emotion Detection service.

    Args:
        text_to_analyze (str): The input text string to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores for anger, disgust, fear, joy, sadness,
              and the dominant emotion as a string.
    """
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header) 
 
    emotions = {}
    #Check if status code of response if OK
    if response.status_code == 200:
        # If successful, parse the JSON response
        response_dict = response.json() 
        # Extract the required set of emotions
        emotions =response_dict["emotionPredictions"][0]["emotion"]
        #Can combine top to lines to be:
         #emotions = response.json()["emotionPredictions"][0]["emotion"]
      
        # Find the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotions, key=emotions.get)
    
        # Add dominant emotion to the dictionary
        emotions['dominant_emotion'] = dominant_emotion
   
    elif response.status_code == 400:
        # Return dictionary with None values for all emotions and dominant_emotion
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return emotions
