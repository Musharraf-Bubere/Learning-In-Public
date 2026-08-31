from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r'LangChain\Campusx\Practical\07_Document_Loader\books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))

