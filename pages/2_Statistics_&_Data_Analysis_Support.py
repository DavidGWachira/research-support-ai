import streamlit as st

from services.openai_service import ask_openai
from services.prompts import STATS_PROMPT

st.title("📊 Statistics & Data Analysis Support")

# MEMORY INITIALIZATION
if "stats_messages" not in st.session_state:
    st.session_state.stats_messages = []

st.markdown("""
Describe your:
- research question
- dataset: population, variables
- statistical goals

Example:

'I have a longitudinal study dataset, the outcome is systolic blood pressure measured at
baseline, 3 months, and 6 months. 
Predictors include age, BMI, sex, and treatment group.
I want to understand whether treatment affects BP over time.'
""")

# MEMORY
if "stats_messages" not in st.session_state:
    st.session_state.stats_messages = []

# DISPLAY CHAT HISTORY
for message in st.session_state.stats_messages:

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
    st.session_state.stats_messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Generate AI response
    with st.spinner("Analyzing..."):

        response = ask_openai(
            STATS_PROMPT,
            st.session_state.stats_messages
        )

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save AI response
    st.session_state.stats_messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# CLEAR BUTTON
if st.button("Clear Conversation"):

    st.session_state.stats_messages = []

    st.rerun()


