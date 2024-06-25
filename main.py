import requests 

def emotion_detector(text_to_analyse):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   myobj = {"raw_document": { "text": text_to_analyse } }
   response = requests.post(url, json = myobj, headers = headers)
   return response.text


import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    status_code = response.status_code
    
    if status_code == 400:
        formatted_output = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None }
    else:
        res = json.loads(response.text)
        formatted_output = res[‘emotionPredictions’][0][‘emotion’]
        dominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])
        formatted_response[‘dominant_dictionary’] = dominant_emotion

    return formatted_response



import unittest
from EmotionDetection.emotion_detection import emotion.detector
 
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion.detector(“I am glad this happened”)
        self.assertEqual(result1[‘dominant_emotion’], ’joy’)
        result2 = emotion.detector(“I am really mad about this”)
        self.assertEqual(result2[‘dominant_emotion’], ‘anger’)
        result3 = emotion.detector(“I feel disgusted just hearing about this”)
        self.assertEqual(result3[‘dominant_emotion’], ’ disgust’)
        result4 = emotion.detector(“I am so sad about this”)
        self.assertEqual(result4[‘dominant_emotion’], ’sadness’)
        result5 = emotion.detector(“I am really afraid that this will happen”)
        self.assertEqual(result5[‘dominant_emotion’], ’fear’)

unittest.main()



from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    ''' This function calls the application
    '''
    test_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."

    return response_text

@app.route("\")
def render_index_page():
    ''' This is the function to render the html interface
    '''
    return render_template('index.html')

if _name_ == "_main_":
    app.run(host = "0.0.0.0", port = 5000)
