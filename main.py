from deepface import DeepFace
import cv2
import time
import controller as cnt

time.sleep(2.0)

img_path = 'smile_girl.jpg'
img = cv2.imread(img_path)

attributes = ['gender','emotion']

demography = DeepFace.analyze(img_path,attributes)
demography_data = demography[0].get('dominant_emotion')

print(demography_data)

if demography_data == 'happy':
    cnt.led('happy')
elif demography_data == 'angry':
    cnt.led('angry')
elif demography_data == 'neutral':
    cnt.led('neutral')
elif demography_data == 'surprise':
    cnt.led('surprise')
else:
    cnt.led('other')
