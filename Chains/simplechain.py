from langchain_groq import  ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
 
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)
prompt=PromptTemplate(
    template='give me 5 intersting facts about {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()
chain=prompt|llm|parser
result=chain.invoke({'topic':'Ai'})
print(result)
chain.get_graph().print_ascii()