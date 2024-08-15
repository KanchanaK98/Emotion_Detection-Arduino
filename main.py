from deepface import DeepFace
import cv2
import json

img_path = 'angry_girl.jpg'
img = cv2.imread(img_path)

attributes = ['gender','emotion']

demography = DeepFace.analyze(img_path,attributes)
# type(demography)
# results = json.loads(demography)
demography_data = demography[0].get('dominant_emotion')
print(demography_data)
