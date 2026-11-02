import os,dotenv
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI

def batch_example():
    llm = ChatOpenAI(
        model="deepseek-ai/DeepSeek-V4.1-Flash",
        base_url=os.getenv("GJ_URL"),
        api_key=os.getenv("GJ_API")
    )
    questions =[
        "十个字介绍一下自己",
        "为什么发展趋向在朝ai发展",
        "ai工程师后续就业发展如何"
    ]
    res = llm.batch(questions)
    for i,j in zip(questions,res):
        print(f"i: {i}")
        print(f"j: {j.content}")
batch_example()
