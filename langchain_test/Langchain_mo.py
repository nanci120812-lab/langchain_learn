# 第一种对接大模型方式  官方版本直连（不推荐）

# 第二种Langcchain
# （1）第一种 openai 需要安装 langchain_openai,其他模型同样
# import os
# from langchain_openai import ChatOpenAI
# import dotenv

# dotenv.load_dotenv()
#
# LLM_GJ = ChatOpenAI(
#     model="cc",
#     base_url=os.getenv("GJ_URL"),
#     api_key=os.getenv("GJ_API"),
#     temperature=0.7,  # 随机性，0=确定性，1=有创意（默认因模型而异）
#     max_tokens=1000,  # 最大输出长度
#     timeout=60,  # 超时时间（秒）
#     max_retries=2,  # 失败重试次数
# )
#
# print(LLM_GJ.invoke("生成一段自我介绍"))

# 第三种 init
from langchain.chat_models import init_chat_model
import dotenv


dotenv.load_dotenv()
import os

LLM_01 = init_chat_model(
    model="deepseek-ai/DeepSeek-V4-Flash",
    model_provider="openai",
    base_url=os.getenv("GJ_URL"),
    api_key=os.getenv("GJ_API"),
)
LLM_02 = init_chat_model(
    model="deepseek-ai/DeepSeek-V4.1-Flash",
    model_provider="openai",
    base_url=os.getenv("GJ_URL"),
    api_key=os.getenv("GJ_API"),
)#
LLM_03 = init_chat_model(
    model="Qwen/Qwen3.8-27B",
    model_provider="openai",
    base_url=os.getenv("GJ_URL"),
    api_key=os.getenv("GJ_API"),
)
for name, lmm in [("模型01", LLM_01), ("模型02", LLM_02), ("模型03", LLM_03)]:
    response = lmm.invoke("简述一下自己的优点")
    print(f"{name}:{response.content}")


# 1111111111111111111