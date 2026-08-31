from langchain_community.document_loaders import TextLoader

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.7
)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader(r'LangChain\Campusx\Practical\07_Document_Loader\cricket.txt', encoding='utf-8')

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))