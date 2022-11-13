import torch
import torchvision
import torchvision.models as models
import sys
import cv2
import numpy as np
import requests
import json




if __name__ == '__main__':
    # print(cv2.__version__)

    onnx_model_path = './model'

    ############################ model conversion and saved as onnx_model_path variable. For simplification purposes, I’ll use a pre-trained one (Densenet 121).

    # https://pytorch.org/hub/pytorch_vision_densenet/
    # model = torch.hub.load('pytorch/vision:v0.6.0', 'densenet121', weights='DenseNet121_Weights.IMAGENET1K_V1')

    # set the model to inference mode
    # model.eval()
    '''
    # Create some sample input in the shape this model expects
    # This is needed because the convertion forward pass the network once
    dummy_input = torch.randn(1, 3, 224, 224)
    torch.onnx.export(model, dummy_input, onnx_model_path, verbose=True)

    '''
    ################################################test the  converted model by loading it with OpenCV

    sample_image = "sample_image.jpeg"

    # The Magic:
    net = cv2.dnn.readNetFromONNX(onnx_model_path)
    image = cv2.imread(sample_image)
    blob = cv2.dnn.blobFromImage(image, 1.0 / 255, (224, 224), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    preds = net.forward()
    biggest_pred_index = np.array(preds)[0].argmax()
    print("Predicted class:", biggest_pred_index)

    f = open('labels.json')
    labels = json.load(f)
    print(labels[biggest_pred_index])
    f.close()


