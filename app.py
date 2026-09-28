import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables from .env file
load_dotenv()

#Get API key
api_key = os.getenv("GEMINI_API_KEY")

#create Gemini client
client = genai.Client(api_key=api_key)

#Page configuration
st.set_page_config(
    page_title="Gemini AI App",
    page_icon="🤖",
    layout="centered"
)

#Title
st.title("🤖 Gemini AI chatbot")

st.write("Ask Gemini anything!")

#User prompt
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)

#Generate button
if st.button("Generate Response"):

    if prompt:

        with st.spinner("Gemini is thinking..."):

            response = client.generate_text(
                model = "gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("Response generated!")

        st.write(response.text)

    else:
        st.warning("Please enter a prompt.")