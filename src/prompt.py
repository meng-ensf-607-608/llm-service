from langchain_core.prompts import ChatPromptTemplate

def create_prompt(template):
    return ChatPromptTemplate.from_template(template)
