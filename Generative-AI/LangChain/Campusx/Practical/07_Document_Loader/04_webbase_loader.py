from langchain_community.document_loaders import WebBaseLoader

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
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

url = 'https://docs.langchain.com/'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

chain.invoke({'question': 'what is the langchain', 'text': docs[0].page_content})