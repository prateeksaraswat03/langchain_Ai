from langchain_groq import  ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)
parser=StrOutputParser()
prompt1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template=' Summarize the following text \n {text}',
    input_variables=['text']
)
detail_chain=RunnableSequence(prompt1,llm,parser)
branch_chain=RunnableBranch(
    (lambda x: len(x.split())>500, prompt2 | llm | parser),
    RunnablePassthrough()
)
chain=RunnableSequence(detail_chain,branch_chain)
result=chain.invoke({'topic':'AI'})
print(result)
