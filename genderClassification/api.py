import tensorflow
from tensorflow.keras.models import load_model
from PIL import Image
import requests
from io import BytesIO
from tensorflow.keras.utils import load_img, img_to_array
from skimage import io
from rest_framework.response import Response
from rest_framework.decorators import permission_classes,api_view
from rest_framework.status import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np 
import urllib.request

# cred = credentials.Certificate("/Users/rohitlokhande/Documents/projects/gender-detection/gender-detection/gender_detection_service_key.json")
# firebase_admin.initialize_app(cred)

@api_view(['POST'])
def predictGender(request):
    if request.method == 'POST':
        # img1 = io.imread(request.data['faceImgUrl'])
        try:
         urllib.request.urlretrieve(
        'https://firebasestorage.googleapis.com/v0/b/gender-detection-eb4d9.appspot.com/o/my_model1.h5?alt=media&token=6961f8f3-8639-445d-901d-c13ee8d94b7e', 'model.h5')
         response = requests.get('https://firebasestorage.googleapis.com/v0/b/gender-detection-eb4d9.appspot.com/o/131422.jpg.jpg?alt=media&token=91fc935f-a83b-4779-9016-cd73f2f7dfd0')
         img = Image.open(BytesIO(response.content)).convert("L")
         img = img.resize((50, 50), Image.ANTIALIAS)
         img = img_to_array(img)
         img = np.expand_dims(img, axis=0)
         model = load_model('./model.h5')
         result = model.predict(img)
         print(result[0][0])
         return Response({
            'status': 200,
            'gender':result[0][0]},status=HTTP_200_OK)
        except BaseException as error:
            return Response({
                'status': 500,
                'message': error.args[0]
            },status=HTTP_200_OK)
    return Response({
        'message': 'Bad request',
        'status': 400
    },status=HTTP_400_BAD_REQUEST)

