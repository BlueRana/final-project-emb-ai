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
    # Return the response text from the API
    return response.text
