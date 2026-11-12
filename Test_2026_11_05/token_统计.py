from langchain_core.callbacks import get_usage_metadata_callback
import os,dotenv
from langchain_openai import ChatOpenAI
dotenv.load_dotenv()

llm = ChatOpenAI (
        model = "deepseek-ai/DeepSeek-V4.1-Flash",
        base_url = os.getenv("GJ_URL"),
        api_key = os.getenv("GJ_API")
)
with get_usage_metadata_callback() as callback:
    llm.invoke("你好")
    llm.invoke("再见")

    print(callback.usage_metadata)
# {
#     'input_tokens': 总输入token数,
#     'output_tokens': 总输出token数,
#     'total_tokens': 总token数
# }