import cv2
import numpy as np
from keras.models import model_from_json
import os

class PlantModel():
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'model_json.json'), 'r') as f:
            line = f.read()
            self.model = model_from_json(line)
        self.model.load_weights(os.path.join(os.path.dirname(os.path.realpath(__file__)),'model.h5'))
        self.model.make_predict_function()

    def result(self, image):
        img = cv2.imdecode(np.frombuffer(image, np.uint8), -1)
        image = cv2.resize(img, (256,256))
        img1 = cv2.resize(img, (800, 600))
        cv2.imwrite(os.path.join(os.path.dirname(os.path.realpath(__file__)),'static/images/plant_img.jpg'),img1)
        ajay = image[np.newaxis,:]
        res = self.model.predict(ajay)
        dieses = ['Healthy', 'Multiple Diseases', 'Rust', 'Scab']
        return dieses[np.argmax(res)]
         