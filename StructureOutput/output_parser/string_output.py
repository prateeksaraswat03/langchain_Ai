from langchain_groq import  ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
 
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)
template1=PromptTemplate(
    template="write a detail report on {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="write a 5 line summary of  follow report  on text./{text}",
    input_variables=['text']
)
parser=StrOutputParser()
chain=template1|llm|parser|template2|llm|parser
result=chain.invoke({'topic':'black hole'})
print(result)