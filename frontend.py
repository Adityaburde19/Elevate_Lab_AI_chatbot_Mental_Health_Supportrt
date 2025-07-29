import streamlit as st
import requests
import uuid

# Create session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(page_title="🧠 Mental Health Chatbot", layout="centered")
st.title("🧠 Mental Health Support Chatbot")
st.markdown("Feel free to share your thoughts. This chatbot is here to listen and support you.")

user_input = st.text_input("You:", key="input", placeholder="Type something...")

if st.button("Send") and user_input:
    st.session_state.messages.append(("You", user_input))
    try:
        response = requests.post("http://127.0.0.1:5000/chat", json={
            "message": user_input,
            "session_id": st.session_state.session_id
        })

        if response.status_code == 200:
            reply = response.json()["response"]
        else:
            reply = response.json().get("error", "Error occurred.")
    except Exception as e:
        reply = "Could not connect to the chatbot backend."

    st.session_state.messages.append(("Bot", reply))

# Display messages in reverse order
st.divider()
for speaker, msg in reversed(st.session_state.messages):
    st.markdown(f"**{speaker}:** {msg}")
