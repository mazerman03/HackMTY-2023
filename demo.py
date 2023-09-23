# pip install openai
# pip install gradio
# pip install langchain
# pip install faiss-cpu
# pip install llama_index

import os 
os.environ["OPEN_API_KEY"] = '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'

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('AQUI VA LA KNOWLEDGE BASE ').load_data()

index = GPTVectorStoreIndex.from_documents(documents)

index.storage_context.persist('AQUI VA DONDE GUARDAMOS EL INDEX')

from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
storage_context = StorageContext.from_defaults
(persist_dir='AQUI VA DONDE GUARSAMOS EL INDEX')
# load index
index = load_index_from_storage(storage_context)

# Chat Bot

import openai
import json

class Chatbot:
    def __init__(self, api_key, index):
        self.index = index
        openai.api_key = api_key
        self.chat_history = []

    def generate_response(self, user_input):
        prompt = "\n".join([f"{message['role']}: {message['content']}" 
                           for message in self.chat_history[-5:]])
        prompt += f"\nUser: {user_input}"
        query_engine = index.as_query_engine()
        response = query_engine.query(user_input)

        message = {"role": "assistant", "content": response.response}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message

    def load_chat_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f)