from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import os
import matplotlib.pyplot as plt
import tensorflow_hub as hub
from data.style import *
# Load compressed models from tensorflow_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
style_path = tf.keras.utils.get_file('kandinsky5.jpg','https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg')
style_image = load_img(style_path)

input_shape = (224,224)
max_dim = 512

model = None

def load_model():
    #model = tf.keras.applications.MobileNetV2(weights="imagenet")
    model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    return model

def predict(image: np.ndarray):
    global model
    if model is None:
        model = load_model()
    stylized_image = model(tf.constant(image), tf.constant(style_image))[0]
    stylized_image =  tensor_to_image(stylized_image)
    return stylized_image

def read_image(image_encoded):
    img = Image.open(BytesIO(image_encoded))
    img  = tf.keras.preprocessing.image.img_to_array(img)
    img = img/255
    img = tf.image.convert_image_dtype(img, tf.float32)
    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = max(shape)
    
    scale = max_dim / long_dim

    new_shape = tf.cast(shape * scale, tf.int32)

    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]
    
    return img

def preprocess(image: Image.Image):
    image = image.resize(input_shape)
    image = np.asfarray(image)
    image = image / 127.5 - 1.0
    image = np.expand_dims(image, 0)
    
    return image


