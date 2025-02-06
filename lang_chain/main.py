import os

from langchain_core.messages import HumanMessage
from openai import OpenAI
from langchain_openai import ChatOpenAI
api_key = os.getenv('allenDeepSeek')
client = OpenAI(api_key=os.getenv('allenDeepSeek'), base_url="https://api.deepseek.com")

chat = ChatOpenAI(model="deepseek-chat",api_key=api_key, base_url="https://api.deepseek.com")
# 替换为您的深度求索API密钥


# 导入LangChain中的提示模板
# 创建原始模板
template = "hello"

# 使用 PromptTemplate 生成描述
# 使用 invoke 方法进行对话

print(chat.invoke([HumanMessage(content="Hi! I'm Bob")]))