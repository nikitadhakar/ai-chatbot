import os
import streamlit as st
from google import genai
from pathlib import Path

def load_css(file_path: str):
    css_file = Path(file_path)
    if css_file.exists():
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Configure page settings
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖  AI Assistant")
load_css("style.css")

# 1. Initialize API Client
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Please set the GEMINI_API_KEY environment variable.")
    st.stop()

client = genai.Client(api_key=api_key)

# 2. Maintain message history across user interactions
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Render previous messages in the conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle incoming user prompts
if prompt := st.chat_input(" Ask me anything..."):
    # Display and store user prompt
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Format conversation history for multi-turn context
    formatted_contents = [
        {"role": "model" if m["role"] == "assistant" else "user", "parts": [{"text": m["content"]}]}
        for m in st.session_state.messages
    ]

    # Generate and stream the assistant response
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        try:
            stream = client.models.generate_content_stream(
                model="gemini-3.6-flash",
                contents=formatted_contents,
            )

            for chunk in stream:
                if chunk.text:
                    full_response += chunk.text
                    response_container.markdown(full_response + "▌")

            response_container.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            # If high demand hits, show a friendly warning instead of crashing
            error_msg = str(e)
            if "503" in error_msg or "high demand" in error_msg.lower():
                st.warning("The model is experiencing temporary high traffic. Please wait a few seconds and send your message again.")
            else:
                st.error(f"Error: {e}")