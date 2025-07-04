import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers = header, json = input_json)

    if response.status_code == 200:
        data = json.loads(response.text)['emotionPredictions'][0]['emotion']
        max_key = max(data, key = data.get)
        data['dominant_emotion'] = max_key

    elif response.status_code == 400:
        data = {'anger' : None, 'disgust' : None, 'fear' : None, 
        'joy' : None, 'sadness' : None, 'dominant_emotion' : None,}

    return data