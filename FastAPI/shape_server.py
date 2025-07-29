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

# 클래스 3가지 있다. 라고 저장해두기 
CLASSES = ['cir', 'tri', 'x']

def preprocess_image(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.Grayscale(1),
        transforms.ToTensor(),
        transforms.RandomInvert(1),
        transforms.Normalize((0.5), (0.5))
    ])
    # io.BytesIO : 웹에서 입력받은 이미지를 바이너리 이미지 데이터로 처리하고, 파일처럼 다룰 수 있게 가상 메모리 객체로 변환 (디스크에 저장하지 않아도, 메모리에서 이미지를 읽어서 쓸 수 있게 해줌)
    # convert('L') : 이미지 색상 모드를 변경, L : 그레이스케일 
    image = Image.open(io.BytesIO(image_bytes)).convert('L')
    return transform(image).unsqueeze(0)

app = FastAPI()

# CORS 문제 해결하는 코드 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.post("/classify")
# 비동기 함수가 동작하게 되는 코드 
async def classify_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        print(f"Received file: {file.filename}, size: {len(image_bytes)} bytes")
        
        input_tensor = preprocess_image(image_bytes)
        print(f"input tensor shape: {input_tensor.shape}")
        
        with torch.no_grad(): #torch.no_grad() : test 모드라는 것 
            outputs = model(input_tensor)
            print(f"Model outputs: {outputs}")
            
            _, predicted = torch.max(outputs, 1) # 예측에서 가장 큰 인덱스 값을 전달받는다. 
            label = CLASSES[predicted.item()]
            print(f"Predicted label: {label}") # 결과 나오는 라벨을 얻어서 
        
        return JSONResponse(content={"label": label}) # JSON 형태로 바꿔준다. 
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
    # 서버 실행하는 애 
    # uvicorn shape_server:app --reload