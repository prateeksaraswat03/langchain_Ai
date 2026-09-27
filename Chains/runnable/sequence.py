from langchain_groq import  ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)
parser=StrOutputParser()
prompt=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)
chain=RunnableSequence(prompt,llm,parser)
result=chain.invoke({'topic':'llm'})
print(result)
