from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
When you run the code and prompt the agent to tell you about the weather in San Francisco, the agent uses that input and its available context. The agent understands that you are asking about the weather for the city San Francisco and therefore calls the weather tool with the provided city name.

In the following example you will build a research agent that can answer questions about text files. Along the way you will explore the following concepts:
Detailed system prompts for better agent behavior
Create tools that integrate with external data
Model configuration for consistent responses
Conversational memory for chat-like interactions
Deep Agents for built-in features
Testing your agent
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)