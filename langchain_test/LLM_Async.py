# import asyncio
# from langchain_openai import ChatOpenAI
# import os
# import dotenv
# dotenv.load_dotenv()
#
# llm = ChatOpenAI(
#     model="deepseek-ai/DeepSeek-V4.1-Flash",
#     base_url=os.getenv('GJ_URL'),
#     api_key=os.getenv('GJ_API'),
# )
#
# async def call_llm_async():
#     res = await llm.ainvoke("如何委婉表达感情")
#     print(res.content)
# asyncio.run(call_llm_async())

import time
import asyncio
import os
import dotenv
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4.1-Flash",
    base_url=os.getenv("GJ_URL"),
    api_key =os.getenv("GJ_API"),
)

#准备三个测试问题
prompts =[
    "一句话证明自己在某个领域的用处",
    '一句话证明自己比别人优秀',
    '一句话证明自己足够自信'
]

#============测试一：同步调用 invoke（串行）================
def test_sync_invoke():
    print("===同步 invoke ===")
    start_time = time.time()

    for i, prompt in enumerate(prompts):
        print(f"[同步]正在发送{i+1}个请求。。。")
        res = llm.invoke(prompt).content
        print(res)
    print(f"总耗时：{time.time()-start_time:.2f} 秒\n")
#test_sync_invoke()

#=============测试二：异步调用 ainvoke（并行）================
async def test_async_ainvoke():
    print("===异步 ainvoke ===")
    start_time = time.time()
    print("【异步】瞬间派发三个请求。。。")
    takes = [llm.ainvoke(prompt) for prompt in prompts]
    results = await asyncio.gather(*takes)

    for r in results:
        print(f"回答：{r.content}...")
    print(f"总耗时：{time.time()-start_time}")
# asyncio.run(test_async_ainvoke())

#=========运行对比==========
async def main():
    test_sync_invoke()
    await   test_async_ainvoke()
asyncio.run(main())