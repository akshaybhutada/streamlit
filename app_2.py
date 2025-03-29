from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import requests
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import openai
import streamlit as st



groq_api_key=os.getenv("GROQ_API_KEY")

load_dotenv()
model=ChatGroq(model="llama3-70b-8192",groq_api_key=groq_api_key)
memory = ConversationBufferMemory()


chatbot = ConversationChain(llm=model, memory=memory)

st.title("🤖 AI Chatbot with LangChain & Groq")
st.write("Ask me anything")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.text_input("What question you have in mind?")

response = chatbot.run(user_input)
st.session_state.messages.append({"role": "user", "content": user_input})
st.session_state.messages.append({"role": "assistant", "content": response})

# Display chatbot response
with st.chat_message("assistant"):
    st.markdown(response)
