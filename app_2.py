import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq

# --- UI Header ---
st.title("🤖 AI Chatbot with LangChain & Groq")
st.write("Ask me anything")

# --- Step 1: Ask for API Key ---
groq_api_key = st.text_input(
    "🔑 Enter your GROQ API Key:", 
    type="password", 
    help="We don’t store your key. It's used only in this session."
)

# --- Step 2: Initialize Chatbot (if key is provided) ---
if groq_api_key:
    model = ChatGroq(model="llama3-70b-8192", groq_api_key=groq_api_key)
    memory = ConversationBufferMemory()
    chatbot = ConversationChain(llm=model, memory=memory)

    # --- Step 3: Handle Conversation ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Say something")

    if prompt:
        response = chatbot.run(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)
else:
    st.warning("👆 Please enter your GROQ API key to start chatting.")
