from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r'LangChain\Campusx\Practical\07_Document_Loader\Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[0])