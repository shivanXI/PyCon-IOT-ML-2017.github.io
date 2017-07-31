import picamera
import time
import io

from google.cloud import vision
from google.cloud import language

camera = picamera.PiCamera()
camera.capture('123.jpg')

camera.vflip = True

camera.capture('1234.jpg')

camera.start_recording('123vid.h264')
time.sleep(6)
camera.stop_recording()



vision_client = vision.Client()
file_name = '123.png'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )

labels = image.detect_labels()
print("for image 1")
for label in labels:
    print(label.description)


file_name = '1234.png'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )

labels = image.detect_labels()
print("for image 1")
for label in labels:
    print(label.description)


# sentiment analysis module for the audio test 

'''
def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment, entities


example_text = 'This is a test, this audio will be taken from the pi and it will be awesome'
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)
for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)

'''