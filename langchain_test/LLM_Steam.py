import os,dotenv,asyncio,time
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4.1-Flash",
    temperature=0,
    base_url=os.getenv("GJ_URL"),
    api_key=os.getenv("GJ_API"),
)

# def streaming_exampl():
print("AI...回答")
full_msg = None # 存大模型给我们返回的消息
for i in llm.stream("请写一首不屈于命运的诗,50字"):
    full_msg =i if full_msg is None else full_msg + i
    print(i.content,end="",flush=True)
    time.sleep(1)
print("-----------------------------")
print(f"\n\n完整消息\n{full_msg.content}")

