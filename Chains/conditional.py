from langchain_groq import  ChatGroq
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()
llm1 = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)
parser=StrOutputParser()
class feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='Give the sentiment of the feedback')
parser2 = PydanticOutputParser(pydantic_object=feedback)
prompt1=PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
combine_chain=prompt1|llm1|parser2
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2|llm1|parser),
    (lambda x:x.sentiment=='negative',prompt3|llm1|parser),
    RunnableLambda(lambda x: "could not find sentiment")
)
chain = combine_chain | branch_chain

print(chain.invoke({'feedback': 'This is a worst phone'}))