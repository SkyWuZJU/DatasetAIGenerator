# Return False if the prompt generated is not valid
import os
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = "https://xiaoma-openai.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "44a43d50221443c690df1c2fd0f9cc14"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"

import prompt_templates
from langchain.prompts import PromptTemplate
from langchain.chat_models import azure_openai
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# 处理结果是否需要第三种——重新生成？还是说默认不通过的都会重新生成？个人偏向后者

# 没有新增任何信息或条件的指令
TEMPERTATURE = 0
def is_not_equal(prompt, evolved_prompt):
    judgement_prompt = PromptTemplate(
        input_variables=['FirstPrompt', 'SecondPrompt'],
        template = prompt_templates.equal_judger
    )
    llm = azure_openai.AzureChatOpenAI(
        deployment_name = 'turbo35',
        temperature = TEMPERTATURE,
    )
    judgement_outcome = llm([HumanMessage(content = judgement_prompt.format(FirstPrompt=prompt, SecondPrompt=evolved_prompt))]).content
    if judgement_outcome == "Not Equal" or judgement_outcome == "Not Equal.":
        return True
    elif judgement_outcome == "Equal" or judgement_outcome == "Equal.":
        return False
    ## 补充else的情况

def callback_test():
    print("Rejudge the prompt!")

# print(is_not_equal("1+1=?", "Hello what is your name", callback_test)) #测试用


# 非法关键词过滤，如果生成的指令中包含非法关键词，则返回False
# def is_legal(prompt, callback):

# 生成失败，如生成的内容是乱码、空的等，返回False
# def is_generated(prompt, callback):


def prompt_filter(prompt, evolved_prompt):
    # 总共有三种处理结果：通过、不通过、重新生成
    if is_not_equal(prompt, evolved_prompt) : #如果三个条件都满足，则返回True
        return True
# print(prompt_filter("1+1=?", "Hello what is your name")) #测试用