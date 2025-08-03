import google.generativeai as genai
import streamlit as st
from PIL import Image

# 🌐 Styling
st.set_page_config(page_title="Image Analytics AI", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
    }
    .block-container {
        padding: 2rem;
        border-radius: 12px;
        background: #1e1e1e;
        box-shadow: 0px 0px 20px #F3E8FF;
    }
    h1, h2, h3 {
        color: #00fff7;
    }
    input, .stTextInput>div>div>input {
        background-color: #333 !important;
        color: #fff !important;
        border: 1px solid #F3E8FF !important;
    }
    .stButton>button {
        background-color: #F3E8FF;
        color: #000;
        font-weight: bold;
        padding: 0.5rem 1.5rem;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #F3E8FF;
        box-shadow: 0 0 10px #00fff7;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# 🔐 Configure Gemini
api_key = <"Your API Key">
genai.configure(api_key=api_key)

# 🧠 App Title
st.header("🤖 AI-Powered Image Analytics")

# 📁 File Uploader
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(Image.open(uploaded_file), caption="Uploaded Image", use_column_width=True)

# 📝 Text Prompt
prompt = st.text_input("💬 What do you want to ask about the image?")

# 🔍 Generate AI Response
if st.button("✨ GET RESPONSE"):
    if uploaded_file is not None and prompt:
        img = Image.open(uploaded_file)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([prompt, img])
        st.markdown(f"### 🔎 AI Response:\n{response.text}")
    else:
        st.warning("Please upload an image and enter a prompt.")
