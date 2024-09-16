from flask import Flask, render_template, request
import tensorflow
from tensorflow.keras.models import load_model   #type:ignore
import cv2
import numpy as np

app = Flask(__name__)

# Loading the ESRGAN model
try:
    ESRGAN_model = tensorflow.saved_model.load('Models/ESRGAN_Model')
except Exception as e:
    print('Error loading ESRGAN model.\n', e)

# Loading the CNN model
try:
    CNN_model = load_model('Models/CNN_Model.h5')
except Exception as e:
    print('Error loading CNN model.\n', e)


# Setting the mapping of 43 classes of GTSRB dataset
classes = {
    0: 'Speed Limit (20 km/h)',
    1: 'Speed Limit (30 km/h)',
    2: 'Speed Limit (50 km/h)',
    3: 'Speed Limit (60 km/h)',
    4: 'Speed Limit (70 km/h)',
    5: 'Speed Limit (80 km/h)',
    6: 'End of Speed Limit (80 km/h)',
    7: 'Speed Limit (100 km/h)',
    8: 'Speed Limit (120 km/h)',
    9: 'No Passing',
    10: 'No Passing for Vehicles over 3.5 metric tons',
    11: 'Right-of-way at the next intersection',
    12: 'Priority Road',
    13: 'Yield',
    14: 'Stop',
    15: 'No Vehicles',
    16: 'Vehicles over 3.5 metric tons prohibited',
    17: 'No Entry',
    18: 'General Caution',
    19: 'Dangerous Curve to the left',
    20: 'Dangerous Curve to the right',
    21: 'Double Curve',
    22: 'Bumpy Road',
    23: 'Slippery Road',
    24: 'Road Narrows on the Right',
    25: 'Road Work',
    26: 'Traffic Signals',
    27: 'Pedestrians',
    28: 'Children Crossing',
    29: 'Bicycles Crossing',
    30: 'Beware of Ice/Snow',
    31: 'Wild Animals Crossing',
    32: 'End of all speed and passing limits',
    33: 'Turn right ahead',
    34: 'Turn left ahead',
    35: 'Ahead only',
    36: 'Go straight or right',
    37: 'Go straight or left',
    38: 'Keep right',
    39: 'Keep left',
    40: 'Roundabout mandatory',
    41: 'End of no passing',
    42: 'End of no passing by vehicles over 3.5 metric tons'
}

# Load and preprocess a single test image
def preprocess_test_image(image):
    resized_image = tensorflow.image.resize(image, [128, 128], method=tensorflow.image.ResizeMethod.BICUBIC)
    normalized_image = resized_image / 255.0
    return normalized_image

# Defining a function to apply ESRGAN model to enhance the quality of images
def enhance_images(images):
    images = images * 2.0 - 1.0  # Rescale the entire batch to [-1, 1]
    enhanced_images = ESRGAN_model(images)  # Enhance the batch
    enhanced_images = (enhanced_images + 1.0) / 2.0  # Rescale back to [0, 1]
    enhanced_images = np.clip(enhanced_images, 0, 1)  # Clip values to [0, 1]
    return enhanced_images

# Load and enhance the test image
def enhance_test_image(image):
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    enhanced_image = enhance_images(image)  # Apply ESRGAN
    enhanced_image = np.squeeze(enhanced_image, axis=0)  # Remove batch dimension
    return enhanced_image

        
# Creating routes
@app.route('/')
def index():
    return render_template('index.html', data='hey')

@app.route('/prediction', methods=['post'])
def prediction():
    img = request.files['img']
    img.save('img.jpg')

    test_image = cv2.imread('img.jpg')
    image = preprocess_test_image(test_image)
    enhanced_image = enhance_test_image(image)
    test_image = (enhanced_image * 255).astype(np.uint8)
    test_image = cv2.resize(test_image, (128, 128)) / 255.0

    # Use CNN model to classify the enhanced image
    test_image = np.expand_dims(test_image, axis=0)
    pred = CNN_model.predict(test_image)
    pred = np.argmax(pred)
    pred = classes[pred]

    return render_template('prediction.html', data=pred)

if __name__ == '__main__':
    app.run(debug=True)