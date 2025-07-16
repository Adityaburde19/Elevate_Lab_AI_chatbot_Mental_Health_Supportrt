import streamlit as st
import requests

st.set_page_config(page_title="Mental Health Support Chatbot")

st.title("🧠 Mental Health Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    st.session_state.chat.append(("You", user_input))
    response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input})
    bot_reply = response.json()["response"]
    st.session_state.chat.append(("Bot", bot_reply))

for speaker, msg in reversed(st.session_state.chat):
    st.markdown(f"**{speaker}:** {msg}")
