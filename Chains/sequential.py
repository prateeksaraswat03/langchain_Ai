from langchain_groq import  ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)
prompt1=PromptTemplate(
    template="generate the detail of report on {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="generate the 5 point of summnary from the following text /n{text}",
    input_variables=['text']
)
parser=StrOutputParser()
chain =prompt1|llm|parser|prompt2|llm|parser
result=chain.invoke({'topic':'unemployement'})
print(result)