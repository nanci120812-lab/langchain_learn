from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
# 系统 用户 AI 工具
from langchain_openai import ChatOpenAI
import os
import dotenv
dotenv.load_dotenv()
llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4.1-Flash",
    base_url=os.getenv("GJ_URL"),
    api_key=os.getenv("GJ_API"),
)

# 多轮对话
conversation = [
    SystemMessage(content="你是一个情感助手助手"),
    HumanMessage(content="你好，我叫筱莜"),
    AIMessage(content="你好！筱莜,有什么我可以帮助你的吗？"),
    HumanMessage(content="我压力好大"),
]
# 单论对话
resource = llm.invoke([HumanMessage(content=('请用一句话介绍自己'))])
res = llm.invoke(conversation)
# print(resource.content)
# print(res.content)


#使用元组或字典对话
#元组方式：（角色，内容）
tuple_message =[
    ("system",'你是一个情感助手'),
    ('user','教我怎么哄对象')
]
# print(llm.invoke(tuple_message).content)

#字典方式{‘role’:角色,'content':内容}
dict_message = [
    {'role':'system','content':'你是一个健身教练'},
    {'role':'user','content':'帮我介绍一下健身器材100字'}
]
# print(llm.invoke(dict_message).content)

#从配置读取对话模板
prompt_template=[
    {'role':'system','content':'你是一个{role}'},
    {'role':"user",'content':'请解释{topic}'}
]

#动态填充
message =[
    {
        'role':t["role"],
        "content":t["content"].format(
            role ="解释助手",
            topic ="langchain的用处"
        ),
     }
    for t in prompt_template
]
print(llm.invoke(message).content)