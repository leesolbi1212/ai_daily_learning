# FastAPI backend
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import torch
from torchvision import transforms
from PIL import Image
import io
import torch.nn as nn
import torch.nn.functional as F
class ConvNeuralNetwork(nn.Module):
    def __init__(self):
        super(ConvNeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.classifier = nn.Sequential(
            nn.Conv2d(1, 28, kernel_size=3, padding='same'),
            nn.ReLU(),

            nn.Conv2d(28, 28, kernel_size=3, padding='same'),
            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2),
            nn.Dropout(0.25),

            nn.Conv2d(28, 56, kernel_size=3, padding='same'),
            nn.ReLU(),

            nn.Conv2d(56, 56, kernel_size=3, padding='same'), # (56, 14, 14)
            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2), # (56, 7, 7)
            nn.Dropout(0.25),
        )
        self.Linear = nn.Linear(56 * 7 * 7, 3)
    
    def forward(self, x):
        x = self.classifier(x)
        x = self.flatten(x)
        output = self.Linear(x)
        return output
    
model = ConvNeuralNetwork()
state_dict = torch.load('./model_weights.pth', map_location=torch.device('cpu'))
model.load_state_dict(state_dict)
model.eval() 