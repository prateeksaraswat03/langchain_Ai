from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(r'C:\Users\HP840G6\OneDrive\Desktop\langchain\Rag\loader\dl-curriculum.pdf')
docs = loader.load()

print(docs[0].page_content)
