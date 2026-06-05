from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables

#
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)
#

def ask_openai(system_prompt, chat_history):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Add previous conversation
    messages.extend(chat_history)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content

