# Gradio frontend
import gradio as gr
import requests
import io

# 이미지를 넣어주면 실행해주는 함수
def classify_with_backend(image):
    url = "http://127.0.0.1:8000/classify"
    image_bytes = io.BytesIO() # 객체 일단 만들기 
    image.save(image_bytes, format="PNG") # 일단 PNG로 저장하기 
    image_bytes = image_bytes.getvalue() # 값을 얻어와서 
    response = requests.post(url, files={"file": ("image.png", image_bytes, "image/png")})
    if response.status_code == 200:
        return response.json().get("label", "Error") #라벨을 전달하기 
    else:
        return "Error"

# 화면 그리기 
iface = gr.Interface( # 그라디오의 인터페이스 이용 
    fn=classify_with_backend, # 위의 함수 콜백으로 등록 
    inputs=gr.Image(type="pil"), # 이미지를 입력받을 수 있는 입력 양식, type="pil : 이미지 양식
    outputs="text",
    title="손글씨 도형 분류하기",
    description="○, X, △ 이미지를 넣어주세요 !!"
)
# 모듈로 실행할 게 아니라 얘 자체를 실행할거라서 아래의 코드.
if __name__ == "__main__":
    iface.launch()