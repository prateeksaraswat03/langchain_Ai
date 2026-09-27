from langchain_groq import  ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)
def word_count(text):
    return len(text.split())

parser=StrOutputParser()
prompt=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_of_gen=RunnableSequence(prompt,llm,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'count':RunnableLambda(word_count)

})
chain=RunnableSequence(joke_of_gen,parallel_chain)
result=chain.invoke({'topic':'llm'})
print(result)