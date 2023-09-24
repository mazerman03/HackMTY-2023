import os
import pandas as pd
import matplotlib.pyplot as plt
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Load the text from your file (assuming 'fundInversiones.txt' is in the same directory)
with open('HackMTY-2023/datatxt/fundInversiones.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Create function to count tokens (Not needed for ChatGPT 3.5)
def count_tokens(text: str) -> int:
    return len(text.split())  # Just count words

# Split text into chunks (Not needed for ChatGPT 3.5)
try:
    chunks = text.split('\n')  # Split by newline if needed
    print("Number of chunks:", len(chunks))
except IndexError as e:
    print("An IndexError occurred:", e)

# Get embedding model (Not needed for ChatGPT 3.5)
embeddings = OpenAIEmbeddings()

# Create vector database (Not needed for ChatGPT 3.5)
# db = FAISS.from_documents(chunks, embeddings)

# Check similarity search is working (Not needed for ChatGPT 3.5)
# query = "¿Qué es una buena inversión?"
# docs = db.similarity_search(query)
# docs[0]

# Create QA chain to integrate similarity search with user queries (Not needed for ChatGPT 3.5)
# chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

# query = "¿Qué es una buena inversión?"
# docs = db.similarity_search(query)

# chain.run(input_documents=docs, question=query)

# Create conversation chain (Not needed for ChatGPT 3.5)
# qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.1), db.as_retriever())

# Now, you can use ChatGPT 3.5 for interactions
import openai

# Define your question or prompt
prompt = "¿Qué es una buena inversión?"

# Make an API call to ChatGPT 3.5
response = openai.Completion.create(
    engine="davinci",  # Use ChatGPT 3.5's engine
    prompt=prompt,
    max_tokens=150,  # Adjust the maximum response length as needed
)

# Get the response from ChatGPT 3.5
chat_response = response.choices[0].text

# Print or use the response
print(chat_response)
