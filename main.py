# ---------------
#    LIBRERIAS
# ---------------

import os
import pandas as pd
import matplotlib.pyplot as plt
from transformers import GPT2TokenizerFast
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

# ---------------
#     API KEY
# ---------------

os.environ["OPENAI_API_KEY"] = "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"

# ---------------
#     OPEN TXT
# ---------------
# Step 2: Save to .txt and reopen (helps prevent issues)

with open('datatxt/compilation.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Step 3: Create function to count tokens
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text))

# Step 4: Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 512,
    chunk_overlap  = 48,
    length_function = count_tokens,
)

chunks = text_splitter.create_documents([text])
 

# Result is many LangChain 'Documents' around 500 tokens or less (Recursive splitter sometimes allows more tokens to retain context)
type(chunks[0]) 

# Quick data visualization to ensure chunking was successful

""" # Create a list of token counts
token_counts = [count_tokens(chunk.page_content) for chunk in chunks]

# Create a DataFrame from the token counts
df = pd.DataFrame({'Token Count': token_counts})

# Create a histogram of the token count distribution
df.hist(bins=40, )

# Show the plot
plt.show() """

# Get embedding model
embeddings = OpenAIEmbeddings()

# Create vector database
db = FAISS.from_documents(chunks, embeddings)


# --------------------------
#      INICIA EL CHATBOT
# --------------------------
# Check similarity search is working
print("BenIA: ¡Hola! Soy BenIA, tu coach personal de inversión, puedes hacerme preguntas, consultas y aprender de mí. ¿Cómo puedo ayudarte?")


run = True
while run:
    query = input("User: ")
    docs = db.similarity_search(query)
    docs[0]

    # Create QA chain to integrate similarity search with user queries (answer query from knowledge base)

    chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
    response = chain.run(input_documents=docs, question=query)
    print("BenIA: ",response)
    from IPython.display import display
    import ipywidgets as widgets

    # Create conversation chain that uses our vectordb as retriver, this also allows for chat history management
    qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.1), db.as_retriever())

    if "adiós" in query.lower() or "adios" in query.lower():
        print(">> Gracias por consultar a BenIA, ¡nos vemos pronto!")
        run = False
        

chat_history = []

"""
def on_submit(_):
    query = input_box.value
    input_box.value = ""
    
    if query.lower() == 'exit':
        print("Gracias por usar BenIA, nos vemos pronto!")
        return
    
    result = qa({"question": query, "chat_history": chat_history})
    chat_history.append((query, result['answer']))
    
    display(widgets.HTML(f'<b>User:</b> {query}'))
    display(widgets.HTML(f'<b><font color="blue">Chatbot:</font></b> {result["answer"]}'))

print("Welcome to the Transformers chatbot! Type 'exit' to stop.")

input_box = widgets.Text(placeholder='Please enter your question:')
input_box.on_submit(on_submit)

display(input_box) """


# ----------------------------------
#   POSSIBLE FLASK IMPLEMENTATION
# ----------------------------------

""" from flask import Flask, render_template, request

app = Flask(__name__)

# Your chatbot code here
def generate_chat_response(user_input):
    # Replace this with your chatbot logic to generate a response based on user_input
    # Example:
    chatbot_response = f"You asked: {user_input}. This is a sample response."
    return chatbot_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    chatbot_response = generate_chat_response(user_input)
    return render_template('index.html', user_input=user_input, chatbot_response=chatbot_response)

if __name__ == '__main__':
    app.run(debug=True) """