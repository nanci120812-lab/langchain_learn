import base64,dotenv,os
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
llm = ChatOpenAI (
        model = "deepseek-ai/DeepSeek-V4.1-Flash",
        base_url = os.getenv("GJ_URL"),
        api_key = os.getenv("GJ_API")
)

with open("e9b77f373e23cab57e067ce1adc25a7e.jpg", "rb") as f:
        image_data =f.read()

message = HumanMessage(content=[
        {"type": "text","text":'描述这张图片'},
        {"type": "image_url","image_url":{"url":f"data:image/jpg;base64,{base64.b64encode(image_data).decode()}"}}
])

response =llm.invoke([message])
print(response.content)
