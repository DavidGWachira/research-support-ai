import streamlit as st

from services.openai_service import ask_openai
from services.prompts import LITERATURE_SEARCH_PROMPT

st.title("🔍 Literature Search Strategy Support")

# MEMORY INITIALIZATION
if "lit_messages" not in st.session_state:
    st.session_state.lit_messages = []

st.markdown("""
Describe your:
- research question or topic
- any limits or requirements for the literatute search

Example:

'I am interested in the effects of social isolation on depression 
among older adults in rural communities.'
""")

# MEMORY
if "lit_messages" not in st.session_state:
    st.session_state.lit_messages = []

# DISPLAY CHAT HISTORY
for message in st.session_state.lit_messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# CHAT INPUT
user_input = st.chat_input(
    "Ask Anything..."
)

if user_input:

    # Show user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message
    st.session_state.lit_messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate AI response
    with st.spinner("Analyzing..."):

        response = ask_openai(
            LITERATURE_SEARCH_PROMPT,
            st.session_state.lit_messages
        )

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save AI response
    st.session_state.lit_messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# CLEAR BUTTON
if st.button("Clear Conversation"):

    st.session_state.lit_messages = []

    st.rerun()


