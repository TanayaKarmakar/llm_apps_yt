from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('files/deep_learning_course_curriculum.pdf')

docs = loader.load()

print(docs)