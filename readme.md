# 🤖 Gemini AI Assistant

A sleek, responsive AI conversational web app built with Python, Streamlit, and Google's GenAI SDK. Features low-latency token streaming, context-aware memory, and an adaptive UI styled entirely with custom CSS.

---

## ✨ Features

- **⚡ Real-Time Streaming:** Responses stream word-by-word via `generate_content_stream` to eliminate user wait times.
- **🧠 Multi-Turn Memory:** Preserves full conversation context across prompts using Streamlit's session state.
- **🎨 Dynamic Center-to-Bottom Layout:** The input bar starts in the center of the viewport (ChatGPT/Gemini style) and smoothly transitions to the bottom once the conversation begins.
- **🌌 Custom Theming & Background:** Fully custom `style.css` featuring a dark slate palette, embedded pill-shaped input, and a subtle geometric tech doodle pattern.
- **🛡️ Resilient Error Handling:** Built-in catch routines for handling API rate limits and high-traffic server spikes.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Framework:** [Streamlit](https://streamlit.io/)
- **LLM SDK:** [Google GenAI SDK](https://github.com/googleapis/python-genai)
- **Styling:** Custom CSS (`style.css`) with SVG Data-URIs

---

## 📁 Project Structure

```text
ai-chatbot/
├── .streamlit/
│   └── config.toml       # (Optional) Global Streamlit theme overrides
├── app.py                # Core application logic and Streamlit UI
├── style.css             # Custom CSS styling and dynamic transitions
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules (protects API keys and venv)
└── README.md             # Project documentation