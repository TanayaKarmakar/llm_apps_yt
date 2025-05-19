from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

#model = ChatOpenAI()

# 1st Prompt -> Detailed Report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)


# 2nd Prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following \n{text}",
    input_variables=["text"]
)


prompt1 = template1.invoke({
    "topic": "Black Hole"
})

result = model.invoke(prompt1)

prompt2 = template2.invoke({
    "text": result.content
})

final_result = model.invoke(prompt2)

print(final_result.content)