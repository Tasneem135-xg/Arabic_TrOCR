from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import VisionEncoderDecoderProcessor, VisionEncoderDecoderModel
import torch
from django.conf import settings
from . import urls

class TrocrEndpoint(APIView):
    def post(self, request):
        processor = VisionEncoderDecoderProcessor.from_pretrained("C:/Users/lenovo/Desktop/trocr - Copy/processor")
        model = VisionEncoderDecoderModel.from_pretrained("C:/Users/lenovo/Desktop/trocr - Copy/model/checkpoint-560")
        model.eval()  # Set the model to evaluation mode

        image = request.FILES.get('image')  # Assuming the image is sent as a file
        pixel_values = processor.feature_extractor(images=image, return_tensors="pt").pixel_values
        
        with torch.no_grad():
            outputs = model(image_features=pixel_values)
            predicted_text = processor.feature_extractor.decode(outputs.logits.argmax(-1)[0], skip_special_tokens=True)
            
        return Response({'predicted_text': predicted_text}, status=status.HTTP_200_OK)
