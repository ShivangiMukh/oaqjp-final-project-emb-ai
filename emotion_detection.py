import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    response_text = json.loads(response.text)
    emotion_output = response_text["emotionPredictions"][0]["emotion"]
    anger_score = emotion_output["anger"]
    disgust_score = emotion_output["disgust"]
    fear_score = emotion_output["fear"]
    joy_score = emotion_output["joy"]
    sadness_score = emotion_output["sadness"]
    emotions = {"anger": anger_score, "disgust": disgust_score, "fear": fear_score, "joy": joy_score, "sadness": sadness_score}
    dominant_emotion = max(emotions, key=emotions.get)
    return {"anger": anger_score, "disgust": disgust_score, "fear": fear_score, "joy": joy_score, "sadness": sadness_score, "dominant_emotion": dominant_emotion}
