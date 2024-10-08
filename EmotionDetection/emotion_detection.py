import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    print(formatted_response)
    print(response.status_code)
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        max_key = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = max_key
        return emotions  
    elif response.status_code == 400:
        return {'dominant_emotion': None, "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None}
    elif response.status_code == 500:
        return {'dominant_emotion': None, "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None}
      
