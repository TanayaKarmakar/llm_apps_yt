from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import argparse
from pprint import pprint
from dotenv import load_dotenv
from sqlalchemy.testing.plugin.plugin_base import start_test_class_outside_fixtures


def add_context_back(input_with_code):
    #print(input_with_code)
    object = {
        "code": input_with_code["code"],
        "code_snippet": input_with_code["code"],
        "language": input_with_code.get("language"),
        "task": input_with_code.get("task")
    }
    print("Object Printing ")
    pprint(object)
    return object
#
# def add_output_context(final_output):
#     print("Output Context: \n")
#     pprint(final_output)
#     return {
#         "code": final_output.get("code"),
#         "test": final_output["test"]
#     }

load_dotenv()
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()


llm = ChatOpenAI()

code_prompt = PromptTemplate(
    template = "Write a very short {language} function that will {task}",
    input_variables= ["language", "task"]
)

test_prompt = PromptTemplate(
    template = "Write a test for the following {language} code:\n{code}",
    input_variables=["language", "code"]
)

code_chain = code_prompt | llm | RunnableLambda(lambda output: {"code": output.content})
test_chain = test_prompt | llm | RunnableLambda(lambda output: {"test": output.content})

chain = (
    RunnableLambda(lambda x: {
        "language": x["language"],
        "task": x["task"]
    }) |
    code_chain |
    RunnableLambda(add_context_back) |
    test_chain |
    RunnableLambda(lambda x: {
        "code": x.get("code_snippet"),
        "language": x.get("language"),
        "test": x["test"]
    })
    # RunnableLambda(add_output_context)
)

result = chain.invoke({
    "language": args.language,
    "task": args.task
})

print("\n\n")
print("Output Printing: \n")
pprint(result)
print("\n")
