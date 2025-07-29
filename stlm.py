import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time

llm = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)
def get_response(user_input):
    chain = prompt | llm
    return chain.invoke({"question": user_input})

def generate_response(user_input):
     time.sleep(2)
     return f"Response to: {user_input}"

st.title("AI ChatBot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("You: ", key="input")

if user_input:
        with st.spinner('Generating Response.....'):
            response=generate_response(user_input)
            response = get_response(user_input)
            st.session_state.chat_history.append({"user": user_input, "bot": response})

if st.session_state['chat_history']:
    for chat in st.session_state['chat_history']:
        st.write(f"You: {chat['user']}")
        st.write(f"Bot: {chat['bot']}")