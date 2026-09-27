from langchain_groq import  ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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
prompt1=template1.invoke({'topic':'black hole'})

result=llm.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})

result1=llm.invoke(prompt2)

print(result1.content)