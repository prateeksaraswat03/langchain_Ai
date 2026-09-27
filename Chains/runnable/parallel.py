from langchain_groq import  ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence

load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)
parser=StrOutputParser()
prompt1=PromptTemplate(
    template='generate  a tweet  about {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='generate the linkdin post about {topic}',
    input_variables=['topic']
)
parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt2,llm,parser),
    'linkdin':RunnableSequence(prompt2,llm,parser)
})
result=parallel_chain.invoke({'topic':"Ai"})
print(result['tweet'])
print(result['linkdin'])