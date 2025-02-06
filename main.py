import os
from typing import TypedDict, Annotated, Sequence


os.environ["DEEPSEEK"] = os.getenv('allenDeepSeek')
os.environ["TAVILY_API_KEY"] = os.getenv('TAVILY_API_KEY')


# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好，你跟openai的关系"},
    ],
    stream=False
)

print(response.choices[0].message.content)