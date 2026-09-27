

from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    r"C:\Users\HP840G6\OneDrive\Desktop\langchain\Rag\story.txt"
)

docs = loader.load()
print(docs)
import os
from langchain_community.document_loaders import TextLoader

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "story.txt")

print(file_path)
print(os.path.exists(file_path))

loader = TextLoader(file_path)
docs = loader.load()

print(docs[0].page_content)


