from langchain_groq import  ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

loader=TextLoader(r"C:\Users\HP840G6\OneDrive\Desktop\langchain\Rag\story.txt")
doc=loader.load()
print(doc[0].page_content)


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)
parser=StrOutputParser()
prompt=PromptTemplate(
    template='genearte the  7 line summary of following story\n {story}',
    input_variables=['story']
)
chain=prompt|llm|parser
result=chain.invoke({'story':doc[0].page_content})
print(result)
