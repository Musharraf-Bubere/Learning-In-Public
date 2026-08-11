# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from typing import TypedDict, Annotated, Optional, Literal
# from pydantic import BaseModel, Field

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id='deepseek-ai/DeepSeek-V4-Flash-0731',
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# # Schema
# class Review(BaseModel):

#     key_themes: list[str] = Field(description= "Write down all the key themes descussed in the review in a list")
#     summary: str = Field(description= "A brief summary of the review")
#     sentiment: Literal["pos", "neg"] = Field(description= "Return sentiment of the review either negative, positive or neutral")
#     pros: Optional[list[str]] = Field(default=None, description= "Write down all the pros inside a list")
#     cons: Optional[list[str]] = Field(default=None, description= "Write down all the cons inside a list")
#     name: Optional[str] = Field(default=None, description= "Write the name of the reviewer")

# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke(""" I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful

# Cons:
# Bulky and heavy—not great for one-handed use
# Bloatware still exists in One UI
# Expensive compared to competitors""")

# print(result)




from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv 
from typing import Optional, Literal 
from pydantic import BaseModel, Field 

load_dotenv() 

# 1. Initialize the Endpoint and Chat Wrapper
llm = HuggingFaceEndpoint( 
    repo_id='deepseek-ai/DeepSeek-V4-Flash-0731', 
    task="text-generation" 
) 
model = ChatHuggingFace(llm=llm) 

# 2. Define your exact Pydantic Schema
class Review(BaseModel): 
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list") 
    summary: str = Field(description="A brief summary of the review") 
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="Return sentiment of the review either pos, neg, or neutral") 
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list") 
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list") 
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer") 

# 3. Create a strict Pydantic Output Parser
parser = PydanticOutputParser(pydantic_object=Review)

# 4. Construct a prompt template containing exact format instructions
prompt = PromptTemplate(
    template="Analyze the following product review closely and extract structured metadata.\n\n{format_instructions}\n\nReview Content:\n{query}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 5. Build a LangChain Expression Language (LCEL) chain
chain = prompt | model | parser

# 6. Fire your input text into the parsing chain
review_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow. Pros: Insanely powerful processor (great for gaming and productivity) Stunning 200MP camera with incredible zoom capabilities Long battery life with fast charging S-Pen support is unique and useful Cons: Bulky and heavy—not great for one-handed use Bloatware still exists in One UI Expensive compared to competitors
"""

# Invoke the structured processing chain
result = chain.invoke({"query": review_text})

# Print the cleanly generated Pydantic object
print(result)

# Confirm object access works via standard dot notation
print("\n--- Individual Field Output ---")
print(f"Sentiment: {result.sentiment}")
print(f"Summary: {result.summary}")